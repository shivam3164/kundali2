from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    locale = Column(String)
    timezone = Column(String)

class BirthProfile(Base):
    __tablename__ = 'birth_profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    date = Column(String)
    time = Column(String)
    place = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    tz = Column(String)
    dst = Column(String)
    ayanamsa = Column(String)
    chart_style = Column(String)

class PlanetPosition(Base):
    __tablename__ = 'planet_positions'
    id = Column(Integer, primary_key=True)
    birth_profile_id = Column(Integer)
    planet = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    speed = Column(Float)
    retrograde = Column(String)
    house = Column(Integer)
    nakshatra = Column(String)
    pada = Column(Integer)

class DashaTimeline(Base):
    __tablename__ = 'dasha_timelines'
    id = Column(Integer, primary_key=True)
    birth_profile_id = Column(Integer)
    dasha_type = Column(String)
    sequence = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

class YogaResult(Base):
    __tablename__ = 'yoga_results'
    id = Column(Integer, primary_key=True)
    birth_profile_id = Column(Integer)
    yoga_name = Column(String)
    strength = Column(Float)
    notes = Column(String)

class Interpretation(Base):
    __tablename__ = 'interpretations'
    id = Column(Integer, primary_key=True)
    birth_profile_id = Column(Integer)
    category = Column(String)
    text = Column(String)
    confidence = Column(Float)
