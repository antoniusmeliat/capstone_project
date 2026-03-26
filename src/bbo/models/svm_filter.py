
from sklearn.svm import SVC
import numpy as np

def svm_filter(X,Y,cfg):
    labels = Y>np.quantile(Y,cfg.svm_high_quantile)
    clf=SVC(C=cfg.svm_C,kernel=cfg.svm_kernel,gamma=cfg.svm_gamma)
    clf.fit(X,labels)
    scores=clf.decision_function(X)
    keep=int(len(X)*cfg.svm_keep_frac)
    idx=np.argsort(scores)[-keep:]
    return X[idx]
