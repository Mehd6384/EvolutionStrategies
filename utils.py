import numpy as np 
import matplotlib.pyplot as plt 


def eval_rastrigin(pos): 

    a = 10
    n = 2
    return a*n + np.sum(pos**2 - a*np.cos(np.pi*2*pos), axis =1)  

def plot_rastrigin(ax, res, lim =5.): 

    a = 10 
    n = 2
    x = np.linspace(-lim,lim,res)
    X, Y = np.meshgrid(x,x)

    points = a*n + (np.square(X) - a*np.cos(np.pi*2*X)) + (np.square(Y) - a*np.cos(np.pi*2*Y))
    ax.matshow(points, cmap = 'autumn', extent = [-lim, lim, -lim, lim])
