"""
Transit Analysis Module - Barrel File.

Exports the public API for transit analysis.
Foundation: BPHS (Brihat Parashara Hora Shastra)
Enhancement: Vedic Astrology: An Integrated Approach by P.V.R. Narasimha Rao
"""

# Types
from .types import (
    TransitStatus,
    MurthiType,
    TaraType,
    PlanetTransitResult,
    VedhaResult,
    TaraResult,
    MurthiResult,
    TransitSummary,
    TransitReport,
    TransitRequest,
    TransitResponse,
    SIGN_NAMES,
    NAKSHATRA_NAMES,
    PLANET_NAMES,
)

# BPHS Foundation
from .rules import MOON_TRANSIT_RULES

# Vedic Astro Enhancements
from .vedha import check_vedha_obstruction, VEDHA_RULES, get_vedha_house
from .taras import calculate_tara, is_favorable_tara, TARA_DATA
from .murthi import get_murthi_for_transit, get_murthi_modifier, MURTHI_DATA

# Main Analyzer
from .analyzer import TransitAnalyzer, create_transit_report

__all__ = [
    # Types
    "TransitStatus",
    "MurthiType", 
    "TaraType",
    "PlanetTransitResult",
    "VedhaResult",
    "TaraResult",
    "MurthiResult",
    "TransitSummary",
    "TransitReport",
    "TransitRequest",
    "TransitResponse",
    "SIGN_NAMES",
    "NAKSHATRA_NAMES",
    "PLANET_NAMES",
    
    # Foundation
    "MOON_TRANSIT_RULES",
    
    # Enhancements
    "check_vedha_obstruction",
    "VEDHA_RULES",
    "get_vedha_house",
    "calculate_tara",
    "is_favorable_tara",
    "TARA_DATA",
    "get_murthi_for_transit",
    "get_murthi_modifier",
    "MURTHI_DATA",
    
    # Main API
    "TransitAnalyzer",
    "create_transit_report",
]
