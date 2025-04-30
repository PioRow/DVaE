import matplotlib.pyplot as plt
import genieclust as gini
import numpy as np
import clustbench as cb
from Scorer import Scorer


def plot_results(b, r, name, ds,plot=False, save=False):
    plt.figure(figsize=(16, 10))
    plt_len=len(r.keys())
    for j, i in enumerate(r.keys()):
        plt.subplot(1,plt_len , j + 1)
        plt.title(ds + " " + name + " " + str(i))

        gini.plots.plot_scatter(b.data, labels=r[i])
        lbl_idx = np.argwhere(b.n_clusters == i)[0][0]
        score = Scorer.score_cluster(b.labels[lbl_idx], r[i], name)
        score = "score: " + str(round(score, 3))
        plt.text(0.01, 0.99, s=score, ha='left', va='top', transform=plt.gca().transAxes, c="#AA00AA")
        if plot:
            plt.plot()
    if save:
        plt.savefig("clusters/" + ds + "_" + name + ".png")

def plot_ref(b,ds,plot=False,save=False):
    plt.figure(figsize=(16, 10))
    plt_len=len(b.labels)
    for i in range(plt_len):
        plt.subplot(1, plt_len,i+1)
        labels=b.labels[plt_len-i-1]
        uniq=len(np.unique(labels))
        plt.title(ds + " " +str(uniq))
        gini.plots.plot_scatter(b.data, labels=labels)
        if plot:
            plt.plot()
    if save:
        plt.savefig("clusters/" + ds +".png")

