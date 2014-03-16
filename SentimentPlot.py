from __future__ import division

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def radial_jitter(val1, val2, scale=0.1):
    '''
    '''
    dr = scale * np.random.rand()
    dth = np.random.rand() * 2 * np.pi
    
    return val1 + dr * np.cos(dth), val2 + dr * np.sin(dth)

def sentiment_plotter(jitter_scores, songs):
    '''
    '''
    x = []
    y = []
    z = []
    
    for point,song in zip(jitter_scores,songs):
        xj, yj = point[0], point[1]
        
        x.append(xj)
        y.append(yj)
        z.append(song.year)

    data = zip(x,y,z)
    np.random.shuffle(data)
    x, y, z = list(zip(*data))
        
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, aspect='equal')
    
    ax.set_title("Sentiment Content for Songs")
    out = plt.scatter(x, y, s=5, c=z, cmap = cm.jet, edgecolors='none')   
    cbar = plt.colorbar(out)
    
    plt.savefig("sentiments_year_colormap.png", dpi=100)

def similarity_plotter(figure, sim_list, target_val):
    '''

    '''
    x = []
    y = []
    
    for each in sim_list:
        x.append(each[0])
        y.append(each[1])
    plt.scatter(x, y, s=1, c='k', marker='.')
    plt.scatter(target_val[0],target_val[1], s=8, c='0.2', marker='x')
    plt.scatter(target_val[0],target_val[1], s=100, c='0.7', marker='o',facecolor='none')
    plt.savefig("sentiment_cluster.png",dpi=500)
    plt.show()

