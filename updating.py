from sqlalchemy import update
from creatingtable import user_table
from connect1 import engine


statement=update(user_table).where(user_table.c.name=='indra').values(name='Indrajeet')
print(statement)
with engine.connect() as conn:
    conn.execute(statement)

    conn.commit()
