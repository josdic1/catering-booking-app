# cli.py
"""
Command-line interface for database operations
"""
from extensions import db
from models import Membership

def init_db_command(app):
    """Initialize the database"""
    with app.app_context():
        db.create_all()
        print("✅ Database tables created")

def seed_db_command(app):
    """Add sample data"""
    with app.app_context():
        if Membership.query.count() == 0:
            samples = [
                Membership(account_name="Hallow Family", max_guests=4),
                Membership(account_name="George", max_guests=4),
                Membership(account_name="Smith Family", max_guests=4),
            ]
            db.session.bulk_save_objects(samples)
            db.session.commit()
            print("✅ Sample data added")
        else:
            print("⚠️ Database already has data")

def reset_db_command(app):
    """Drop all tables and recreate"""
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("✅ Database reset")