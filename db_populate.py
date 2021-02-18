import json
from model import *

Base.metadata.create_all(engine)
session = Session()

conn = engine.connect()

f = open("csec_data_full.json", 'r')
csec_data = json.loads(f.read())
f.close()


for k in csec_data.keys():
    ka = csec_data[k]
    summary = ka['summary']
    essentials = ka['essentials']
    ka_db_obj = KA(k, summary, essentials)
    session.add(ka_db_obj)
    for outcome in ka['outcomes']:
        outcome_db_obj = Outcome(outcome['name'], outcome['questions'], ka_db_obj)
        session.add(outcome_db_obj)
    for ku in ka['units']:
        ku_db_obj = KU(ku['name'], ku['description'], ka_db_obj)
        session.add(ku_db_obj)
        keys = list(ku.keys())[2:]
        for topic in keys:
            topic_db_obj = Topic(topic, ku[topic], ku_db_obj)
            session.add(topic_db_obj)
    

session.commit()
session.close()
