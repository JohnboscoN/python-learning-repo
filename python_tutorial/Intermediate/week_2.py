import pandas as pd

from sqlalchemy import (
    create_engine,
    inspect,
    text,
    select,
    MetaData,
    Table,
)


# Example: Create a database engine
# engine = create_engine("sqlite:///example.db")

# Example: Inspect database tables
# inspector = inspect(engine)
# print(inspector.get_table_names())
#print("Database tables inspected successfully.")

filepath = "/workspaces/python-learning-repo/python_tutorial/Intermediate/Data/903_database.db"

engine_903 = create_engine(f"sqlite+pysqlite:///{filepath}")
connection = engine_903.connect()

# Uncomment to check connection to database
# inspection = inspect(engine_903)
# table_names = inspection.get_table_names()
# print(table_names)


inspection = inspect(engine_903)
table_names = inspection.get_table_names()


# Uncomment to check connection to database
print(table_names)

metadata_903 = MetaData()

dfs = {}
for table in table_names:
    current_table = Table(table, metadata_903, autoload_with=engine_903)
    with engine_903.connect() as con:
        stmt = select(current_table)
        result = con.execute(stmt).fetchall()
    dfs[table] = pd.DataFrame(result)

print(dfs.keys())
print(dfs['header'])

from utils import clean_903_table

for key, df in dfs.items():
    dfs[key] = clean_903_table(df)