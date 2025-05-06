import numpy as np
import importlib
import matplotlib.pyplot as plt
import sklearn.decomposition as decomposition
import sklearn.ensemble as ensemble
import sklearn.svm as svm
import sklearn.ensemble as ens
import dataGenerator
import utils as u
import featureSelectionMethods as fs
import metricEvaluator as mev
importlib.reload(fs)
importlib.reload(u)
importlib.reload(dataGenerator)

import json
import featureExtractor as fe
import sklearn.metrics as metrics
import sklearn.model_selection as ms



def cross_validate_models(fun, fun_name, rel):
    fs_methods = ["all_features", "relevant_features", "ANOVA_filter", "mutual_info_filter", "SVM_wrapper",
                  "Logistic_wrapper", "PCA_projection"]

    SVM_d = {}
    R_d = {}
    for fs_method in fs_methods:
        SVM_d[fs_method] = []
        R_d[fs_method] = []
    for i in range(5):
        X, Y = u.direct_build_32()
        folder = ms.KFold(n_splits=10, shuffle=True, random_state=i)
        for k, (train, test) in enumerate(folder.split(X)):
            print("iteration",i,"fold",k)
            X_train, X_test = X[train], X[test]
            Y_train, Y_test = Y[train], Y[test]
            for fs_method in fs_methods:
                ext = fe.featureExtractor(rel)
                x_train, y_train = getattr(ext, fs_method)(X_train, Y_train, True)
                x_test, y_test = getattr(ext, fs_method)(X_test, Y_test, False)
                svm_pred = svm.SVC(kernel="linear").fit(x_train, y_train).predict(x_test)
                rf_pred = ensemble.RandomForestClassifier().fit(x_train, y_train).predict(x_test)
                SVM_d[fs_method].append(fun(y_test, svm_pred))
                R_d[fs_method].append(fun(y_test, rf_pred))
    return SVM_d, R_d

def main():
    funs = [metrics.accuracy_score, metrics.f1_score
        , metrics.recall_score, metrics.precision_score]
    metrics_names = ["accuracy", "F1", "recall", "precision"]
    for fun, name in zip(funs, metrics_names):
        a, b = cross_validate_models(fun, name, np.arange(8))
        print(name)
        with open("model_data/" + name + "_SVM.json", "w") as f:
            json.dump(a, f)
        with open("model_data/" + name + "_RF.json", "w") as f:
            json.dump(b, f)
main()