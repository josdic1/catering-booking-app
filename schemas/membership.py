# schemas/membership.py
"""
Marshmallow schema for Membership - Building step by step
"""
from extensions import ma
from models import Membership
from .member import MemberSchema #

class MembershipSchema(ma.SQLAlchemyAutoSchema):
    """
    This schema defines a Membership and includes its list of members.
    """
    # This line can now safely use the imported MemberSchema
    members = ma.Nested(MemberSchema, many=True, exclude=('membership',))

    class Meta:
        model = Membership
        load_instance = True
        include_fk = True


