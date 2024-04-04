from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from starlette.templating import Jinja2Templates

from app.utils.utils import getConnectionParameters

params = getConnectionParameters("local")
DATABASE_URL = f"mysql://{params['user']}:@{params['host']}/{params['db']}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
sql = SessionLocal()
templates = Jinja2Templates(directory="view/templates")



