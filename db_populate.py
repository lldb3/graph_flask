import sqlite3
import json
from sqlalchemy.orm import sessionmaker
from model import *
from base import Session, Base, engine


Base.metadata.create_all(engine)
session = Session()

conn = engine.connect()

f = open("csec_data_full.json", 'r')
csec_data = json.loads(f.read())
f.close()

for k in csec_data.keys():
    ka = csec_data[k]
    summary = ka['summary']
    essentials = str(ka['essentials'])
    ka_obj = KA(k, summary, essentials)
    session.add(ka_obj)
    

session.commit()
session.close()
