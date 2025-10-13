# app.py
"""
Main Flask application
"""
from flask import Flask, jsonify
from flask_cors import CORS
from extensions import db, ma
from config import config


def create_app():
    """Create and configure Flask app"""
    app = Flask(__name__)
    app.config.from_object(config['development'])
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    
    # Enable CORS
    CORS(app, origins=['http://localhost:5173'])
    
    # Register route blueprints
    from routes.memberships import memberships_bp
    app.register_blueprint(memberships_bp)
    
    # Basic routes
    @app.route('/')
    def home():
        return jsonify({'message': 'Catering Booking API', 'status': 'running'})
    
    @app.route('/api/health')
    def health():
        try:
            from models import Membership
            count = Membership.query.count()
            return jsonify({'status': 'healthy', 'memberships': count})
        except:
            return jsonify({'status': 'error'}), 500
    
    return app


def init_db(app):
    """Create tables and add sample data"""
    with app.app_context():
        db.create_all()
        print("✅ Tables created")
        
        from models import Membership
        if Membership.query.count() == 0:
            hallow = Membership(
                account_name="Hallow Family",
                email="hallow@example.com",
                phone="555-0001"
            )
            hallow.set_password("password123")
            
            george = Membership(
                account_name="George",
                email="george@example.com",
                phone="555-0002"
            )
            george.set_password("password123")
            
            db.session.add_all([hallow, george])
            db.session.commit()
            print("✅ Sample data added")


if __name__ == '__main__':
    app = create_app()
    init_db(app)
    app.run(debug=True, port=5555)