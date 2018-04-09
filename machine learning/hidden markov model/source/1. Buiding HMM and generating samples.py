# -*- coding:utf-8 -*-  
__author__ = 'conghuai'

import numpy as np
from hmmlearn import hmm

np.random.seed(42)
model = hmm.GaussianHMM(n_components=3, covariance_type='full')
model.startprob_ = np.array([0.6, 0.3, 0.1])
model.transmat_ = np.array([[0.7, 0.2, 0.1],
                           [0.3, 0.5, 0.2],
                           [0.3, 0.3, 0.4]])
model.means_ = np.array([[0.0, 0.0], [3.0, -3.0], [5.0, 10.0]])
model.covars_ = np.tile(np.identity(2), (3, 1, 1))
X, Z = model.sample(100)

remodel = hmm.GaussianHMM(n_components=3, covariance_type='full', n_iter=100)
remodel.fit(X)
Z2 = remodel.predict(X)
