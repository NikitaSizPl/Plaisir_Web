from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    images_id = Column(Integer)
    images_url = Column(String)
    #  Зависимость таблицы и название "category"
    items = relationship("Item", back_populates="category")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    in_stock = Column(Boolean, default=True)
    images_id = Column(Integer)
    images_url = Column(String)
    innader_info = Column(String)

    # сделать имя категории
    #  Зависимость таблицы к классу "Product"
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="items")
