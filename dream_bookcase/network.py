import networkx as nx
from pyvis.network import Network
from .data import WORKS

def build_network_html(output_file="dream_bookcase_network.html"):
    """
    Build an interactive HTML network where nodes are works,
    and edges connect works that share at least one theme.
    """
    G = nx.Graph()
    for w in WORKS:
        G.add_node(w["title"], title=", ".join(w["themes"]))

    # connect works sharing themes
    for i, w1 in enumerate(WORKS):
        for w2 in WORKS[i+1:]:
            if set(w1["themes"]) & set(w2["themes"]):
                G.add_edge(w1["title"], w2["title"])

    net = Network(height="750px", width="100%", notebook=False)
    net.from_nx(G)
    net.write_html(output_file)
    print(f"Network graph written to {output_file}")
