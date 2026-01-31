"""
Chart Feature - API Router
FastAPI routes for chart calculation endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict, Any

from .schemas import ChartRequest, ChartResponse
from .service import ChartService
from app.dependencies import get_chart_service


router = APIRouter(prefix="/chart", tags=["Chart"])


@router.post(
    "/calculate",
    response_model=ChartResponse,
    summary="Calculate Birth Chart",
    description="""
    Calculate a complete Vedic birth chart (Kundali) for given birth details.
    
    Returns:
    - Ascendant (Lagna) with sign, nakshatra, and degree
    - All 9 planets (Navagraha) with positions, nakshatras, and houses
    - 12 house cusps with lords
    - Planetary dignities (exalted, debilitated, own sign, etc.)
    - Combustion status
    - Aspects between planets
    """
)
async def calculate_chart(
    request: ChartRequest,
    chart_service: ChartService = Depends(get_chart_service)
) -> Dict[str, Any]:
    """Calculate birth chart from birth details"""
    try:
        chart_data = chart_service.calculate_chart(
            year=request.year,
            month=request.month,
            day=request.day,
            hour=request.hour,
            minute=request.minute,
            latitude=request.lat,
            longitude=request.lon,
            ayanamsa=request.ayanamsa
        )
        
        # Add optional fields from request
        if request.name:
            chart_data["birth_data"]["name"] = request.name
        if request.place_name:
            chart_data["birth_data"]["place_name"] = request.place_name
        
        return chart_data
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Chart calculation failed: {str(e)}"
        )


@router.post(
    "/summary",
    summary="Get Chart Summary",
    description="Get a human-readable summary of the birth chart"
)
async def get_chart_summary(
    request: ChartRequest,
    chart_service: ChartService = Depends(get_chart_service)
) -> Dict[str, Any]:
    """Get simplified chart summary"""
    try:
        chart_data = chart_service.calculate_chart(
            year=request.year,
            month=request.month,
            day=request.day,
            hour=request.hour,
            minute=request.minute,
            latitude=request.lat,
            longitude=request.lon,
            ayanamsa=request.ayanamsa
        )
        
        summary = chart_service.get_planet_summary(chart_data)
        
        return {
            "lagna": f"{chart_data['ascendant']['sign']} ({chart_data['ascendant']['nakshatra']})",
            "planets": summary,
            "moon_sign": chart_data.get("moon_sign", ""),
            "sun_sign": chart_data.get("sun_sign", ""),
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Chart summary failed: {str(e)}"
        )
