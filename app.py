from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from io import BytesIO
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from services import QRService
import logging
from models import Base

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)

engine = create_engine(Config.POSTGRES_URI)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

@app.before_request
def create_db_session():
    request.db = SessionLocal()


@app.teardown_request
def close_db_session(exc):
    if hasattr(request, 'db'):
        request.db.close()


@app.route('/api/qr', methods=['GET'])
def get_qr():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    try:
        qr_service = QRService(request.db)
        qr_data = qr_service.get_or_create_qr(url)

        buffer = BytesIO(qr_data)
        return send_file(buffer, mimetype='image/png')
    except Exception as e:
        logging.error(f"Error generating QR code: {str(e)}")
        return jsonify({'error': 'Failed to generate QR code'}), 500