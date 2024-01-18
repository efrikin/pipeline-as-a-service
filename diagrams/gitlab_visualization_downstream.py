
#!/usr/bin/python

from diagrams import Diagram, Cluster, Node, Edge
from diagrams.onprem.vcs import Gitlab
from diagrams.programming.flowchart import StartEnd

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

stages = ["devops/ci\ntest job", "apps/test\nproject"]
results = []

with Diagram("Pipeline visualization for devops/ci project",
             graph_attr=graph_attr,
             edge_attr=edge_attr,
             node_attr=node_attr,
             filename="gitlab_visualization_downstream",
             show=False,) as diag:


    with Cluster("", graph_attr=cluster_attr):
        vis = Edge(
                label="Trigger job",
                minlen="3",
                fontsize="20",
                )
        for stage in range(len(stages)):
            s = StartEnd(stages[stage], labelloc="c", height="3", width="3")
            results.append(s)
            vis >> results[stage]
diag

