
import Sentiments as Sentiments
import numpy as np

def NmostSimilar(target_song, N, word_scores, songs, song_scores):
    '''
    '''
    target_score = Sentiments.tuple_score(word_scores, target_song)
    pairwise_dists = []
    pairwise_src = []
    
    for comp_score in song_scores:
        x1 = target_score[0]
        y1 = target_score[1]
        x2 = comp_score[0]
        y2 = comp_score[1]
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
        pairwise_dists.append( dist )
        pairwise_src.append( (x1,y1,x2,y2) )
    
    lookups = np.argsort(pairwise_dists)[:N]
    # It's sorted ascended, give me first N
        
    return lookups

if __name__ == "__main__":

    # Do a small jitter for each score to prevent overlapping, but preserve
    # original song_scores
    jitter_scores = []
    for each in song_scores:
        jitter_scores.append(radial_jitter(each[0], each[1]) )

    # Choose a random test song, score it and then find similarly scored songs
    test_song = songs[np.random.randint(n_samples)]
    test_score = Sentiments.score_a_song(scores, test_song)
    print("Test Song:{0}, Score=({01},{2}).".format(test_song.title, *test_score))

    # Find the list indices of the most similar songs to test_song
    idxs = NmostSimilar(test_song, 30, scores, songs, jitter_scores)
    sim_list = []
    for rank, idx in enumerate(idxs):
        print("#{0} {1}, Score={2}".format(rank+1, songs[idx].title, jitter_scores[idx]))
        sim_list.append(jitter_scores[idx])
