import qrcode
from io import BytesIO
from typing import Optional
from sqlalchemy.orm import Session
from models import QRCode


class QRService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def generate_qr(self, url: str) -> bytes:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        return buffer.getvalue()

    def get_or_create_qr(self, url: str) -> Optional[bytes]:
        qr_record = self.db.query(QRCode).filter(QRCode.url == url).first()

        if not qr_record:
            qr_data = self.generate_qr(url)
            qr_record = QRCode(url=url, qr_data=qr_data)
            self.db.add(qr_record)
            self.db.commit()

        return qr_record.qr_data