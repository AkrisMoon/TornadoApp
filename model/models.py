from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from tornado_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import insert
from datetime import datetime
from settings import settings


db = SQLAlchemy(url=f'postgresql+psycopg2://{settings.SQL_USER}:{settings.SQL_PASSWORD}@'
                    f'{settings.SQL_HOST}:{settings.SQL_PORT}/{settings.SQL_DATABASE}')

session = db.sessionmaker(expire_on_commit=False)

class Array(db.Model):
    __tablename__ = 'array'

    id = Column(BigInteger, primary_key=True)
    array = Column(ARRAY(String), unique=False)
    result_array = Column(ARRAY(String), unique=False)
    date_of_creation = Column(DateTime(timezone=True), onupdate=func.now())

    def save(self, array, result_array):
        new_object = Array(array=array, result_array=result_array, date_of_creation = datetime.utcnow())
        session.add(new_object)
        session.commit()
        return new_object

    def get_by_id(self, id):
        object = session.query(Array).get(id)
        session.commit()
        return object
