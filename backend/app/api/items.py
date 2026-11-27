from fastapi import APIRouter, Depends, HTTPException, status, Query
from app.models import Item
from app.schemas import ItemUpdate, ItemResponse, ItemCreate
from typing import List, Optional
from app.database import get_db
from sqlalchemy.orm import Session
from app.api.exceptions import create_item_exception, update_item_exception


router = APIRouter(prefix="/items", tags=["Item Registry"])

db_dependency:Session = Depends(get_db)

@router.get("/", response_model=List[ItemResponse], status_code=status.HTTP_200_OK)
def get_items(
    keyword: Optional[str] = Query(None, description="Search for an item's name"),
    db = db_dependency
):
    query = db.query(Item)

    if keyword:
        query = query.filter(Item.name.ilike(f"%{keyword}%"))

    items = query.all()

    if not items:
        return []

    return items


@router.post("/", response_model=ItemResponse, status_code = status.HTTP_201_CREATED)
def create_item(
    item: ItemCreate,
    db = db_dependency
):
    check_existing = db.query(Item).filter(
        Item.name == item.name
    ).first()

    if check_existing:
        raise create_item_exception

    new_item = Item(
        name=item.name,
        price = item.price,
        stock = item.stock
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


@router.put("/{item_id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
def update_item(
    item_id: int,
    update_data: ItemUpdate,
    db = db_dependency
):
    item_to_update = db.query(Item).filter(
        Item.id == item_id
    ).first()

    if not item_to_update:
        raise update_item_exception

    item_update = update_data.model_dump(exclude_unset=True)

    for key, value in item_update.items():
        setattr(item_to_update, key, value)


    db.commit()
    db.refresh(item_to_update)

    return item_to_update

     