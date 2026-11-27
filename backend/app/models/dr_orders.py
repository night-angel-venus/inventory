from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import Mapped, relationship
from app.database import Base


class DR_Order(Base):
    __tablename__ = "dr_orders"

    id = Column(Integer, autoincrement=True, primary_key=True)
    order_no = Column(String(50), nullable=False, unique=True)
    date =  Column(Date, nullable=False)