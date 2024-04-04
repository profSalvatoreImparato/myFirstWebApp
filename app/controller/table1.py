from fastapi import APIRouter
from starlette.requests import Request

from app.configuration.config import templates
from app.model.entity.table1 import Table1
from app.services.table1 import Table1Service
from app.utils.utils import arrayToJSON

table1Router = APIRouter()


# Rendering di una pagina html utilizzando Jinja
@table1Router.get("/one")
def getOne(request: Request) :
    row: Table1 = Table1Service.getOne()
    return templates.TemplateResponse(
        request=request,
        name="one.html",
        context={"id" : row.id, "name" : row.name}
    )


# Rendering di un endpoint JSON
@table1Router.get("/getByName/{name}")
def getByName(request: Request, name: str) :
    rows: list[Table1] = Table1Service.getByName(name)
    return arrayToJSON(rows)
