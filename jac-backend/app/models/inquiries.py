
from datetime import datetime
from app.extensions import db

class Inquiry(db.Model):
    __tablename__ = "product_inquiries"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    message = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    product = db.relationship("Product", backref=db.backref("inquiries", lazy=True))
    
    
    
