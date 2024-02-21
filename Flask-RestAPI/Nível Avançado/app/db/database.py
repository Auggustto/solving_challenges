from sqlalchemy import Integer, String, create_engine, Column, Date, ForeignKey, Time
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import date


engine = create_engine('sqlite:///blog.db')
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    birthdata = Column(Date, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    posts = relationship("Posting", back_populates="author")

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "birthdata": self.birthdata.strftime("%d/%m/%Y"),
            "email": self.email,
            "posts": [post.as_dict() for post in self.posts]
        }


class Posting(Base):
    __tablename__ = "posting"

    id = Column(Integer, primary_key=True)
    category = Column(String(30), nullable=False)
    post = Column(String)
    comment = Column(String)
    date = Column(Date)
    time = Column(Time)
    like = Column(Integer)
    deslike = Column(Integer)

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")

    def as_dict(self):
        return { 
            "id": self.id,
            "category": self.category,
            "post": self.post,
            "comment": self.comment,
            "date": self.date,
            "like": self.like,
            "deslike": self.deslike
        }


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()