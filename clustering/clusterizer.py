import clustbench as cb
import numpy as np
import sklearn
class Clusterizer:

    @staticmethod
    def evaluate_model(b,model,model_name):
        if model_name=="DBSCAN":
            return Clusterizer._eval_db(b, model)
        else:
            return Clusterizer._eval(b, model)

    @staticmethod
    def _eval_db( b, model):
        res={}
        X=b.data
        min_samples=int(X.shape[0]*0.01)
        dist=sklearn.metrics.pairwise_distances(X).flatten()
        dist=dist[np.where(dist>0)]
        eps=np.quantile(dist,q=0.1)

        mdl=model(eps=eps, min_samples=min_samples)

        y=mdl.fit_predict(X)+1
        for i in b.n_clusters:
            res[int(i)]=y
        return res
    @staticmethod
    def _eval(b,model):
        return cb.fit_predict_many(model, b.data, b.n_clusters)