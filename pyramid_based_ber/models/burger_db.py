from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from pyramid_based_ber.models.meta import Base


class BurgerDB(Base):
    __tablename__ = 'burgers'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    bun = Column(Text)
    cutlet = Column(Text)


Index('my_index', BurgerDB.id, unique=True, mysql_length=255)
