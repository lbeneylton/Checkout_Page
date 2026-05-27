from enum import Enum


class RoleType(str, Enum):
    admin = "admin"
    client = "client"
    vendedor = "vendedor"
