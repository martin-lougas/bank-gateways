import uuid
from typing import List, Optional
from sqlalchemy.orm import Session
from app.database.models import Authorization
from app.schemas.partner_schema import Authorization, Customer


# async def add_category(category: categories_schemas.Category, database: Session) -> categories_models.Category:
#     new_category = categories_models.Category(name=category.name)
#     database.add(new_category)
#     database.commit()
#     database.refresh(new_category)
#     return new_category


# async def get_categories(database: Session) -> List[categories_models.Category]:
#     return database.query(categories_models.Category).all()


async def get_category_by_id(user_uuid: uuid.UUID, database: Session) -> Optional[Authorization]:
    return database.query(Authorization.customer_id).filter(categories_models.Category.id == category_id).first()


# async def delete_category(category: categories_models.Category, database: Session) -> None:
#     database.delete(category)
#     database.commit()
