# schemas/membership.py
"""
Marshmallow schema for Membership - Building step by step
"""

from extensions import ma
from models.membership import Membership

class MembershipAdminSchema(ma.SQLAlchemyAutoSchema):
    """Admin Schema - Step 1.: Bare Minimum"""
    class Meta:
        model = Membership
        load_instance = True

membership_admin_schema = MembershipAdminSchema()