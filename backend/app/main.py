"""
Main Application Entry Point
FastAPI application with all feature routers
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import settings

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.log_level),
    format=settings.log_format
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")
    logger.info(f"Environment: {settings.environment}")
    logger.info(f"Debug mode: {settings.debug}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down application")


# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="""
    # Kundali API - Vedic Astrology Engine
    
    A comprehensive Vedic astrology API based on Brihat Parashara Hora Shastra (BPHS).
    
    ## Features
    
    - **Chart Calculation**: Generate accurate birth charts with planetary positions
    - **Dasha System**: Vimshottari Dasha calculations with Mahadasha, Antardasha, Pratyantardasha
    - **Yoga Detection**: Detect 100+ yogas including Raja, Dhana, Mahapurusha yogas
    - **Interpretation**: Comprehensive chart interpretation with life area analysis
    - **Remedies**: Traditional remedial measures based on planetary positions
    
    ## Technical Details
    
    - Uses Swiss Ephemeris for accurate astronomical calculations
    - Supports multiple Ayanamsa systems (Lahiri, Raman, Krishnamurti, etc.)
    - All calculations follow BPHS principles
    """,
    openapi_url=f"{settings.api_prefix}/openapi.json",
    docs_url=f"{settings.api_prefix}/docs",
    redoc_url=f"{settings.api_prefix}/redoc",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Import and include routers
from features.chart.router import router as chart_router
from features.dasha.router import router as dasha_router
from features.yoga.router import router as yoga_router
from features.interpretation.router import router as interpretation_router
from features.transits.router import router as transit_router

app.include_router(chart_router, prefix=settings.api_prefix)
app.include_router(dasha_router, prefix=settings.api_prefix)
app.include_router(yoga_router, prefix=settings.api_prefix)
app.include_router(interpretation_router, prefix=settings.api_prefix)
app.include_router(transit_router, prefix=settings.api_prefix)


# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version,
    }


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information"""
    return {
        "app": settings.app_name,
        "version": settings.app_version,
        "docs": f"{settings.api_prefix}/docs",
        "endpoints": {
            "chart": f"{settings.api_prefix}/chart",
            "dasha": f"{settings.api_prefix}/dasha",
            "yoga": f"{settings.api_prefix}/yoga",
            "interpretation": f"{settings.api_prefix}/interpretation",
        }
    }


# Combined calculation endpoint
@app.post(f"{settings.api_prefix}/calculate", tags=["Combined"])
async def calculate_all(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
    lat: float,
    lon: float,
    ayanamsa: str = "lahiri"
):
    """
    Calculate everything at once - chart, dasha, yogas, and interpretation.
    
    This is a convenience endpoint that combines all calculations.
    For more control, use the individual endpoints.
    """
    from datetime import date
    from app.dependencies import (
        get_chart_service,
        get_dasha_service,
        get_yoga_service,
        get_interpretation_service
    )
    
    # Get services
    chart_service = get_chart_service()
    dasha_service = get_dasha_service()
    yoga_service = get_yoga_service()
    interpretation_service = get_interpretation_service()
    
    # Calculate chart
    chart_data = chart_service.calculate_chart(
        year=year, month=month, day=day,
        hour=hour, minute=minute,
        latitude=lat, longitude=lon,
        ayanamsa=ayanamsa
    )
    
    # Calculate dasha
    moon_lon = chart_data.get("planets", {}).get("Moon", {}).get("longitude", 0)
    birth_date = date(year, month, day)
    dasha_data = dasha_service.calculate_full_dasha(
        moon_longitude=moon_lon,
        birth_date=birth_date,
        target_date=date.today(),
        include_antardashas=True
    )
    
    # Detect yogas
    yoga_data = yoga_service.detect_all_yogas(chart_data)
    
    # Generate interpretation
    interpretation = interpretation_service.generate_full_interpretation(
        chart_data=chart_data,
        yoga_data=yoga_data,
        dasha_data=dasha_data,
        depth="standard",
        include_remedies=True
    )
    
    return {
        "chart": chart_data,
        "dasha": dasha_data,
        "yogas": yoga_data,
        "interpretation": interpretation,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level=settings.log_level.lower()
    )
