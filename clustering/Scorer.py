import clustbench as cb
import sklearn
import genieclust as gini

class Scorer:

    @staticmethod
    def score_cluster(lb,r,model_name):
        print(model_name)
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
        return cb.get_score(lb,r)