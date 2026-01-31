"""
Dasha Feature - API Router
FastAPI routes for Dasha calculation endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict, Any, Optional
from datetime import date

from .schemas import DashaRequest, DashaResponse, AntardashaResponse
from .service import DashaService
from app.dependencies import get_dasha_service, get_ephemeris


router = APIRouter(prefix="/dasha", tags=["Dasha"])


@router.post(
    "/calculate",
    response_model=DashaResponse,
    summary="Calculate Vimshottari Dasha",
    description="""
    Calculate complete Vimshottari Dasha periods from birth details.
    
    The Vimshottari Dasha system (120-year cycle) is the most commonly used
    planetary period system in Vedic astrology, as described in BPHS Chapter 46.
    
    Returns:
    - Dasha balance at birth
    - All 9 Mahadasha periods with dates
    - Antardasha periods within each Mahadasha
    - Current running Dasha (if target_date provided)
    """
)
async def calculate_dasha(
    request: DashaRequest,
    dasha_service: DashaService = Depends(get_dasha_service),
    ephemeris = Depends(get_ephemeris)
) -> Dict[str, Any]:
    """Calculate Vimshottari Dasha periods"""
    try:
        # Determine Moon's longitude
        moon_longitude = request.moon_longitude
        
        # If Moon longitude not provided, calculate from birth data
        if moon_longitude is None:
            if all([request.year, request.month, request.day, request.lat, request.lon]):
                chart = ephemeris.calculate_full_chart(
                    year=request.year,
                    month=request.month,
                    day=request.day,
                    hour=request.hour or 12,
                    minute=request.minute or 0,
                    latitude=request.lat,
                    longitude=request.lon
                )
                moon_longitude = chart.planets["Moon"].longitude
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Either moon_longitude or complete birth details (year, month, day, lat, lon) required"
                )
        
        # Determine birth date
        if request.year and request.month and request.day:
            birth_date = date(request.year, request.month, request.day)
        else:
            # Default to a reference date if not provided
            birth_date = date(2000, 1, 1)
        
        # Target date for current dasha
        target_date = request.target_date or date.today()
        
        # Calculate full Dasha
        dasha_data = dasha_service.calculate_full_dasha(
            moon_longitude=moon_longitude,
            birth_date=birth_date,
            target_date=target_date,
            include_antardashas=True
        )
        
        return dasha_data
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Dasha calculation failed: {str(e)}"
        )


@router.post(
    "/current",
    summary="Get Current Dasha",
    description="Get the currently running Mahadasha, Antardasha, and Pratyantardasha"
)
async def get_current_dasha(
    request: DashaRequest,
    dasha_service: DashaService = Depends(get_dasha_service),
    ephemeris = Depends(get_ephemeris)
) -> Dict[str, Any]:
    """Get current running Dasha periods"""
    try:
        # Determine Moon's longitude
        moon_longitude = request.moon_longitude
        
        if moon_longitude is None:
            if all([request.year, request.month, request.day, request.lat, request.lon]):
                chart = ephemeris.calculate_full_chart(
                    year=request.year,
                    month=request.month,
                    day=request.day,
                    hour=request.hour or 12,
                    minute=request.minute or 0,
                    latitude=request.lat,
                    longitude=request.lon
                )
                moon_longitude = chart.planets["Moon"].longitude
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Either moon_longitude or complete birth details required"
                )
        
        # Determine birth date
        if request.year and request.month and request.day:
            birth_date = date(request.year, request.month, request.day)
        else:
            birth_date = date(2000, 1, 1)
        
        # Target date
        target_date = request.target_date or date.today()
        
        # Find current Dasha
        current = dasha_service.find_current_dasha(
            moon_longitude=moon_longitude,
            birth_date=birth_date,
            target_date=target_date
        )
        
        return current
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Current Dasha lookup failed: {str(e)}"
        )


@router.get(
    "/antardashas/{mahadasha_planet}",
    response_model=AntardashaResponse,
    summary="Get Antardashas for Mahadasha",
    description="Get all Antardasha periods for a specific Mahadasha planet"
)
async def get_antardashas(
    mahadasha_planet: str,
    start_date: date,
    duration_years: float,
    dasha_service: DashaService = Depends(get_dasha_service)
) -> Dict[str, Any]:
    """Get Antardasha periods for a Mahadasha"""
    try:
        # Validate planet
        valid_planets = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]
        if mahadasha_planet not in valid_planets:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid planet. Must be one of: {valid_planets}"
            )
        
        duration_days = int(duration_years * 365.25)
        
        antardashas = dasha_service.generate_antardashas(
            mahadasha_planet=mahadasha_planet,
            mahadasha_start=start_date,
            mahadasha_duration_days=duration_days
        )
        
        return {
            "mahadasha_planet": mahadasha_planet,
            "mahadasha_start": start_date,
            "mahadasha_end": start_date + timedelta(days=duration_days),
            "antardashas": antardashas
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Antardasha calculation failed: {str(e)}"
        )


# Import timedelta for the antardashas endpoint
from datetime import timedelta
