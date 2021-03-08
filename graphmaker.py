#!/usr/bin/env python3
import json
from model import *
from random import randint

Base.metadata.create_all(engine)
session = Session()

kas = session.query(KA).all()
json_root_obj = {'name': 'root', 'children': []}

for ka in kas:
    kus = session.query(KU).filter(KU.ka == ka).all()
    print(f'{ka.name} has {[ku.name for ku in kus]}')
    json_ka_obj = {'name': ka.name, 'children': []}
    for ku in kus:
        json_ku_obj = {'name': ku.name, 'children': []}
        topics = session.query(Topic).filter(Topic.ku == ku).all()
        for topic in topics:
            json_topic_obj = {'name': topic.name, 'value': randint(1, 55)}
            json_ku_obj['children'].append(json_topic_obj)
        json_ka_obj['children'].append(json_ku_obj)
    json_root_obj['children'].append(json_ka_obj)

with open('static/root.json', 'w') as f:
    f.write(json.dumps(json_root_obj, indent=2))
