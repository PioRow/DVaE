import numpy as np
import sklearn.feature_selection as fs
import sklearn.svm as svm

class featureSelector:

    def __init__(self,prc=0.9,n=None):
        self.prc = prc
        self.n=n

    def ANOVA_filter(self,X,y):
        score,p=fs.f_classif(X,y)
        if self.n is None:
            top = np.max(score)*self.prc
            return np.argwhere(score>top)
        else:
            return np.argsort(score)[::-1][:self.n]


    def mutual_info_filter(self,X,y):
        score = fs.mutual_info_classif(X, y)
        if self.n is None:
            top = np.max(score) * self.prc
            return np.argwhere(score > top)
        else:
            return np.argsort(score)[::-1][:self.n]

    def SVM_wrapper(self,X,y):
        print(123)
