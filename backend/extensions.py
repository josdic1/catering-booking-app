# extensions.py
"""
Shared extensions used across the app.
Initialize here to avoid circular imports.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize extensions (but don't attach to app yet)
db = SQLAlchemy()
ma = Marshmallow()