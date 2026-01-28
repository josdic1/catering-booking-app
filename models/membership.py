# models/membership.py
"""
Membership model - represents a membership account
"""
from datetime import datetime, timezone
from extensions import db
import bcrypt

class Membership(db.Model):
    """
    Membership account (family or individual)
    Each membership can have multiple members and make reservations.
    """
    __tablename__ = 'memberships'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Core fields
    account_name = db.Column(db.String(100), nullable=False, unique=True)
    max_guests = db.Column(db.Integer, nullable=False, default=4)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    # Custom fields
    email = db.Column(db.String(120), unique=True, nullable=False, index=True) 
    phone = db.Column(db.String(20), nullable=True) 

    # Timestamps
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    # Password
    def set_password(self, password):
        """Set password (hashing to be implemented)"""
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password_bytes, salt)
        self.password_hash = hashed.decode('utf-8')

    def check_password(self, password):
        """Check password"""
        password_bytes = password.encode('utf-8')
        stored_hash_bytes = self.password_hash.encode('utf-8')
        return bcrypt.checkpw(password_bytes, stored_hash_bytes)
    

    def __repr__(self):
        return f'<Membership: {self.account_name}>'
    
    def __str__(self):
        return self.account_name