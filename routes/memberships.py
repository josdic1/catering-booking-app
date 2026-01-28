# routes/memberships.py
"""
Membership routes
"""
from flask import Blueprint, request, jsonify
from extensions import db
from models import Membership
from schemas import membership_admin_schema

memberships_bp = Blueprint('memberships', __name__, url_prefix='/api/memberships')


@memberships_bp.route('/api/memberships/<int:id>')
def get_membership(id): 
    membership = Membership.query.get_or_404(id)
    membership_data = membership_admin_schema.dump(membership)
    return jsonify(membership_data) 


@memberships_bp.route('/admin', methods=['GET'])
def admin_get_all():
    """Get all memberships"""
    memberships = Membership.query.all()
    result = [membership_admin_schema.dump(m) for m in memberships]
    return jsonify(result), 200


