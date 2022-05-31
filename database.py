from sqlmodel import SQLModel, create_engine
import os

mariadb_file_name = "database.py"
mariadb_url = f"mariadb:///{mariadb_file_name}"

engine = create_engine(mariadb_url,echo=True)