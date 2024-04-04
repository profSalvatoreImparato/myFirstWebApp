import hashlib
from datetime import datetime
import yaml

from starlette.responses import JSONResponse


def getConnectionParameters(datasource):
    with open('../config/config.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        for ds in data['datasources']:
            if ds["name"] == datasource:
                return {"user": ds["user"],
                        "password": ds["password"],
                        "host": ds["host"],
                        "port": ds["port"],
                        "db": ds["db"]}
        raise Exception("Connection not found")


def getVariables(datasource):
    with open('../config/config.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        for ds in data['variables']:
            if ds['name'] == datasource:
                return ds


def hashString(password: str):
    return hashlib.md5(password.encode('UTF-8')).hexdigest()


def createSuccessResponse(param):
    return {
        "date": str(datetime.now()),
        "success": True,
        "param": param,
        "code": 200,
    }


def getFormattedDateTime():
    return datetime.now().__str__() \
        .replace("-", "") \
        .replace(" ", "") \
        .replace(":", "") \
        .replace(".", "")


def createErrorResponse(error):
    return JSONResponse({
        "date": str(datetime.now()),
        "success": False,
        "error": {
            "message": error.message,
            "path": error.__module__
        },
        "code": error.code,
    }, error.code)


def arrayToJSON(array: list):
    res = []
    for element in array:
        res.append(element.toJSON())
    return res

BASE_URL = getVariables('local')['BASE_URL']
