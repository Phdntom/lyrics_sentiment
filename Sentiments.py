from __future__ import division, print_function

def get_scores(fname):
    '''
    Parameters
    ----------
    fname:      filename str to a valid word, score file, tab separated

    Returns
    -------
    scores:     dict: word --> int; sentiment score on [-5,5], no zeros
    
    '''
    scores = {}
    with open(fname, 'r') as fobj:
        for line in fobj:
            word, val = line.split('\t')
            scores[word] = int(val)
            
    return scores

def score_a_song(scores, song):
    '''
    '''
    lyrics = song.lyrics.split()
    pos_word_count = 0
    neg_word_count = 0
    pos_score = 0
    neg_score = 0
    for word in lyrics:
        if word in scores:
            score_val = scores[word]
            if score_val > 0:
                pos_score += score_val
                pos_word_count += 1
            else:
                neg_score += score_val
                neg_word_count += 1
    if pos_word_count > 0:
        pos_score /= pos_word_count
    if neg_word_count > 0:
        neg_score /= neg_word_count
        
    return (pos_score, abs(neg_score))

def score_songs(scores, songs):
    '''
    Parameters
    ----------
    scores:     dict of word --> sentiment scores
    songs:      list of Song objects

    Returns
    -------
    song_scores: list of 2-tuple of (pos_score, neg_score)

    Notes
    -----
    2-tuples generated in this way lie in the 1st quadrant with the maximum
    in the domain matching the maximum/min score in scores dictionary for each
    axis. i.e.
        pos_score is on [0,max(scores)]
        neg_score is on [0,abs(min(scores))]
    '''
    song_scores = []
    for song in songs:
        song_scores.append(score_a_song(scores, song))
    
    return song_scores

if __name__ == "__main__":
    pass
    # test
