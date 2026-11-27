from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from app.database import Base


class StockOut(Base):
    __tablename__ = "stock_out"

    id = Column(Integer, autoincrement=True, primary_key=True)
    dr_id = Column(Integer, ForeignKey("dr_orders.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    quantity =  Column(Integer, nullable=False, default=0)

    item_out: Mapped["Item"] = relationship(back_populates="outgoing_item") 