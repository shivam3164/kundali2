"""
Transit Analysis Router - API Endpoints for Transit Features.

Endpoints:
- /transit/analyze - Basic transit analysis
- /transit/enhanced - Enhanced 8-layer transit analysis
- /transit/area/{area} - Life area specific analysis
- /transit/ask - Natural language question answering
- /transit/timeline - 12-month outlook graph data
- /transit/current-positions - Current planetary positions
"""
from fastapi import APIRouter, HTTPException, Query
from datetime import datetime, date
from typing import Optional, Dict, List
from pydantic import BaseModel
import swisseph as swe

from .types import TransitRequest, TransitResponse, TransitReport
from .analyzer import create_transit_report
from .enhanced_analyzer import EnhancedTransitAnalyzer, create_enhanced_transit_report
from .area_analysis import analyze_area, get_all_area_analysis, AREA_ICONS
from .question_parser import process_question, parse_query
from .timeline_analysis import calculate_yearly_timeline, calculate_all_areas_timeline

router = APIRouter(prefix="/transit", tags=["Transit Analysis"])


# Request/Response models for new endpoints
class EnhancedTransitRequest(BaseModel):
    """Request for enhanced transit analysis"""
    year: int
    month: int
    day: int
    hour: int
    minute: int
    lat: float
    lon: float
    transit_year: Optional[int] = None
    transit_month: Optional[int] = None
    transit_day: Optional[int] = None


class AreaQueryRequest(BaseModel):
    """Request for area-specific analysis"""
    year: int
    month: int
    day: int
    hour: int
    minute: int
    lat: float
    lon: float
    area: str  # career, health, marriage, etc.


class QuestionRequest(BaseModel):
    """Request for natural language question"""
    year: int
    month: int
    day: int
    hour: int
    minute: int
    lat: float
    lon: float
    question: str


class TimelineRequest(BaseModel):
    """Request for 12-month timeline analysis"""
    year: int
    month: int
    day: int
    hour: int
    minute: int
    lat: float
    lon: float
    area: Optional[str] = None  # If None, returns all areas


def get_planetary_positions(year: int, month: int, day: int, hour: int = 12, minute: int = 0) -> dict:
    """
    Get planetary positions using Swiss Ephemeris.
    Returns sidereal longitudes (Lahiri ayanamsa).
    """
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    jd = swe.julday(year, month, day, hour + minute / 60.0)
    
    planets = {
        "Sun": swe.SUN,
        "Moon": swe.MOON,
        "Mars": swe.MARS,
        "Mercury": swe.MERCURY,
        "Jupiter": swe.JUPITER,
        "Venus": swe.VENUS,
        "Saturn": swe.SATURN,
        "Rahu": swe.TRUE_NODE,
    }
    
    positions = {}
    for name, code in planets.items():
        result = swe.calc_ut(jd, code, swe.FLG_SIDEREAL)
        positions[name] = result[0][0]  # Longitude
    
    # Ketu is always 180° from Rahu
    positions["Ketu"] = (positions["Rahu"] + 180) % 360
    
    return positions


def get_nakshatra_from_longitude(longitude: float) -> int:
    """Convert longitude to nakshatra index (1-27)."""
    return int(longitude // (360 / 27)) + 1


def get_sign_from_longitude(longitude: float) -> int:
    """Convert longitude to sign index (1-12)."""
    return int(longitude // 30) + 1


@router.post("/analyze", response_model=TransitResponse)
async def analyze_transits(request: TransitRequest):
    """
    Analyze planetary transits for a given birth chart and transit date.
    
    This endpoint combines:
    - BPHS Foundation: Basic Moon transit rules
    - Vedha: Obstruction analysis
    - Tara: Nakshatra-based strength
    - Murthi: Form quality (when available)
    
    **Request Body:**
    - Birth data: year, month, day, hour, minute, lat, lon
    - Transit date (optional): transit_year, transit_month, transit_day
      (defaults to current date if not provided)
    
    **Returns:**
    - Complete transit analysis with favorable/unfavorable planets
    - Detailed breakdown for each planet including Vedha and Tara
    """
    try:
        # Get natal chart Moon position
        natal_positions = get_planetary_positions(
            request.year, request.month, request.day,
            request.hour, request.minute
        )
        
        natal_moon_longitude = natal_positions["Moon"]
        natal_moon_sign = get_sign_from_longitude(natal_moon_longitude)
        natal_moon_nakshatra = get_nakshatra_from_longitude(natal_moon_longitude)
        
        # Get transit date (default to today)
        if request.transit_year and request.transit_month and request.transit_day:
            transit_date = date(request.transit_year, request.transit_month, request.transit_day)
        else:
            transit_date = date.today()
        
        # Get transit positions
        transit_positions = get_planetary_positions(
            transit_date.year, transit_date.month, transit_date.day
        )
        
        # Create transit report
        report = create_transit_report(
            natal_moon_sign=natal_moon_sign,
            natal_moon_nakshatra=natal_moon_nakshatra,
            natal_moon_longitude=natal_moon_longitude,
            transit_positions=transit_positions,
            transit_date=transit_date.strftime("%Y-%m-%d"),
            murthi_data=None  # Murthi requires historical data - can be added later
        )
        
        return TransitResponse(success=True, data=report)
        
    except Exception as e:
        return TransitResponse(success=False, error=str(e))


@router.get("/current-positions")
async def get_current_positions():
    """
    Get current planetary positions.
    
    Returns sidereal longitudes for all planets using Lahiri ayanamsa.
    Useful for debugging or displaying current sky positions.
    """
    try:
        today = date.today()
        positions = get_planetary_positions(today.year, today.month, today.day)
        
        # Add sign and nakshatra info
        detailed_positions = {}
        sign_names = ["", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                      "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
        nakshatra_names = [
            "", "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
            "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
            "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
            "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishtha",
            "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
        ]
        
        for planet, longitude in positions.items():
            sign = get_sign_from_longitude(longitude)
            nakshatra = get_nakshatra_from_longitude(longitude)
            detailed_positions[planet] = {
                "longitude": round(longitude, 2),
                "sign": sign_names[sign],
                "sign_degree": round(longitude % 30, 2),
                "nakshatra": nakshatra_names[nakshatra],
            }
        
        return {
            "date": today.strftime("%Y-%m-%d"),
            "positions": detailed_positions
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/quick-check")
async def quick_transit_check(
    moon_sign: int,
    moon_nakshatra: int
):
    """
    Quick transit check for a given Moon sign and nakshatra.
    
    This is a simplified endpoint for users who already know their
    Moon sign and nakshatra. Useful for daily transit checks.
    
    **Parameters:**
    - moon_sign: Natal Moon sign (1-12, where 1=Aries)
    - moon_nakshatra: Natal Moon nakshatra (1-27, where 1=Ashwini)
    
    **Returns:**
    - Today's transit analysis
    """
    try:
        today = date.today()
        transit_positions = get_planetary_positions(today.year, today.month, today.day)
        
        report = create_transit_report(
            natal_moon_sign=moon_sign,
            natal_moon_nakshatra=moon_nakshatra,
            natal_moon_longitude=(moon_sign - 1) * 30 + 15,  # Approximate
            transit_positions=transit_positions,
            transit_date=today.strftime("%Y-%m-%d"),
            murthi_data=None
        )
        
        return {
            "success": True,
            "date": today.strftime("%Y-%m-%d"),
            "overall": report.summary.overall_assessment,
            "favorable": report.favorable_planets,
            "unfavorable": report.unfavorable_planets,
            "details": [
                {
                    "planet": r.planet,
                    "sign": r.transit_sign_name,
                    "house": r.house_from_moon,
                    "status": r.final_status,
                    "tara": r.tara.tara_name,
                    "blocked": r.vedha.is_obstructed,
                }
                for r in report.analysis_results
            ]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/enhanced")
async def enhanced_transit_analysis(request: EnhancedTransitRequest):
    """
    Enhanced 8-layer transit analysis.
    
    Includes:
    - BPHS Foundation rules
    - Vedha obstruction analysis  
    - Tara nakshatra strength
    - Murthi form quality
    - Special Nakshatras (16 types)
    - Latta (Planetary Kicks)
    - Body Parts mapping
    - Ashtakavarga scoring
    
    Returns comprehensive transit report with life area impacts.
    """
    try:
        # Get natal positions
        natal_positions = get_planetary_positions(
            request.year, request.month, request.day,
            request.hour, request.minute
        )
        
        natal_moon_longitude = natal_positions["Moon"]
        natal_moon_sign = get_sign_from_longitude(natal_moon_longitude)
        natal_moon_nakshatra = get_nakshatra_from_longitude(natal_moon_longitude)
        
        # Calculate natal lagna (use Sun as approximate if needed)
        natal_lagna_longitude = natal_positions["Sun"]  # Simplified - ideally calculate true lagna
        natal_lagna_sign = get_sign_from_longitude(natal_lagna_longitude)
        natal_lagna_nakshatra = get_nakshatra_from_longitude(natal_lagna_longitude)
        
        # Get transit date
        if request.transit_year and request.transit_month and request.transit_day:
            transit_date = date(request.transit_year, request.transit_month, request.transit_day)
        else:
            transit_date = date.today()
        
        # Get transit positions
        transit_positions = get_planetary_positions(
            transit_date.year, transit_date.month, transit_date.day
        )
        
        # Create natal positions dict for Ashtakavarga
        natal_signs = {
            planet: get_sign_from_longitude(long) 
            for planet, long in natal_positions.items()
        }
        natal_signs["Lagna"] = natal_lagna_sign
        
        # Create enhanced report
        report = create_enhanced_transit_report(
            natal_moon_sign=natal_moon_sign,
            natal_moon_nakshatra=natal_moon_nakshatra,
            natal_moon_longitude=natal_moon_longitude,
            natal_lagna_sign=natal_lagna_sign,
            natal_lagna_nakshatra=natal_lagna_nakshatra,
            natal_positions=natal_signs,
            transit_positions=transit_positions,
            transit_date=transit_date.strftime("%Y-%m-%d"),
        )
        
        # Convert dataclasses to dicts for JSON response
        planet_results = []
        for r in report.planet_results:
            planet_results.append({
                "planet": r.planet,
                "transit_sign": r.transit_sign_name,
                "transit_nakshatra": r.transit_nakshatra_name,
                "house_from_moon": r.house_from_moon,
                "house_from_lagna": r.house_from_lagna,
                "basic_status": r.basic_status,
                "basic_prediction": r.basic_prediction,
                "vedha": r.vedha,
                "tara": r.tara,
                "murthi": r.murthi,
                "special_nakshatra": r.special_nakshatra,
                "latta": r.latta,
                "ashtakavarga": r.ashtakavarga,
                "final_status": r.final_status,
                "final_prediction": r.final_prediction,
                "confidence": r.confidence,
                "score": r.score,
            })
        
        return {
            "success": True,
            "native_data": report.native_data,
            "transit_date": report.transit_date,
            "planet_results": planet_results,
            "overall_summary": report.overall_summary,
            "latta_analysis": report.latta_analysis,
            "special_nakshatra_analysis": report.special_nakshatra_analysis,
            "body_parts_analysis": report.body_parts_analysis,
            "health_analysis": report.health_analysis,
            "ashtakavarga_summary": report.ashtakavarga_summary,
            "area_impacts": report.area_impacts,
            "favorable_planets": report.favorable_planets,
            "unfavorable_planets": report.unfavorable_planets,
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/area")
async def analyze_life_area(request: AreaQueryRequest):
    """
    Get detailed analysis for a specific life area.
    
    **Areas supported:**
    - career, job, business
    - finance, wealth, income
    - health, longevity
    - marriage, relationships, love
    - children, family
    - education, higher_education
    - travel, foreign
    - property, vehicles
    - legal, litigation
    - spirituality, moksha
    """
    try:
        # Get natal positions
        natal_positions = get_planetary_positions(
            request.year, request.month, request.day,
            request.hour, request.minute
        )
        
        natal_moon_longitude = natal_positions["Moon"]
        natal_moon_sign = get_sign_from_longitude(natal_moon_longitude)
        natal_moon_nakshatra = get_nakshatra_from_longitude(natal_moon_longitude)
        
        # Get current transit positions
        today = date.today()
        transit_positions = get_planetary_positions(today.year, today.month, today.day)
        
        # Create basic transit report first
        report = create_transit_report(
            natal_moon_sign=natal_moon_sign,
            natal_moon_nakshatra=natal_moon_nakshatra,
            natal_moon_longitude=natal_moon_longitude,
            transit_positions=transit_positions,
            transit_date=today.strftime("%Y-%m-%d"),
        )
        
        # Convert to dict format for area analysis
        transit_results = [
            {
                "planet": r.planet,
                "house_from_moon": r.house_from_moon,
                "house_from_lagna": r.house_from_moon,  # Simplified
                "final_status": r.final_status,
                "transit_sign": r.transit_sign_name,
            }
            for r in report.analysis_results
        ]
        
        # Analyze specific area
        area_result = analyze_area(request.area, transit_results)
        
        return {
            "success": True,
            "area": area_result.area,
            "display_name": area_result.area_display_name,
            "outlook": area_result.overall_outlook,
            "confidence": area_result.confidence,
            "score": area_result.score,
            "relevant_houses": area_result.relevant_houses,
            "planet_influences": area_result.planet_influences,
            "transit_impacts": area_result.transit_impacts,
            "prediction": area_result.short_term_prediction,
            "advice": area_result.advice,
            "strengths": area_result.strengths,
            "challenges": area_result.challenges,
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/ask")
async def ask_question(request: QuestionRequest):
    """
    Ask a natural language question about your chart.
    
    **Example questions:**
    - "How is my career looking?"
    - "Will I get married soon?"
    - "Is this a good time for travel?"
    - "What about my health?"
    - "Should I start a business?"
    """
    try:
        # Get natal positions
        natal_positions = get_planetary_positions(
            request.year, request.month, request.day,
            request.hour, request.minute
        )
        
        natal_moon_longitude = natal_positions["Moon"]
        natal_moon_sign = get_sign_from_longitude(natal_moon_longitude)
        natal_moon_nakshatra = get_nakshatra_from_longitude(natal_moon_longitude)
        
        # Get current transit positions
        today = date.today()
        transit_positions = get_planetary_positions(today.year, today.month, today.day)
        
        # Create transit report
        report = create_transit_report(
            natal_moon_sign=natal_moon_sign,
            natal_moon_nakshatra=natal_moon_nakshatra,
            natal_moon_longitude=natal_moon_longitude,
            transit_positions=transit_positions,
            transit_date=today.strftime("%Y-%m-%d"),
        )
        
        # Convert to dict format
        transit_results = [
            {
                "planet": r.planet,
                "house_from_moon": r.house_from_moon,
                "house_from_lagna": r.house_from_moon,
                "final_status": r.final_status,
                "transit_sign": r.transit_sign_name,
            }
            for r in report.analysis_results
        ]
        
        # Process question
        response = process_question(request.question, transit_results)
        
        return {
            "success": True,
            "question": response["question"],
            "answer": response["answer"],
            "confidence": response["confidence"],
            "area": response["area"],
            "detailed_analysis": response["detailed_analysis"],
            "follow_up_suggestions": response["follow_up_suggestions"],
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/areas")
async def get_available_areas():
    """
    Get list of all supported life areas for queries.
    """
    areas = [
        {"key": "career", "name": "Career & Profession", "icon": "💼"},
        {"key": "job", "name": "Job & Employment", "icon": "👔"},
        {"key": "business", "name": "Business", "icon": "🏢"},
        {"key": "finance", "name": "Finance & Money", "icon": "💰"},
        {"key": "wealth", "name": "Wealth & Assets", "icon": "💎"},
        {"key": "health", "name": "Health & Wellness", "icon": "❤️"},
        {"key": "marriage", "name": "Marriage", "icon": "💍"},
        {"key": "relationships", "name": "Relationships", "icon": "💕"},
        {"key": "love", "name": "Love & Romance", "icon": "❤️‍🔥"},
        {"key": "children", "name": "Children", "icon": "👶"},
        {"key": "education", "name": "Education", "icon": "📚"},
        {"key": "travel", "name": "Travel", "icon": "✈️"},
        {"key": "foreign", "name": "Foreign & Overseas", "icon": "🌍"},
        {"key": "property", "name": "Property & Real Estate", "icon": "🏠"},
        {"key": "family", "name": "Family", "icon": "👨‍👩‍👧‍👦"},
        {"key": "legal", "name": "Legal Matters", "icon": "⚖️"},
        {"key": "spirituality", "name": "Spirituality", "icon": "🙏"},
    ]
    return {"areas": areas}


@router.post("/timeline")
async def get_yearly_timeline(request: TimelineRequest):
    """
    Get 12-month transit outlook timeline for graphing.
    
    Returns monthly scores (0-100 scale) for the next 12 months.
    - 0-30: Challenging period
    - 30-50: Below average
    - 50: Neutral
    - 50-70: Above average
    - 70-100: Favorable period
    
    **Request Body:**
    - Birth data: year, month, day, hour, minute, lat, lon
    - area (optional): Specific area to analyze. If not provided, returns all areas.
    
    **Returns:**
    - 12-month timeline with scores for each month
    - Summary statistics (avg, min, max)
    - Best and worst months highlighted
    """
    try:
        # Get natal Moon position
        natal_positions = get_planetary_positions(
            request.year, request.month, request.day,
            request.hour, request.minute
        )
        
        natal_moon_longitude = natal_positions["Moon"]
        natal_moon_sign = get_sign_from_longitude(natal_moon_longitude)
        natal_moon_nakshatra = get_nakshatra_from_longitude(natal_moon_longitude)
        
        if request.area:
            # Single area timeline
            timeline = calculate_yearly_timeline(
                natal_moon_sign=natal_moon_sign,
                area=request.area,
            )
            
            return {
                "success": True,
                "area": request.area,
                "monthly_data": [
                    {
                        "month": score.month_name,
                        "year": score.year,
                        "normalized_score": score.normalized_score,
                        "raw_score": score.raw_score,
                        "outlook": score.brief_outlook,
                        "trend": score.trend,
                        "key_planets": score.key_planets,
                    }
                    for score in timeline.monthly_scores
                ],
                "summary": {
                    "average_score": timeline.average_score,
                    "peak_score": timeline.peak_score,
                    "lowest_score": timeline.lowest_score,
                    "best_months": timeline.best_months,
                    "challenging_months": timeline.challenging_months,
                    "overall_trend": timeline.overall_trend,
                },
            }
        else:
            # All areas timeline
            all_timelines = calculate_all_areas_timeline(
                natal_moon_sign=natal_moon_sign,
            )
            
            return {
                "success": True,
                "areas": {
                    area: {
                        "monthly_data": [
                            {
                                "month": score.month_name,
                                "year": score.year,
                                "normalized_score": score.normalized_score,
                                "outlook": score.brief_outlook,
                            }
                            for score in timeline.monthly_scores
                        ],
                        "summary": {
                            "average_score": timeline.average_score,
                            "peak_score": timeline.peak_score,
                            "lowest_score": timeline.lowest_score,
                            "best_months": timeline.best_months,
                            "challenging_months": timeline.challenging_months,
                        },
                    }
                    for area, timeline in all_timelines.items()
                },
            }
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

