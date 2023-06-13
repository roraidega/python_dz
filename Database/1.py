"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов, получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

datab = "sqlite:///db_films.sql"
engine = create_engine(datab)


class Base(DeclarativeBase): pass
#базовый класс для моделей

class Films(Base):
    __tablename__ = 'Films'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(String)
    genre = Column(String)
    rating = Column(Integer)

Base.metadata.create_all(bind=engine)

def create(fi_name, fi_date, fi_genre, fi_rating):
    with Session(autoflush=False, bind=engine) as bd:
        f = Films(name = fi_name, date = fi_date, genre = fi_genre, rating = fi_rating)
        bd.add(f)
        bd.commit()

create('Дневники вампира', '2009', 'Драма', '8')
create('Бумажный дом', '2017', 'Боевик', '8,1')
create('Очень странные дела', '2016', 'Ужасы', '8,4')
create('Киберсталкер', '2019', 'Драма', '7,2')

def get_info():
    with Session(autoflush=False, bind=engine) as bd:
        f = bd.query(Films).all()
        for i in f:
            print(i.name)

def delete(id_del):
     with Session(autoflush=False, bind=engine) as bd:
        kill = bd.query(Films).filter(Films.id==id_del).first() #получаем первую запись из таблицы 
        bd.delete(kill)
        bd.commit()

delete(3)
