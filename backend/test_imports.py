#!/usr/bin/env python3
"""Test script to verify all module imports work correctly."""

import sys
import os

# Ensure backend directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test all module imports."""
    print("Testing imports...")
    print()
    
    # Test knowledge
    print("1. Testing knowledge module...")
    try:
        from knowledge import bphs_knowledge, BPHSKnowledge
        print("   ✓ Knowledge module imports work")
        print(f"   - Planets: {len(bphs_knowledge.planets)}")
        print(f"   - Signs: {len(bphs_knowledge.signs)}")
        print(f"   - Raja Yogas: {len(bphs_knowledge.raja_yogas)}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Test shared types
    print("2. Testing shared types...")
    try:
        from shared.types.common import BirthData, PlanetPosition, ChartData
        print("   ✓ Shared types import work")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Test ephemeris
    print("3. Testing ephemeris...")
    try:
        from shared.ephemeris.service import EphemerisService
        print("   ✓ Ephemeris service imports work")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Test app config
    print("4. Testing app config...")
    try:
        from app.config import Settings
        settings = Settings()
        print(f"   ✓ Settings: {settings.app_name}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Test chart feature
    print("5. Testing chart feature...")
    try:
        from features.chart.schemas import ChartRequest, ChartResponse
        from features.chart.service import ChartService
        print("   ✓ Chart feature imports work")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Test dasha feature
    print("6. Testing dasha feature...")
    try:
        from features.dasha.schemas import DashaRequest, DashaResponse
        from features.dasha.service import DashaService
        print("   ✓ Dasha feature imports work")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Test yoga feature
    print("7. Testing yoga feature...")
    try:
        from features.yoga.schemas import YogaRequest, YogaResponse
        from features.yoga.service import YogaService
        print("   ✓ Yoga feature imports work")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Test interpretation feature
    print("8. Testing interpretation feature...")
    try:
        from features.interpretation.schemas import InterpretationRequest, InterpretationResponse
        from features.interpretation.service import InterpretationService
        print("   ✓ Interpretation feature imports work")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print()
    print("✅ All module imports passed!")
    return True


if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)
