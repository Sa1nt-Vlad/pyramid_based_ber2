from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey
)

from pyramid_based_ber.models.meta import Base


class SauceDB(Base):
    __tablename__ = 'burgers'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    type = Column(Text)
    burger = Column(Integer, ForeignKey('models.burger.id'))


Index('my_index', SauceDB.id, unique=True, mysql_length=255)
