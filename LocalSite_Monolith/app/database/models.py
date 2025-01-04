from sqlalchemy import Table, Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    phone = Column(String, unique=True, index=True)
    address = Column(String)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, default="super thing")
    price = Column(String, nullable=False)
    image = Column(String, nullable=False)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    status = Column(String, default='pending')
    date = Column(String)
    total = Column(Integer)
    product_id = Column(Integer)  # Просто тест, в реале нужно выстроить отношения 
    user_id = Column(Integer)  # Просто тест, в реале нужно выстроить отношения 


def create_tables(engine) -> None:
    Base.metadata.create_all(bind=engine)