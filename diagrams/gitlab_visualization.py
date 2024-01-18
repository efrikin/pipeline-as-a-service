
#!/usr/bin/python

from diagrams import Diagram, Cluster, Node, Edge
from diagrams.programming.flowchart import StartEnd
from diagrams.generic.blank import Blank

from urllib.request import urlretrieve


graph_attr = {
    "pad": "0",
    "fontsize": "22",
    "fontcolor": "black",
    "bgcolor": "transparent",
    "compund": "True",
    "concentrate": "true",
    "splines": "spline",
}

cluster_attr = {
    "bgcolor": "transparent",
    "fontcolor": "black",
    "fontsize": "18",
}

node_attr = {
    "fontsize": "20",
}

edge_attr = {
    "penwidth":"3.0",
}

stages = ["build", "test", "deploy"]
results = []

with Diagram("Pipeline visualization for apps/test project",
             graph_attr=graph_attr,
             edge_attr=edge_attr,
             node_attr=node_attr,
             filename="gitlab_visualization",
             show=False,) as diag:

    with Cluster("", graph_attr=cluster_attr):
        inv = Edge(style="invis",minlen="3")
        for stage in range(len(stages)):
            s = StartEnd(stages[stage], labelloc="c", height="3", width="3")
            results.append(s)
            results[stage-1] >> inv >> results[stage]
diag

