from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import settings
##################################################################

asyncengine=create_async_engine(settings.DATABASE_ASYNC_URI)
#db_session=sessionmaker(autocommit=False,autoflush=False,bind=syncengine)
# async_session = sessionmaker(asyncengine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()   

async def async_main():
    #engine = create_async_engine(DATABASE_URL, future=True, echo=True)

    async with asyncengine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


######################################################
async def droptables():
    async with asyncengine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


###################################################################
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer,String, ForeignKey, Sequence,Enum
from sqlalchemy.sql import func

from datetime import tzinfo, timedelta, datetime

import uuid
from typing import List, Optional,Literal
from pydantic import BaseModel,EmailStr
from sqlalchemy.dialects.postgresql import UUID
# from pydantic.dataclasses import dataclass

#############################################################################
    #this is roles table along with its methods
############################################################################
class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True,autoincrement="auto")
    name = Column(String(80), unique=True)
    description = Column(String(255))

    def __repr__(self):
        return f"{self.name}"
    @staticmethod
    def tableroute():
        return "role"

class RoleModel(BaseModel):
    
    name : str 
    description : Optional[str]
    
    class Config:
        orm_mode = True
#############################################################################


###################################################################


class User(Base):
    """ User Model for storing user related details """
    __tablename__ = "user"
    id = Column(Integer(), primary_key=True,autoincrement="auto")
    uid = Column(UUID(as_uuid=True),unique=True,default=uuid.uuid4)
    email=Column(String(255), unique=True,nullable=False)
    username =Column(String(100),unique=True,nullable=False)
    first_name =Column(String(100),nullable=False)
    middle_name = Column(String(100),nullable=False)
    last_name= Column(String(100),nullable=False)
    password = Column(String(500),nullable=False)
    # date_registerd=Column(DateTime(),default=datetime.datetime.now().astimezone())
    date_registerd=Column(DateTime(timezone=True), default=func.now())
    confirmed_at=Column(DateTime(),nullable=True)
    active = Column(Boolean(),default=False)
    roles = relationship('Role', secondary='roles_users',backref=backref('users',cascade="all", lazy='dynamic'))
     
    def __repr__(self):
        return f"<User '{self.username}'>"

    @staticmethod
    def tableroute():
        return "user"
    
class UserModel(BaseModel):
    email : EmailStr 
    username: str
    first_name : str
    middle_name : Optional[str] = None 
    last_name : str 
    password : str 
    # date_registerd : datetime.datetime
    confirmed_at : Optional[datetime] 
    active :Optional[bool] 
    
    class Config:
        orm_mode = True
###########################################################################
    #this is for many to many roles models relationship 
############################################################################
class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(),ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))
    #users = relationship('User',backref=backref('users', lazy='dynamic'))

    def __repr__(self):
        return f"<UserRole '{self.role_id}'>"
###########################################################################
    #this is for many to many roles models relationship 
############################################################################       