"""
Application Configuration
Centralized configuration management using Pydantic Settings
"""

from typing import Optional
from pydantic_settings import BaseSettings
from functools import lru_cache
import os


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Application
    app_name: str = "Kundali API"
    app_version: str = "1.0.0"
    debug: bool = False
    environment: str = "development"
    
    # API Settings
    api_prefix: str = "/api/v1"
    allowed_origins: str = "http://localhost:5173,http://localhost:3000"
    
    # Database
    database_url: str = "sqlite:///./kundali.db"
    
    # Ephemeris
    ephemeris_path: Optional[str] = None
    default_ayanamsa: str = "lahiri"
    
    # Rate Limiting
    rate_limit_requests: int = 100
    rate_limit_period: int = 60  # seconds
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
    
    @property
    def allowed_origins_list(self) -> list[str]:
        """Parse allowed origins from comma-separated string"""
        return [origin.strip() for origin in self.allowed_origins.split(",")]
    
    @property
    def is_production(self) -> bool:
        return self.environment == "production"
    
    @property
    def is_development(self) -> bool:
        return self.environment == "development"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()


# Export singleton for easy access
settings = get_settings()
