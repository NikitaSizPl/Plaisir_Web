from pydantic import BaseModel
from sqlalchemy import Column, Integer
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Order(BaseModel):
    __tablename__ = 'orders'
    id: int
    name: str
    phone: int
    instagram: str
    telegram: int
    comment: str
