from sqlmodel import SQLModel
from models import User
from database import engine

print("CREATING DATABASE....")

SQLModel.metadata.create_all(engine)