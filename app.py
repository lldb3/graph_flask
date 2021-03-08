from flask import Flask, render_template
from graphmaker import *
from graphviz import Graph

app = Flask(__name__)


@app.route('/')
def hello_world():
    # kag = make_graph(k_areas, use_sub_topics=False, title="CSEC Global Map")
    # graph = kag.unflatten(stagger=22)
    # graph.format = 'svg'
    # graph.render(f"graphs/{graph.filename}")
    #
    # subs = make_ka_graphs(k_areas, use_sub_topics=True)
    # for s in subs:
    #     graph = s.unflatten(stagger=22)
    #     graph.format = 'svg'
    #     graph.render(f"graphs/{s.filename}")
    #
    # chart_output = graph.pipe(format='svg')

    return render_template('svgtest.html')

if __name__ == '__main__':
    app.run()
