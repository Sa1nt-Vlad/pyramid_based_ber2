from sqlalchemy import (
    Column,
    Index,
    Integer
)

from pyramid_based_ber.models.meta import Base


class PW(Base):
    __tablename__ = 'pws'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    value = Column(Integer)


Index('my_index', PW.id, unique=True, mysql_length=255)
