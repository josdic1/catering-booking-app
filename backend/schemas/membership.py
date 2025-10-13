# schemas/membership.py
"""
Marshmallow schemas for Membership model
Building step by step
"""
from extensions import ma
from models.membership import Membership

# ======================================================================
# ADMIN SCHEMA - Version 1 (Minimal)
# ======================================================================

class MembershipAdminSchema(ma.SQLAlchemyAutoSchema):
    """
    Admin schema - Step 1: Just the basics
    """

    class Meta:
        model = Membership
        load_instance = True

# create instance
membership_admin_schema = MembershipAdminSchema()


