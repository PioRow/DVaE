import numpy as np


class dataGenerator:
    def __init__(self,n_samples=300):
        self.n_samples = n_samples
        self.X = None
        self.n_rel = None
        self.y = np.random.binomial(1, 0.5, n_samples)

    def generate_relevant(self,m1,m2,s1,s2,n_r):
        self.n_rel=n_r
        self.X=np.zeros((self.n_samples, n_r))
        for i,r in enumerate(self.y):
            if r==1:
                self.X[i]=np.random.normal(m1, s1, n_r)
            else:
                self.X[i]=np.random.normal(m2, s2, n_r)

        return self
    def generate_irrelevant(self,lamb_max,n_i):
        irr=np.zeros((self.n_samples, n_i))
        for i in range(n_i):
            lamb=np.random.uniform(0, lamb_max)
            irr[:,i]=np.random.exponential(lamb, self.n_samples)
        self.X=np.concatenate((self.X, irr), axis=1)
        return self

    def generate_correlated(self, n_c):
        corr=np.zeros((self.n_samples, n_c))
        for i in range(n_c):
            size=np.random.randint(1, self.n_rel)
            idxs=np.random.choice(self.n_rel,size, replace=False)
            coef=self._get_coef(size)
            noise=0
            if np.random.uniform(0, 1) > 0.2:
                noise=np.random.normal(0,1)
            corr[:,i]=np.dot(self.X[:,idxs], coef)+noise
        self.X=np.concatenate((self.X, corr), axis=1)
        return self
    def _get_coef(self, size):
        coef = np.zeros(size)
        limit=1
        for i in range(size):
            if i!=size-1:
                coef[i]=np.random.uniform(0, limit)
                limit-=coef[i]
        else:
            coef[i]=limit
        return coef

    def generate_redundant(self,n_red):
        red=np.zeros((self.n_samples, n_red))
        for i in range(n_red):
            size=np.random.randint(1, self.n_rel)
            idxs=np.random.choice(self.n_rel,size, replace=True)
            red[:,i]=np.prod(self.X[:,idxs], axis=1)
        self.X=np.concatenate((self.X, red), axis=1)
        return self
    def build(self):
        return self.X, self.y