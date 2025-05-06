import clustbench as cb
import sklearn
import genieclust as gini
import numpy as np
class Scorer:

    @staticmethod
    def score_cluster(lb,r,model_name):
        if model_name=="DBSCAN":
            return Scorer._score_db(lb,r)
        else:
            return Scorer._score(lb,r)

    @staticmethod
    def _score_db(lb,r):
        a=gini.compare_partitions.normalized_clustering_accuracy(lb,r)
        return gini.compare_partitions.normalized_clustering_accuracy(lb,r)
    @staticmethod
    def _score(lb,r):
        return float(cb.get_score(lb,r))
    @staticmethod
    def _aggregate_reg_db(score,name):
        return np.max(score)
    @staticmethod
    def _aggregate_reg(score,name):
        return np.mean(score)
    @staticmethod
    def aggregate_stage(score,name):

        if name=="DBSCAN":
            return Scorer._aggregate_reg_db(score,name)
        else:
            return Scorer._aggregate_reg(score,name)
