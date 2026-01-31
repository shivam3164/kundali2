"""
Interpretation Feature - API Router
FastAPI routes for chart interpretation endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict, Any, Optional

from .schemas import InterpretationRequest, InterpretationResponse
from .service import InterpretationService
from .house_analyzer import house_analyzer, get_house_analysis, get_single_house_analysis
from app.dependencies import (
    get_interpretation_service, 
    get_chart_service, 
    get_yoga_service,
    get_dasha_service,
    get_ephemeris
)


router = APIRouter(prefix="/interpretation", tags=["Interpretation"])


@router.post(
    "/full",
    response_model=InterpretationResponse,
    summary="Get Full Interpretation",
    description="""
    Get a comprehensive interpretation of the birth chart.
    
    Includes:
    - Overall summary with life themes
    - Planet interpretations
    - House interpretations
    - Life area analysis (career, relationships, etc.)
    - Yoga effects
    - Current Dasha interpretation
    - Remedial measures
    
    You can provide pre-calculated chart/yoga/dasha data or birth details.
    """
)
async def get_full_interpretation(
    request: InterpretationRequest,
    interpretation_service: InterpretationService = Depends(get_interpretation_service),
    chart_service = Depends(get_chart_service),
    yoga_service = Depends(get_yoga_service),
    dasha_service = Depends(get_dasha_service),
    ephemeris = Depends(get_ephemeris)
) -> Dict[str, Any]:
    """Get full chart interpretation"""
    try:
        # Get chart data
        chart_data = request.chart_data
        if chart_data is None:
            if not all([request.year, request.month, request.day, request.lat, request.lon]):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Either chart_data or complete birth details required"
                )
            
            chart_data = chart_service.calculate_chart(
                year=request.year,
                month=request.month,
                day=request.day,
                hour=request.hour or 12,
                minute=request.minute or 0,
                latitude=request.lat,
                longitude=request.lon,
                ayanamsa=request.ayanamsa
            )
        
        # Get yoga data
        yoga_data = request.yoga_data
        if yoga_data is None:
            yoga_data = yoga_service.detect_all_yogas(chart_data)
        
        # Get dasha data
        dasha_data = request.dasha_data
        if dasha_data is None and request.year:
            from datetime import date
            moon_lon = chart_data.get("planets", {}).get("Moon", {}).get("longitude", 0)
            birth_date = date(request.year, request.month, request.day)
            dasha_data = dasha_service.calculate_full_dasha(
                moon_longitude=moon_lon,
                birth_date=birth_date,
                target_date=date.today(),
                include_antardashas=False
            )
        
        # Generate interpretation
        areas = [a.value for a in request.areas] if request.areas else None
        
        interpretation = interpretation_service.generate_full_interpretation(
            chart_data=chart_data,
            yoga_data=yoga_data,
            dasha_data=dasha_data,
            areas=areas,
            depth=request.depth.value,
            include_remedies=request.include_remedies
        )
        
        return interpretation
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Interpretation failed: {str(e)}"
        )


@router.post(
    "/summary",
    summary="Get Interpretation Summary",
    description="Get a brief summary interpretation"
)
async def get_interpretation_summary(
    request: InterpretationRequest,
    interpretation_service: InterpretationService = Depends(get_interpretation_service),
    chart_service = Depends(get_chart_service),
    yoga_service = Depends(get_yoga_service)
) -> Dict[str, Any]:
    """Get brief interpretation summary"""
    try:
        # Get chart data
        chart_data = request.chart_data
        if chart_data is None:
            if not all([request.year, request.month, request.day, request.lat, request.lon]):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Either chart_data or complete birth details required"
                )
            
            chart_data = chart_service.calculate_chart(
                year=request.year,
                month=request.month,
                day=request.day,
                hour=request.hour or 12,
                minute=request.minute or 0,
                latitude=request.lat,
                longitude=request.lon,
                ayanamsa=request.ayanamsa
            )
        
        # Get yoga data
        yoga_data = request.yoga_data
        if yoga_data is None:
            yoga_data = yoga_service.detect_all_yogas(chart_data)
        
        # Generate summary only
        full_interp = interpretation_service.generate_full_interpretation(
            chart_data=chart_data,
            yoga_data=yoga_data,
            depth="brief",
            include_remedies=False
        )
        
        return {
            "overall_summary": full_interp.get("overall_summary"),
            "yoga_effects": full_interp.get("yoga_effects", [])[:5],
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Summary failed: {str(e)}"
        )


@router.post(
    "/area/{area}",
    summary="Get Area Interpretation",
    description="Get interpretation for a specific life area"
)
async def get_area_interpretation(
    area: str,
    request: InterpretationRequest,
    interpretation_service: InterpretationService = Depends(get_interpretation_service),
    chart_service = Depends(get_chart_service),
    yoga_service = Depends(get_yoga_service)
) -> Dict[str, Any]:
    """Get interpretation for a specific life area"""
    try:
        valid_areas = ["personality", "career", "relationships", "health", "wealth", "spirituality", "education", "family"]
        if area not in valid_areas:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid area. Must be one of: {valid_areas}"
            )
        
        # Get chart data
        chart_data = request.chart_data
        if chart_data is None:
            if not all([request.year, request.month, request.day, request.lat, request.lon]):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Either chart_data or complete birth details required"
                )
            
            chart_data = chart_service.calculate_chart(
                year=request.year,
                month=request.month,
                day=request.day,
                hour=request.hour or 12,
                minute=request.minute or 0,
                latitude=request.lat,
                longitude=request.lon,
                ayanamsa=request.ayanamsa
            )
        
        # Get yoga data
        yoga_data = yoga_service.detect_all_yogas(chart_data)
        
        # Generate area interpretation
        full_interp = interpretation_service.generate_full_interpretation(
            chart_data=chart_data,
            yoga_data=yoga_data,
            areas=[area],
            depth=request.depth.value,
            include_remedies=request.include_remedies
        )
        
        return {
            "area": area,
            "interpretation": full_interp.get("area_interpretations", {}).get(area, {}),
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Area interpretation failed: {str(e)}"
        )


# ============================================
# HOUSE INTERPRETATION ENDPOINTS
# ============================================

@router.post(
    "/houses",
    summary="Get All Houses Interpretation",
    description="""
    Get detailed interpretation for all 12 houses based on BPHS.
    
    Returns:
    - House significations from BPHS
    - Planet effects in each house
    - House lord placement effects (BPHS Ch. 24)
    - House strength calculation
    - Life areas summary
    - Remedial measures
    """
)
async def get_houses_interpretation(
    request: InterpretationRequest,
    chart_service = Depends(get_chart_service)
) -> Dict[str, Any]:
    """Get interpretation for all 12 houses"""
    try:
        # Get chart data
        chart_data = request.chart_data
        if chart_data is None:
            if not all([request.year, request.month, request.day, request.lat, request.lon]):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Either chart_data or complete birth details required"
                )
            
            chart_data = chart_service.calculate_chart(
                year=request.year,
                month=request.month,
                day=request.day,
                hour=request.hour or 12,
                minute=request.minute or 0,
                latitude=request.lat,
                longitude=request.lon,
                ayanamsa=request.ayanamsa
            )
        
        # Get house analysis
        house_interpretation = get_house_analysis(
            chart_data=chart_data,
            include_remedies=request.include_remedies
        )
        
        return {
            "success": True,
            "data": house_interpretation
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"House interpretation failed: {str(e)}"
        )


@router.post(
    "/houses/{house_num}",
    summary="Get Single House Interpretation",
    description="""
    Get detailed interpretation for a specific house (1-12) based on BPHS.
    
    Returns:
    - House significations
    - Planets in house effects
    - House lord placement effect
    - House strength
    - Remedies if weak
    """
)
async def get_single_house_interpretation(
    house_num: int,
    request: InterpretationRequest,
    chart_service = Depends(get_chart_service)
) -> Dict[str, Any]:
    """Get interpretation for a specific house"""
    try:
        if house_num < 1 or house_num > 12:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="House number must be between 1 and 12"
            )
        
        # Get chart data
        chart_data = request.chart_data
        if chart_data is None:
            if not all([request.year, request.month, request.day, request.lat, request.lon]):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Either chart_data or complete birth details required"
                )
            
            chart_data = chart_service.calculate_chart(
                year=request.year,
                month=request.month,
                day=request.day,
                hour=request.hour or 12,
                minute=request.minute or 0,
                latitude=request.lat,
                longitude=request.lon,
                ayanamsa=request.ayanamsa
            )
        
        # Get single house analysis
        planets = chart_data.get("planets", {})
        houses = chart_data.get("houses", {})
        
        house_interpretation = house_analyzer.analyze_single_house(
            house_num=house_num,
            houses=houses,
            planets=planets,
            include_remedies=request.include_remedies
        )
        
        return {
            "success": True,
            "house_number": house_num,
            "data": house_interpretation
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"House interpretation failed: {str(e)}"
        )
