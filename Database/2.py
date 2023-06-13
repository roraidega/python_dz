from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, Session, relationship

sql_database = "sqlite:///User_prof.db"
engine = create_engine(sql_database) #движок


class Base(DeclarativeBase):
    pass

asocciation_table = Table('asocciation_table', Base.metadata,
                          Column('user_post_id', Integer, ForeignKey('user_post.id')), #создаем таблицу связей между
                          Column('user_id', Integer, ForeignKey('user.id')))

class User_post(Base):
    __tablename__ = "user_post"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    list_user = relationship("User",secondary=asocciation_table, back_populates="user_post")



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    experience = Column(Integer)
    user_post_id = Column(Integer, ForeignKey("user_post.id"))
    user_post = relationship("User_post", secondary=asocciation_table, back_populates="list_user")



Base.metadata.create_all(bind=engine)
db = Session(autoflush=False, bind=engine)


with Session(autoflush=False, bind=engine) as db:
    user_post_1 = User_post(name="Дизайнер")
    user_post_2 = User_post(name="Программист")
    user_post_3 = User_post(name="Разработчик")

    db.add_all([user_post_1, user_post_2, user_post_3])
    db.commit()

    people_1 = User(name="Yana", experience = 20)
    people_2 = User(name="Ignat", experience = 21)
    people_3 = User(name="Nikita", experience = 22)
    people_1.user_post.append(user_post_1) # добавляем связь между объектами моделей User и User_post

    db.add_all([people_1, people_2, people_3])
    db.commit()


    user_input = input()
    users_db = db.query(User).filter(User.name == user_input).all()
    for i in users_db:
        for j in i.user_post:
            print(j.name)

    user_input = input()
    users_db = db.query(User).filter(User.experience >= 5).all()
    for i in users_db:
        for j in i.user_post:
            if j.name == user_input:
                print(i.name)

