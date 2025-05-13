import matplotlib.pyplot as plt
from .data import WORKS

def plot_timeline(figsize=(12, 8), savepath=None):
    """
    Plot a horizontal timeline of publication years for all works.
    """
    titles = [w["title"] for w in WORKS]
    years  = [w["year"]  for w in WORKS]

    y_pos = list(range(len(WORKS)))
    plt.figure(figsize=figsize)
    plt.hlines(y=y_pos, xmin=0, xmax=years, color="gray", alpha=0.5)
    plt.scatter(years, y_pos, color="navy", s=50)
    plt.yticks(y_pos, titles)
    plt.xlabel("Year (BCE negative; CE positive)")
    plt.title("Timeline of Publication Dates")
    plt.grid(axis="x", linestyle="--", alpha=0.3)
    plt.tight_layout()
    if savepath:
        plt.savefig(savepath)
    plt.show()
