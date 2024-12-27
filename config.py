from dataclasses import dataclass
from typing import Optional
import os

@dataclass
class Config:
    POSTGRES_URI: str = os.getenv('DATABASE_URL', 'postgresql://myuser:mypassword@localhost:5432/qrdb')
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'dev-secret-key')
    RATE_LIMIT: int = int(os.getenv('RATE_LIMIT', '100'))  # requests per minute
