import numpy as np
import featureSelectionMethods as fs
import sklearn.feature_selection as skfs
from  sklearn.decomposition import PCA


class featureExtractor:
    def __init__(self,rel):

        self.rel = rel
        self.ext=fs.featureSelector(n=len(rel))
        self.pca=PCA(n_components=len(rel))
        self.idxs={}
    def all_features(self,X,y,train):
        return X, y

    def relevant_features(self,X,y,train):

        return X[:,self.rel],y

    def ANOVA_filter(self,X,y,train):
        if train:
            self.idxs['Anova']=self.ext.ANOVA_filter(X,y)
            return X[:,self.idxs['Anova']], y
        else:
            return X[:,self.idxs['Anova']], y
    def mutual_info_filter(self,X,y,train):
        if train:
            self.idxs['Mutual']=self.ext.mutual_info_filter(X,y)
            return X[:,self.idxs['Mutual']], y
        else:
            return X[:,self.idxs['Mutual']], y
    def SVM_wrapper(self,X,y,train):
        if train:
            self.idxs['SVM']=self.ext.SVM_wrapper(X,y)
            return X[:,self.idxs['SVM']], y
        else:
            return X[:,self.idxs['SVM']], y

    def Logistic_wrapper(self,X,y,train):
        if train:
            self.idxs['Logistic']=self.ext.Logistic_wrapper(X,y)
            return X[:,self.idxs['Logistic']], y
        else:
            return X[:,self.idxs['Logistic']], y
    def PCA_projection(self,X,y,train):
        if train:
            self.pca.fit(X)
            self.idxs['PCA']=self.pca.transform(X)
            return self.idxs['PCA'], y
        else:
            return self.pca.transform(X), y
