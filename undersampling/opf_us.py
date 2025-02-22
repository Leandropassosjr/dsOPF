# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:14:53 2020

@author: DANILO
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:10:02 2020

@author: DANILO
"""
from undersampling.us import US
import numpy as np

class OpfUS(US):
    
    def variant(self, output, X, Y, majority_class, minority_class):
        #5st case: remove samples from majoritary class until balancing the dataset

        # find the number of samples to remove
        n_samples = len(output)
        n_samples_minority = len(output[output[:,1]==2])
        n_samples_to_remove = n_samples - (n_samples_minority*2)

        # sort samples from majority class by score
        output_majority= output[output[:,1]==majority_class]
        order = np.argsort(output_majority[:,2])
        output_majority_ordered = output_majority[order,:]

        # remove samples
        output_to_remove = output_majority_ordered[:n_samples_to_remove,:]
        X_train = np.delete(X, output_to_remove[:,0],0)
        y_train = np.delete(Y, output_to_remove[:,0])
        
        return X_train, y_train
        
    def fit_resample(self, X, y):
        output, majority_class, minority_class = self.run(X, y)
        X_res, y_res = self.variant(output, X, y, majority_class, minority_class)
        
        return X_res, y_res
