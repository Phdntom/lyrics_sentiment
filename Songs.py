from __future__ import division, print_function
import sqlite3

class Song():
    '''
    '''
    
    def __init__(self, year, title, artist, lyrics, genre, rank):
        '''
        '''
        self.year = year
        self.lyrics = lyrics
        self.title = title
        self.artist = artist
        self.genre = genre
        self.rank = rank

def get_songs(dbname):
    '''
    Paremeters
    ----------
    dbname:   filename str to a valid sqlite3 database 
                SCHEMA: list, rank(of 100), title, artist, genre, lyrics

    Returns
    -------
    songs:    list of Song objects
    '''
    db = sqlite3.connect(dbname)
    c = db.cursor()
    
    songs = []
    for row in c.execute('SELECT * FROM rankings;'):
        lyric_field = row[6]
        # print( row[0])
        if lyric_field is not None:
            if 'all' in row[0]:
                continue
                #year = 2025
            else:
                year = int(row[0])
            rank = row[1]
            title = row[2]
            artist = row[3]
            genre = row[5]
            lyrics = row[6]
            songs.append( Song(year, title, artist, lyrics, genre, rank) )
    print("{0} songs found.".format(len(songs)))
    return songs


if __name__ == "__main__":
    pass
    # some quick tests

