from sqlalchemy import insert 
from creatingtable import user_table,comments_table
from connect1 import engine

statement=insert(user_table).values(name='shreya',fullname='shreya ghadge')

with engine.connect() as conn:
    conn.execute(statement,[
        { 'name':'vivek','fullname':'vivek pisal'},
        {'name':'pooja','fullname':'pooja ghadge'},
        {'name':'indra','fullname':'indra ghadge'}
        
        
    ])
    conn.commit()



