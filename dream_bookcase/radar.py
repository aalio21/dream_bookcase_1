import matplotlib.pyplot as plt
import numpy as np
from .data import WORKS

def plot_ote_radar(title, savepath=None):
    """
    Plot a radar (spider) chart of Ontology/Teleology/Epistemology for the given work.
    """
    w = next((w for w in WORKS if w["title"] == title), None)
    if not w:
        raise ValueError(f"Work '{title}' not found in data.")

    labels = ["Ontology", "Teleology", "Epistemology"]
    scores = [w["O"], w["T"], w["E"]]
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    # close the loop
    scores += scores[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
    ax.plot(angles, scores, '-o', linewidth=2)
    ax.fill(angles, scores, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax.set_ylim(0, 5)
    plt.title(title, y=1.08)
    if savepath:
        plt.savefig(savepath)
    plt.show()
