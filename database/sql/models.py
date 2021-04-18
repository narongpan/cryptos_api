from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Table
from .postgres import Base

# user_role_table = Table(
#     "user_role",
#     Base.metadata,
#     Column("user_id", Integer, ForeignKey("user.id")),
#     Column("role_id", Integer, ForeignKey("role.id"))
# )


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    wallet = relationship("Wallet", back_populates="owner")
    # roles = relationship("Role", back_populates="users",
    #                      secondary=user_role_table)


role_permission_table = Table(
    "role_permission",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("role.id")),
    Column("permission_id", Integer, ForeignKey("permission.id"))
)


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)

    permissions = relationship(
        "Permission", back_populates="roles", secondary=role_permission_table)
    # users = relationship("User", back_populates="roles",
    #                      secondary=user_role_table)


class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)

    roles = relationship("Role", back_populates="permissions",
                         secondary=role_permission_table)


class Wallet(Base):
    __tablename__ = "wallet"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="wallet")


class Coin(Base):
    __tablename__ = "coin"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    logo = Column(String, nullable=True)

# class CoinPrice(Base):
#     __tablename__ = "coin_price"

#     id = Column(Integer, primary_key=True, index=True)
