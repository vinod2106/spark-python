from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String

class ConnectDb():
    engine = create_engine('sqlite:///tutorial.db',echo=True)
    metadata = MetaData(bind=engine)

    users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(40)),
                    Column('age', Integer),
                    Column('password', String),
                    )

    addresses_table = Table('addresses', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('user_id', None, ForeignKey('users.id')),
                        Column('email_address', String, nullable=False)
                        )

    # create tables in database
    metadata.create_all()

if __name__ == '__main__':
    pass