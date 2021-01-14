from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Date,
    ForeignKey
)

from pyramid_based_ber.models.meta import Base


class OrderDB(Base):
    __tablename__ = 'orders'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    phone = Column(Text)
    address = Column(Text)
    time = Column(Date)
    burger = Column(Integer, ForeignKey('burgers.id'))


Index('my_index', OrderDB.id, unique=True, mysql_length=255)
