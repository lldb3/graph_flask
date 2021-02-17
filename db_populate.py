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
    ka_obj = KA(k, summary, essentials)
    session.add(ka_obj)
    

session.commit()
session.close()
