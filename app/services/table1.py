from app.model.entity.table1 import Table1
from app.model.repository.table1 import Table1Repository


class Table1Service:

    @classmethod
    def getOne(cls):
        row: Table1 = Table1Repository.getOne()
        return row

    @classmethod
    def getByName(cls, name: str):
        rows: list[Table1] = Table1Repository.getByName(name)
        return rows