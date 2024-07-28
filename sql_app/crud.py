from sqlalchemy.orm import Session

from .product_model import Category, Item


def get_all_category(db: Session):
    return db.query(Category).all()


def get_one_by_category(cat_id: int, db: Session):
    return db.query(Item).filter(Item.category_id == cat_id).all()


def get_product_by_id(cat_id: int, item_id: int, db: Session):
    # Проверяем, существует ли категория
    category = db.query(Item).filter(Item.category_id == cat_id).all()
    if category:  # Если категория существует
        item = db.query(Item).filter(Item.id == item_id, Item.category_id == cat_id).first()
        return item  # Возвращаем товар, если он существует
    return None  # Возвращаем None, если категория не существует
