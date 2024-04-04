from sqlalchemy import text

from app.configuration.config import sql
from app.model.entity.table1 import Table1


class Table1Repository:

    # get una riga utilizzando l'orm
    @classmethod
    def getOne(cls):
        row: Table1 = sql.query(Table1).first()
        return row

    # get più righe utilizzando l'ORM
    @classmethod
    def getAll(cls):
        rows: list[Table1] = sql.query(Table1).all()
        return rows

    # get righe in base al nome utilizzando l'ORM
    @classmethod
    def getByNameORM(cls, name: str):
        rows: list[Table1] = sql.query(Table1).filter(Table1.name == name).all()
        return rows

    # get righe in base al nome utilizzando una named query
    @classmethod
    def getByName(cls, name: str):
        rows: list[Table1] = sql.query(Table1).from_statement(
            text("SELECT * FROM table1 WHERE name = :name").params(name=name)
        ).all()
        return rows

    # elimina una riga dall'id
    @classmethod
    def deleteRowById(cls, id: int):
        sql.query(Table1).filter(Table1.id == id).delete()
        sql.commit()

    # aggiorna una riga
    @classmethod
    def updateRow(cls, id: int, newName: str):
        row: Table1 = sql.query(Table1).filter(Table1.id == id).first()
        row.name = newName
        sql.commit()
        return row
