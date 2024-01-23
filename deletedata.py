from sqlalchemy import delete
from creatingtable import user_table
from connect1 import engine


statement=delete(user_table).where(user_table.c.name=='Meena')


with engine.connect() as conn:
    conn.execute(statement)

    conn.commit()
