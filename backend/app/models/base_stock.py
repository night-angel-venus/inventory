from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from app.database import Base


class BaseStock(Base):
    __tablename__ = "base_stock"

    id = Column(Integer, autoincrement=True, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)

    item: Mapped["Item"] = relationship(back_populates="base_stock_item")
