# routes/memberships.py
"""
API routes for memberships
"""
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from extensions import db
from models import Membership
from schemas.membership import membership_admin_schema  

memberships_bp = Blueprint('memberships', __name__, url_prefix='/api/memberships')


@memberships_bp.route('/admin/<int:id>', methods=['GET'])
def test_minimal(id):
    membership = Membership.query.get_or_404(id)
    return jsonify(membership_admin_schema.dump(membership))

