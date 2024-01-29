from sqlalchemy import Table,MetaData,Column
from sqlalchemy import Integer,String,Text,ForeignKey

"""
we need to create two tables 
1. User_Table [
            id primary key,
            name string,
            fullname string,
            email
        ]

2. Comment_table [
                id primary key,
                comment string,
                user_id foreign key(User_Table.id) 
            ]
"""
meta_obj=MetaData()

user_table=Table(
    "users",
    meta_obj,
    Column('id',Integer,primary_key=True),
    Column("name",String(25),nullable=False),
    Column("fullname",Text,nullable=False),
)

comments_table=Table(
    'comments',
    meta_obj,
    Column('id',Integer,primary_key=True),
    Column("fullname",Text,nullable=False),
    Column("User_id",ForeignKey('users.id'))

)
