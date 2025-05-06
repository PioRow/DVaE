import numpy as np
import pandas as pd


class ScoreAggregator:
    def __init__(self,models):
        self.scores={}
        for model in models:
            self.scores[model]=[]

    def add_score(self,scores):
        for model in self.scores.keys():
            if model=="DBSCAN":
                new_scores=[max(scores[model])]*len(scores[model])
                self.scores[model]+=new_scores
            else:
                self.scores[model]+=scores[model]
        return self
    def aggregate(self):
        return self.scores