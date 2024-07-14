from sqlalchemy.orm import Session

from .product_model import Category, Item


def get_all_category(db: Session):
    return db.query(Category).all()


def get_one_by_category(cat_id: int, db: Session):
    return db.query(Item).filter(Item.category_id == cat_id).all()


def get_product_by_id(cat_name: str, item_id: int, db: Session):
    return db.query(Item).filter(Category.name == cat_name, Item.id == item_id).first()
