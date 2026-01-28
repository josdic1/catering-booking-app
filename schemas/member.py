# schemas/member.py
"""
Marshmallow schema for Member - Building step by step
"""

# Generated Schemas for Caterer

from extensions import ma
from models import Membership, Member

class MemberSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Member
        load_instance = True
        include_fk = True # Includes the foreign key