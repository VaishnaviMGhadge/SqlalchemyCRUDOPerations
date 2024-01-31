from sqlalchemy import create_engine,text
from sqlalchemy import Integer,String,Column,Table,MetaData,insert
engine=create_engine(url="sqlite:///data.db",echo=True)
metaobj=MetaData()

User=Table('User',
    metaobj,
    Column('id',Integer,nullable=False),
    Column("name",String(20))
)
query=insert(User)
print(query)


with engine.connect() as conn:
    conn.execute(query,
                 [{'id':1,'name':'shreya'}])
    conn.commit()






    