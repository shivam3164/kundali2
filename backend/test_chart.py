#!/usr/bin/env python3
"""Test chart calculation service"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shared.ephemeris.service import EphemerisService
from knowledge import bphs_knowledge
from features.chart.service import ChartService
import traceback

# Create service
ephemeris = EphemerisService()
chart_svc = ChartService(ephemeris=ephemeris, knowledge=bphs_knowledge)

# Test calculation
try:
    result = chart_svc.calculate_chart(
        year=1990,
        month=5, 
        day=15,
        hour=10,
        minute=30,
        latitude=28.6139,
        longitude=77.2090,
        ayanamsa='lahiri'
    )
    print('✅ Chart Calculation Success!')
    print()
    print(f'Ascendant: {result["ascendant"]["sign"]} at {result["ascendant"]["degree_in_sign"]:.2f}°')
    print()
    print('Planets:')
    for name, data in result["planets"].items():
        print(f'  {name:8}: {data["sign"]:12} at {data["degree_in_sign"]:5.2f}° (House {data["house"]}) - {data["dignity"]}')
except Exception as e:
    print(f'❌ Error: {e}')
    traceback.print_exc()
