import os

import numpy as np
import clustbench as cb
import pandas as pd
import sklearn.cluster as clst
import genieclust as gini
import matplotlib.pyplot as plt
import importlib
import plotter
import clusterizer
import Scorer
import comparer
datasets=['a1','a2','a3','aggregation','compound','d31','r15','flame','jain','pathbased','spiral','s1','s2','s3','s4','unbalance']
#special=["birch1","birch2"]
models=[clst.KMeans(),gini.Genie(gini_threshold=0.1),
gini.Genie(gini_threshold=0.3),gini.Genie(gini_threshold=0.5),gini.Genie(gini_threshold=0.7),gini.Genie(gini_threshold=0.9),
    clst.AgglomerativeClustering(linkage='single'),clst.AgglomerativeClustering(linkage='complete')
    ,clst.AgglomerativeClustering(linkage='average'),clst.AgglomerativeClustering(linkage='ward'),clst.DBSCAN]

models_names=['KMeans','Genie_01','Genie_03','Genie_05','Genie_07','Genie_09',
              'Agglomerative_Clustering_single','Agglomerative_Clustering_complete','Agglomerative_Clustering_average',
              'Agglomerative_Clustering_ward','DBSCAN']

import json
def main():

    res = comparer.comparison_for_battery(datasets, models, models_names)

    for k in res.keys():
        print(len(res[k]))
    with open(f"agg_data\\aggregated_results.json", "w") as fp:
        json.dump(res, fp)

main()