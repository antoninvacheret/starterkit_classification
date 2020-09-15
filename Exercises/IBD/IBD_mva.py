import numpy as np
import matplotlib.pyplot as plt
import data_getters
import mpl_examples 
from matplotlib import cm


from sklearn import svm, preprocessing
from sklearn.metrics import roc_curve

#-------------------------------------------------------------------------------

def run():
    # Recall the available files.
    # f_name should be one of ['IBD_off_nonshifted.npy', 
    #                           'IBD_on_nonshifted.npy',
    #                           'IBD_sim_signal_nonshifted.npy',
    #                           'IBD_off_shifted.npy',
    #                           'IBD_on_shifted.npy']

    
    # Pop up all plots made at the end of the run.
    plt.show() 


#-------------------------------------------------------------------------------

run()