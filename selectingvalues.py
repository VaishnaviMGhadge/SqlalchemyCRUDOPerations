from sqlalchemy import select
from creatingtable import user_table
from connect1 import engine

statement=select(user_table).where(user_table.c.name=='vivek')

with engine.connect() as conn:
    res=conn.execute(statement)
    for i in res:
        print(f' user name is {i.name}')
    conn.commit()