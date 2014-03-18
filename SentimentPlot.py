from __future__ import division

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from collections import defaultdict

def radial_jitter(val1, val2, scale=0.1):
    '''
    '''
    dr = scale * np.random.rand()
    dth = np.random.rand() * 2 * np.pi
    
    return val1 + dr * np.cos(dth), val2 + dr * np.sin(dth)

def colormap_plotter(song_scores, songs, sim_list=None, target_val=None, jitter=True):
    '''
    '''
    x = []
    y = []
    z = []

    scale = 0.1
    # radial jitter helps "unstack" identical scores
    plot_scores = []
    if jitter:
        outname = "contour_jittered_map.png"
        for point, song in zip(song_scores, songs):
            plot_scores.append(radial_jitter(point[0], point[1], scale))
    else:
        outname = "contour_map.png"
        for point, song in zip(song_scores, songs):
            plot_scores.append( (point[0], point[1]) )

    for point, song in zip(plot_scores, songs):
        x.append(point[0])
        y.append(point[1])
        z.append(song.year)

    # zip and shuffle points so order doesn't skew interpretation
    data = zip(x, y, z)
    np.random.shuffle(data)
    x, y, z = list(zip(*data))
    x_max, x_min = max(x), min(x)
    y_max, y_min = max(y), min(y)

    # make the figure, labels etc
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, aspect='equal')

    ax.set_xlabel("Positive Sentiment Strength")
    ax.set_ylabel("Negative Sentiment Strength")

    ax.set_xlim(x_min - scale,x_max)
    ax.set_ylim(y_min - scale,y_max)

    image = plt.scatter(x, y, s=8, c=z, cmap=cm.jet, edgecolors='none')

    # check for optional arguments
    if sim_list is not None and target_val is not None:
        outname = "cluster_contour_map.png"
        xC = []
        yC = []
    
        for each in sim_list:
            xC.append(each[0])
            yC.append(each[1])
        # add a target and cluster
        plt.scatter(xC, yC, s=1, c='k', marker='.')
        plt.scatter(target_val[0],target_val[1], s=8, c='0.2', marker='x')
        plt.scatter(target_val[0],target_val[1], s=100, c='0.7', marker='o',facecolor='none')

    # do some matplotlib hacking to align the colormap bar
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = plt.colorbar(image,cax=cax)

    # save it
    plt.savefig(outname, dpi=500)
    # show it
    plt.show()

    return plot_scores

def scatter_plotter(song_scores, songs):

    y1_dict = defaultdict(list)
    y2_dict = defaultdict(list)
    for point, song in zip(song_scores, songs):
        key = int(song.year)
        y1_dict[key].append(point[0])
        y2_dict[key].append(point[1])

    x = []
    y1 = []
    y2 = []
    for key in y1_dict:
        x.append(key)
        y1.append(np.mean(y1_dict[key]))
        y2.append(np.mean(y2_dict[key]))

    #print(y1_dict)

    data = zip(x, y1, y2)
    data.sort(key=lambda t: t[0])
    x, y1, y2 = list(zip(*data))

    fig, ax = plt.subplots()

    ax.set_xlabel("Year")
    ax.set_ylabel("Mean Sentiment Strength")

    ax.scatter(x, y1, color='k', label='Positive Sentiment')
    ax.scatter(x, y2, color='b', label='Negative Sentiment')

    legend = ax.legend(loc='lower right', shadow=True)
    
    plt.savefig("scatter_plot.png", dpi=500)
    plt.show()

if __name__ == "__main__":
    pass
    # some tests



