
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship
from app.database import Base
from typing import List

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)

    incoming_item:Mapped[List["StockIn"]] = relationship(back_populates="item_in")
    outgoing_item:Mapped[List["StockOut"]] = relationship(back_populates="item_out")

