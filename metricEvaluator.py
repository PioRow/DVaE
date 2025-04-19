import numpy as np

class metricEvaluator:
    def __init__(self, y_pred, y_true,all):
        self.y_true=set(y_true)
        self.y_pred=set(y_pred)
        self.all=set(all)

    def Bolon_Canedo(self):
        R_s=len(self.y_pred& self.y_true)
        R_t=len(self.y_true)
        I=self.all-self.y_true
        I_s=len(self.y_pred& I)
        I_t=len(I)
        alpha=min(1/2,R_t/I_t)
        return R_s/R_t+alpha*I_s/I_t
    def accuracy(self):
        TP=len(self.y_pred& self.y_true)
        N=self.all-self.y_true
        TN=len(N-self.y_pred)
        return (TP+TN)/len(self.all)

    def F1(self):
        TP=len(self.y_pred& self.y_true)
        FP=len(self.y_pred-self.y_true)
        PredN=self.all-self.y_pred
        FN=len(self.y_true& PredN)
        return 2*TP/(2*TP+FP+FN)
