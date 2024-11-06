from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


database_name = "empleados.sqlite"
# engine = create_engine(f"sqlite:///{database_name}")
engine = create_engine("sqlite:///empleados.sqlite")

Session = sessionmaker(bind=engine)
session = Session()

ModeloBase = declarative_base()