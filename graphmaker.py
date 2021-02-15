#!/usr/bin/env python3

from graphviz import Digraph
import json

graphviz_special_chars = ':;"\''

k_areas = None
with open("csec_data_full.json", 'r') as f:
    k_areas = json.loads(f.read())


def make_graph(k_areas, use_sub_topics=True, title="Graph"):
    """
    Makes main overall graph
    """
    kag = Digraph(filename=f"{title}.gv", engine='dot', strict=False, node_attr={"fillcolor": "blue"})
    kag.attr(compound='true')
    for ka_name in k_areas.keys():
        print(ka_name)
        kag.node(f"cluster_{ka_name}", ka_name, shape='square')
        with kag.subgraph(name=f"cluster_{ka_name}") as kug:
            for k_unit in k_areas[ka_name]["units"]:
                kug.node(f"cluster_{k_unit['name']}", k_unit['name'], shape='diamond')
                kag.edge(f"cluster_{ka_name}", f"cluster_{k_unit['name']}")
                for topic_name in k_unit.keys():
                    if topic_name == "name" or topic_name == "description":
                        continue
                    with kug.subgraph(name=f"cluster_{topic_name}") as topic_graph:
                        topic_graph.node(f"cluster_{topic_name}", topic_name, shape='box')
                        kug.edge(f"cluster_{k_unit['name']}", f"cluster_{topic_name}")
                        if use_sub_topics == False:
                            break
                        for sub_topic in k_unit[topic_name]:
                            if ':' in sub_topic:
                                sub_topic = sub_topic.replace(':', '-')  # quick fix for gv format error
                            topic_graph.node(f"{topic_name}_{sub_topic}", sub_topic)
                            topic_graph.edge(f"cluster_{topic_name}", f"{topic_name}_{sub_topic}")
    return kag


def make_ka_graphs(k_areas, use_sub_topics=True, title="Graph"):
    """
    Makes a graph for each KA and returns array of graphs
    """
    kag_array = []
    for ka_name in k_areas.keys():
        print(ka_name)
        kag = Digraph(filename=f"{title}: {ka_name}.gv", engine='dot', strict=False, node_attr={"fillcolor": "blue"})
        kag.attr(compound='true')
        kag.node(f"{ka_name}", ka_name, shape='square')
        with kag.subgraph(name=f"cluster_{ka_name}") as kug:
            for k_unit in k_areas[ka_name]["units"]:
                kug.node(f"cluster_{k_unit['name']}", k_unit['name'], shape='diamond')
                kag.edge(f"{ka_name}", f"cluster_{k_unit['name']}")
                for topic_name in k_unit.keys():
                    if topic_name == "name" or topic_name == "description":
                        continue
                    with kug.subgraph(name=f"cluster_{topic_name}") as topic_graph:
                        topic_graph.node(f"cluster_{topic_name}", topic_name, shape='box')
                        kug.edge(f"cluster_{k_unit['name']}", f"cluster_{topic_name}")
                        if use_sub_topics == False:
                            break
                        for sub_topic in k_unit[topic_name]:
                            if ':' in sub_topic:
                                sub_topic = sub_topic.replace(':', '-')  # quick fix for gv format error
                            topic_graph.node(f"{topic_name}_{sub_topic}", sub_topic)
                            topic_graph.edge(f"cluster_{topic_name}", f"{topic_name}_{sub_topic}")
            kag_array.append(kag)
    return kag_array


kag = make_graph(k_areas, use_sub_topics=False, title="CSEC Global Map")
graph = kag.unflatten(stagger=22)
graph.format = 'svg'
graph.render(f"graphs/{graph.filename}")

subs = make_ka_graphs(k_areas, use_sub_topics=True)
for s in subs:
    graph = s.unflatten(stagger=22)
    graph.format = 'svg'
    graph.render(f"graphs/{s.filename}")
