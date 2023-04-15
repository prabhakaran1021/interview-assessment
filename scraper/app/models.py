import datetime

from app.database import Base
from sqlalchemy import String, Integer, Column, Date, Float,DateTime

class BulkDeals(Base):
    id=Column(Integer,primary_key=True)
    deal_date=Column(Date,default=datetime.datetime.utcnow)
    security_code=Column(Integer)
    security_name=Column(String(128))
    client_name=Column(String(128))
    deal_type=Column(String(128))
    quantity=Column(Integer)
    price=Column(Float)
    created_at=Column(DateTime,default=datetime.datetime.utcnow)


