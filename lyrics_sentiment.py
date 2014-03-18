from __future__ import division, print_function
import numpy as np

import Songs as Songs
import Sentiments as Sentiments
from SentimentPlot import colormap_plotter, scatter_plotter
import SentimentsClustering as SentCluster


def main():
    dbname = 'rankings.sqlite3'
    # Load songs from the database
    songs = Songs.get_songs(dbname)
    n_samples = len(songs)
    
    # Load word sentiment scores from known hand scored list
    fname = "AFINN-111.txt"
    word_scores = Sentiments.load_word_scores(fname)

    # Calculate the score for each song using hte lyrics attribute   
    song_scores = Sentiments.score_songs(word_scores, songs)

    # Plot the test song score along with its N closest scores (X marks the spot)
    #similarity_plotter(figure, sim_list, test_score)
    plotted_scores = colormap_plotter(song_scores, songs, jitter=False)
    plotted_scores = colormap_plotter(song_scores, songs, jitter=True)

    test_song = songs[np.random.randint(n_samples)]
    test_score = Sentiments.tuple_score(word_scores, test_song)
    print("Test Song:{0}, Score=({01},{2}).".format(test_song.title, *test_score))

    idxs = SentCluster.NmostSimilar(test_song, 20, word_scores, songs, plotted_scores)
    sim_list = []
    for rank, idx in enumerate(idxs):
        print("#{0} {1}, Score={2}".format(rank+1, songs[idx].title, plotted_scores[idx]))
        sim_list.append(plotted_scores[idx])

    colormap_plotter(plotted_scores, songs, jitter=False, sim_list=sim_list, target_val=test_score)

    scatter_plotter(song_scores, songs)

if __name__ == "__main__":
    main()



