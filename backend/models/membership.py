# models/membership.py
"""
Membership model - represents a membership account
"""
from datetime import datetime, timezone
from extensions import db


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
    
    # Timestamps (timezone-aware)
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
    
    # Relationships (add later)
    # members = db.relationship('Member', backref='membership', lazy='dynamic')
    # reservations = db.relationship('Reservation', backref='membership', lazy='dynamic')
    
    def __repr__(self):
        return f'<Membership: {self.account_name}>'
    
    def __str__(self):
        return self.account_name