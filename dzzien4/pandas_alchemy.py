import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/runners_db',echo=True)

df = pd.read_sql_table('runs', engine)

print(df)
