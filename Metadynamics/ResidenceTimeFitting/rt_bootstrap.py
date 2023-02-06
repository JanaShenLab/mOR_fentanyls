
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import pandas as pd
import random
from scipy.stats import ks_2samp, kstest
from statsmodels.distributions.empirical_distribution import ECDF
from sklearn.utils import resample
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
from scipy.stats import (norm,gamma,sem)
from scipy import stats
from matplotlib.ticker import MultipleLocator
from matplotlib import rcParams
import matplotlib
rcParams['font.family'] ='sans'
rcParams['axes.spines.top'] = 'False'
rcParams['axes.spines.right'] = 'False'
rcParams['axes.titlepad'] = '15'
matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)

def func(x,tau):
    return 1-np.exp(-x/tau)


DATA = np.loadtxt('dissociation_realtimes.dat')

mean = []
P = []
for i in range(10000):
    x = np.random.choice(DATA,size=15,replace=True)
    ecdf = ECDF(x)
    x1 = np.logspace(-4,6,200)
    y1 = ecdf(x1)
    popt,pcov = curve_fit(func,x1,y1)
    tau1=popt[0]
    x2 = np.random.exponential(tau1,10000)
    st,p = ks_2samp(x,x2)
    mean.append(tau1)
    P.append(p)

COM = pd.concat([pd.DataFrame(P,columns=['P']),pd.DataFrame(mean,columns=['Tau'])],axis=1)
COM = COM.drop(COM[COM['P']<0.05].index)
COM = COM[['P','Tau']]
print('Number of successful bootstrapping trials (P-value >= 0.05): ', len(COM))
print('Calculated average residence times (sec): ', np.round(np.mean(COM['Tau']),2))
print('Average P-value from the successful trials: ', np.round(np.mean(COM['P']),3))

