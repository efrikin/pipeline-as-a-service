"""Script creating diagram"""
#!/usr/bin/python

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.vcs import Git
from diagrams.onprem.ci import GitlabCI
from diagrams.azure.general import Usericon


graph_attr = {
    "pad":"0",
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

with Diagram("New feature development in the App project",
             graph_attr=graph_attr,
             edge_attr=edge_attr,
             node_attr=node_attr,
             filename="first_approach",
             show=False,) as diag:

    with Cluster("", graph_attr=cluster_attr):

        cicd = GitlabCI("")

        user = Usericon(
                        fontsize="22",
                        fontcolor="black",
                        height="1.5",
                    )

        app_project = Git("\nApp project",
                        fontsize="22",
                        fontcolor="black",
                    )

        ci_project = Git("\nCI project",
                        fontsize="22",
                        fontcolor="black",
                    )

        # pylint: disable=W0106
        user >> Edge(
                        label="1.Creating branch",
                        color="black",
                        fontcolor="black",
                        fontsize="19",
                    ) >> app_project

        # pylint: disable=W0106
        app_project >> Edge(
                        label="2.Development new feature",
                        color="black",
                        fontcolor="black",
                        fontsize="19",
                    ) << cicd

        # pylint: disable=W0106
        app_project >> Edge(
                        label="3.Moving new feature",
                        style="dashed",
                        color="black",
                        fontcolor="black",
                        fontsize="19",
                    ) >> ci_project

        # pylint: disable=W0106
        ci_project >> Edge(
                        label="4.Updating version CI",
                        color="black",
                        fontcolor="black",
                        fontsize="19",
                    ) >> app_project
