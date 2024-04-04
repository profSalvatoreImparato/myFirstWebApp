from sqlalchemy import Column, Integer, String

from app.configuration.config import sql, Base


class Table1(Base):
    __tablename__ = 'table1'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(24), primary_key=True)

    def __init__(self, name):
        self.name = name

    def toJSON(self, **kvargs):
        obj = {
            "id": self.id,
            "name": self.name
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj