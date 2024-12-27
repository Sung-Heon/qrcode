from sqlalchemy import Column, String, LargeBinary, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class QRCode(Base):
    __tablename__ = 'qr_codes'

    url = Column(String, primary_key=True)
    qr_data = Column(LargeBinary, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'url': self.url,
            'created_at': self.created_at.isoformat()
        }