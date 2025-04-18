import numpy as np
import sklearn.feature_selection as fs
import sklearn.svm as svm

class featureSelector:

    def __init__(self,tol=1,n=None):
        self.tol=tol
        self.n=n

    def ANOVA_filter(self,X,y):
        if self.n is None:
            n=X.shape[1]
        else:
            n=self.n
        f_sc,p=fs.f_classif(X, y)
        p.filter(p<self.tol).argsort

    def mutual_info_filter(self,X,y):
        if self.n is None:
            n=X.shape[1]
        else:
            n=self.n
        chi2_sc,p=fs.chi2(X, y)