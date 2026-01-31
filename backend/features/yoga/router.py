"""
Yoga Feature - API Router
FastAPI routes for Yoga detection endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict, Any

from .schemas import YogaRequest, YogaResponse
from .service import YogaService
from app.dependencies import get_yoga_service, get_chart_service


router = APIRouter(prefix="/yoga", tags=["Yoga"])


@router.post(
    "/detect",
    response_model=YogaResponse,
    summary="Detect Yogas in Chart",
    description="""
    Detect all Yogas present in a birth chart following BPHS.
    
    Categories of Yogas detected:
    - **Raja Yogas**: Power, authority, fame
    - **Dhana Yogas**: Wealth and prosperity
    - **Pancha Mahapurusha**: 5 great person yogas
    - **Nabhash Yogas**: Pattern-based yogas
    - **Chandra Yogas**: Moon-based yogas
    - **Surya Yogas**: Sun-based yogas
    - **Daridra Yogas**: Poverty/obstacle yogas
    - **Viparita Raja Yogas**: Reverse fortune yogas
    
    You can either provide pre-calculated chart data or birth details.
    """
)
async def detect_yogas(
    request: YogaRequest,
    yoga_service: YogaService = Depends(get_yoga_service),
    chart_service = Depends(get_chart_service)
) -> Dict[str, Any]:
    """Detect all yogas in a birth chart"""
    try:
        # Get chart data
        chart_data = request.chart_data
        
        if chart_data is None:
            # Calculate chart from birth details
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
        
        # Detect yogas
        yoga_result = yoga_service.detect_all_yogas(chart_data)
        
        # Filter by categories if specified
        if request.categories:
            category_names = [c.value for c in request.categories]
            filtered_yogas = {
                cat: yogas for cat, yogas in yoga_result["yogas"].items()
                if cat in category_names
            }
            yoga_result["yogas"] = filtered_yogas
            yoga_result["all_yogas"] = [
                y for y in yoga_result["all_yogas"]
                if y["category"] in category_names
            ]
        
        # Filter negative yogas if not requested
        if not request.include_negative:
            yoga_result["yogas"]["daridra_yoga"] = []
            yoga_result["all_yogas"] = [
                y for y in yoga_result["all_yogas"]
                if y["category"] != "daridra_yoga"
            ]
        
        return yoga_result
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Yoga detection failed: {str(e)}"
        )


@router.post(
    "/summary",
    summary="Get Yoga Summary",
    description="Get a simplified summary of yogas in the chart"
)
async def get_yoga_summary(
    request: YogaRequest,
    yoga_service: YogaService = Depends(get_yoga_service),
    chart_service = Depends(get_chart_service)
) -> Dict[str, Any]:
    """Get simplified yoga summary"""
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
        
        # Detect yogas
        yoga_result = yoga_service.detect_all_yogas(chart_data)
        
        # Return just the summary with yoga names
        yoga_names = {
            category: [y["name"] for y in yogas]
            for category, yogas in yoga_result["yogas"].items()
            if yogas
        }
        
        return {
            "summary": yoga_result["summary"],
            "yogas_by_category": yoga_names,
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Yoga summary failed: {str(e)}"
        )
