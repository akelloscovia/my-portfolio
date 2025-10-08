from datetime import datetime
from app.extensions import db


class ContactInfo(db.Model):
    __tablename__ = "contact_info"

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    map_embed_url = db.Column(db.Text, nullable=True)  # Google Maps embed link
    working_hours = db.Column(db.String(255), nullable=True)
    additional_notes = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<ContactInfo {self.address}>"
