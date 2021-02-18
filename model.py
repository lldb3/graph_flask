from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres@localhost:5432/postgres', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class KA(Base):
    __tablename__ = "knowledge_area"
    name = Column(String, unique=True)
    description = Column(String)
    id = Column(Integer, primary_key=True)
    essentials = Column(ARRAY(String))

    def __init__(self, name, description, essentials):
        self.name = name
        self.description = description
        self.essentials = essentials


class KU(Base):
    __tablename__ = "knowledge_unit"
    name = Column(String)
    description = Column(String)
    id = Column(Integer, primary_key=True)
    ka_id = Column(Integer, ForeignKey("knowledge_area.id"))
    ka = relationship("KA")

    def __init__(self, name, description, ka):
        self.name = name
        self.description = description
        self.ka = ka


class Topic(Base):
    __tablename__ = "topic"
    name = Column(String)
    description = Column(ARRAY(String))
    id = Column(Integer, primary_key=True)
    ku_id = Column(Integer, ForeignKey('knowledge_unit.id'))
    ku = relationship("KU")

    def __init__(self, name, description, ku):
        self.name = name
        self.description = description
        self.name = name
        self.description = description
        self.ku = ku

    # TODO implement list of items for the description + spliting on ',' and 'and' keywords


class Outcome(Base):
    __tablename__ = "outcomes"
    name = Column(String)
    id = Column(Integer, primary_key=True)
    questions = Column(ARRAY(String))
    ka_id = Column(Integer, ForeignKey('knowledge_area.id'))
    ka = relationship("KA")

    def __init__(self, name, description, ka):
        self.name = name
        self.description = description
        self.questions = self.description_to_questions()
        self.ka = ka

    def description_to_questions(self):
        return self.description  # TODO desc to questions


class Reference(Base):
    __tablename__ = 'reference'
    id = Column(Integer, primary_key=True)
    type = Column(String)
