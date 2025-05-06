import plotter
import clusterizer
import Scorer
import numpy as np
import clustbench as cb
from ScoreAggregator import ScoreAggregator

def comparison_for_battery(datasets,models,models_names):
    aggreg=ScoreAggregator(models_names)
    for dataset in datasets:
        res=comparison_for_dataset(dataset, models, models_names)
        aggreg.add_score(res)
    return aggreg.aggregate()

def comparison_for_dataset(dataset, models, models_names):
    b = cb.load_dataset("sipu", dataset, path="./clustering-data-v1")
    plotter.plot_ref(b, dataset, save=True)
    scores = {}
    results = {}
    N = len(models)
    if N != len(models_names):
        raise ValueError("Number of models and names must be the same")
    for model, name in zip(models, models_names):
        res = clusterizer.Clusterizer.evaluate_model(b, model, name)
        scores[name] = []
        results[name] = res
        for i in res.keys():
            li = np.argwhere(b.n_clusters == i)[0][0]
            scores[name].append(Scorer.Scorer.score_cluster(b.labels[li], res[i], name))
    agg = []
    for i in scores.keys():
        obj = (i, Scorer.Scorer.aggregate_stage(scores[i], i))
        agg.append(obj)
    agg.sort(key=lambda x: x[1], reverse=True)
    f="clusters/"+dataset+"a_results.txt"
    with open(f, "w") as o:
        for i in agg:
            o.write(str(i[0])+ " = "+str(i[1])+"\n")
    idx = [0, N - 1,N-2]
    for i in idx:
        plotter.plot_results(b, results[agg[i][0]], agg[i][0], dataset, save=True)
    return scores


