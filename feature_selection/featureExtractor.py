import numpy as np
import featureSelectionMethods as fs
import sklearn.feature_selection as skfs
from  sklearn.decomposition import PCA


class featureExtractor:
    def __init__(self,X,y,rel):
        self.X = X
        self.y = y
        self.rel = rel
        self.ext=fs.featureSelector(n=len(rel))

    def all_features(self):
        return self.X, self.y

    def relevant_features(self):

        return self.X[:,self.rel],self.y

    def ANOVA_filter(self):
        idx=self.ext.ANOVA_filter(self.X,self.y)
        return self.X[:,idx], self.y

    def mutual_info_filter(self):
        idx=self.ext.mutual_info_filter(self.X,self.y)
        return self.X[:,idx], self.y

    def SVM_wrapper(self):
        idx=self.ext.SVM_wrapper(self.X,self.y)
        return self.X[:,idx], self.y

    def Logistic_wrapper(self):
        idx=self.ext.Logistic_wrapper(self.X,self.y)
        return self.X[:,idx], self.y

    def PCA_projection(self):
        N=len(self.rel)
        pca=PCA(n_components=N)
        pca.fit(self.X)
        return pca.transform(self.X),self.y

