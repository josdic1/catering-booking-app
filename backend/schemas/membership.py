# schemas/membership.py
"""
Marshmallow schemas for Membership model
Building step by step
"""

from marshmallow import fields
from extensions import ma
from models.membership import Membership

#====================================================================
# ADMIN SCHEMA - Version 2
#=====================================================================

class MembershipAdminSchema(ma.SQLAlchemyAutoSchema):
    """
    Admin schema - Version 2
    Now controlling individual fields
    """

    class Meta:
        model = Membership
        load_instance = True
    
    # ========================================
    # FIELD OVERRIDES
    # ========================================

    # Override the auto-generated max_guests field
    max_guests = fields.Int(dump_only=True)
    

# create instance
membership_admin_schema = MembershipAdminSchema()
