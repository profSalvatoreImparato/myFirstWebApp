import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.configuration.config import Base, engine
from app.controller.table1 import table1Router

app = FastAPI()
#Qui aggiungiamo telle le nuove rotte presenti nella cartella controller
app.include_router(table1Router, prefix="/table1")

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, port=8000)
