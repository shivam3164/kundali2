"""
Dependency Injection Container
Provides factory functions for shared dependencies
"""

from typing import Generator, Optional
from functools import lru_cache

from .config import settings


# ============================================
# DATABASE DEPENDENCY
# ============================================

def get_db():
    """
    Database session dependency
    Usage: db: Session = Depends(get_db)
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session
    
    engine = create_engine(
        settings.database_url,
        connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {}
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============================================
# EPHEMERIS SERVICE DEPENDENCY
# ============================================

@lru_cache()
def get_ephemeris_service():
    """
    Get cached ephemeris service instance
    The ephemeris service is stateless and can be safely cached
    """
    from shared.ephemeris import EphemerisService
    return EphemerisService(ephemeris_path=settings.ephemeris_path)


def get_ephemeris():
    """
    Ephemeris service dependency for route injection
    Usage: ephemeris: EphemerisService = Depends(get_ephemeris)
    """
    return get_ephemeris_service()


# ============================================
# KNOWLEDGE BASE DEPENDENCY
# ============================================

@lru_cache()
def get_knowledge_base():
    """
    Get cached BPHS knowledge base
    """
    from knowledge import bphs_knowledge
    return bphs_knowledge


# ============================================
# FEATURE SERVICE FACTORIES
# ============================================

def get_chart_service():
    """Chart calculation service dependency"""
    from features.chart import ChartService
    return ChartService(
        ephemeris=get_ephemeris_service(),
        knowledge=get_knowledge_base()
    )


def get_dasha_service():
    """Dasha calculation service dependency"""
    from features.dasha import DashaService
    return DashaService(knowledge=get_knowledge_base())


def get_yoga_service():
    """Yoga detection service dependency"""
    from features.yoga import YogaService
    return YogaService(knowledge=get_knowledge_base())


def get_interpretation_service():
    """Interpretation service dependency"""
    from features.interpretation import InterpretationService
    return InterpretationService(knowledge=get_knowledge_base())
