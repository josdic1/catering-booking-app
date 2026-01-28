from .member import MemberSchema
from .membership import MembershipSchema

# Create instances that can be imported into your routes
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

membership_schema = MembershipSchema()
memberships_schema = MembershipSchema(many=True)