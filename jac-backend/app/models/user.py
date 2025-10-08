from datetime import datetime
from app.extensions import bcrypt
from app.extensions import migrate, db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    biography = db.Column(db.Text(), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(20), default='user')  # renamed from user_type
    contact = db.Column(db.Integer, nullable=False, unique=True)
    image = db.Column(db.String(250), nullable=True)
    gender = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, first_name, last_name, email, biography, contact, password, role='user', gender=None, address=None, image=None):
      self.first_name = first_name
      self.last_name = last_name
      self.email = email
      self.contact = contact
      self.address = address
      self.biography = biography
      self.password = password  
      self.gender = gender
      self.role = role
      self.image = image
      
      def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    def check_password(self, password_input):
        return bcrypt.check_password_hash(self.password, password_input)
