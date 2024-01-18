
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
    "fontsize": "19",
}

edge_attr = {
    "penwidth":"3.0",
}

stages = [
        "devops/ci\ngenerate-pipeline job",
        "devops/ci\ntest job",
        "apps/test\nproject"
        ]
results = []

with Diagram("Pipeline visualization for devops/ci project",
             graph_attr=graph_attr,
             edge_attr=edge_attr,
             node_attr=node_attr,
             filename="gitlab_visualization_downstream_second",
             show=False,) as diag:


    with Cluster("", graph_attr=cluster_attr):
        vis = Edge(
                label="Trigger job",
                minlen="3",
                fontsize="20",
            )

        vis_second = Edge(
                label="",
                fontsize="20",
                )

        for stage in range(len(stages)):
            s = StartEnd(stages[stage], labelloc="c", height="3", width="3")
            results.append(s)
        vis_second - results[0] - results[1] - vis >> results[2]
diag

