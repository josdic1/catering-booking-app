# routes/memberships.py
"""
API routes for memberships
"""
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from extensions import db
from models import Membership
from schemas import membership_schema, memberships_schema  # ← This should work now!

memberships_bp = Blueprint('memberships', __name__, url_prefix='/api/memberships')


@memberships_bp.route('', methods=['GET'])
def get_memberships():
    """Get all memberships"""
    memberships = Membership.query.order_by(Membership.account_name).all()
    return jsonify(memberships_schema.dump(memberships)), 200


@memberships_bp.route('/<int:id>', methods=['GET'])
def get_membership(id):
    """Get single membership"""
    membership = Membership.query.get_or_404(id)
    return jsonify(membership_schema.dump(membership)), 200


@memberships_bp.route('', methods=['POST'])
def create_membership():
    """Create new membership"""
    try:
        membership = membership_schema.load(request.json)
        db.session.add(membership)
        db.session.commit()
        return jsonify(membership_schema.dump(membership)), 201
    except ValidationError as err:
        return jsonify({'error': 'Validation failed', 'messages': err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@memberships_bp.route('/<int:id>', methods=['PATCH'])
def update_membership(id):
    """Update membership"""
    membership = Membership.query.get_or_404(id)
    
    try:
        updated = membership_schema.load(request.json, instance=membership, partial=True)
        db.session.commit()
        return jsonify(membership_schema.dump(updated)), 200
    except ValidationError as err:
        return jsonify({'error': 'Validation failed', 'messages': err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@memberships_bp.route('/<int:id>', methods=['DELETE'])
def delete_membership(id):
    """Soft delete membership"""
    membership = Membership.query.get_or_404(id)
    membership.is_active = False
    db.session.commit()
    return jsonify({'message': f'{membership.account_name} deactivated'}), 200