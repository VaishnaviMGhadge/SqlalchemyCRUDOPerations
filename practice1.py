from sqlalchemy import create_engine,text
from sqlalchemy import Integer,String,insert,MetaData,Table,Column

engine=create_engine(url='sqlite:///sample1.db',echo=True)
metaobj=MetaData()

usertable=Table('User',
                metaobj,
                Column("id",Integer),
                Column("name",String(20),nullable=False))

statement=insert(usertable)
print(statement)

with engine.connect() as conn:
    conn.execute(statement,{12,'vaishnavi'})
    conn.commit()