from sqlalchemy import *
from sqlalchemy.orm import relationship
from base import Base


class KA(Base):
    __tablename__ = "knowledge_area"
    name = Column(String, unique=True)
    description = Column(String)
    id = Column(Integer, primary_key=True)
    essentials = Column(String)

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

    def __init__(self, name, description, ka_id):
        self.name = name
        self.description = description
        self.ka_id = ka_id


class Topic(Base):
    __tablename__ = "topic"
    name = Column(String)
    description = Column(String)
    id = Column(Integer, primary_key=True)
    ku_id = Column(Integer, ForeignKey('knowledge_unit.id'))
    ku = relationship("KU")

    def __init__(self, name, description, ku_id):
        self.name = name
        self.description = description
        self.name = name
        self.description = description
        self.ku_id = ku_id

    # TODO implement list of items for the description + spliting on ',' and 'and' keywords


class Outcomes(Base):
    __tablename__ = "outcomes"
    name = Column(String)
    description = Column(String)
    id = Column(Integer, primary_key=True)
    questions = Column(String)
    ka_id = Column(Integer, ForeignKey('knowledge_area.id'))

    def __init__(self, name, description, ka_id):
        self.name = name
        self.description = description
        self.questions = self.description_to_questions()
        self.ka_id = ka_id

    def description_to_questions(self):
        return self.description  # TODO desc to questions


class Reference(Base):
    __tablename__ = 'reference'
