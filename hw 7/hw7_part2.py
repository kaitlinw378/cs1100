#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:23:56 2019

This movie outputs types of movies based on specifications from user inputs
such as genres and years and weight values. It then outputs the highest and 
lowest.

@author: kaitlin
"""

import json

def genre(genresfact):
    genre = input('What genre do you want to see? ') 
    print(genre)
    for genre in genresfact: 
        if genre.lower() == genre.lower():
            return True 
        elif genre.lower() == 'stop':
            return False
    return genre
'''
Function genre takes input and returns true if the user puts a valid genre.
'''

def bestmovies(avgdic):
    for (key, value) in avgdic.items():
        sortedavgl = sorted((value, key))
        
    #sortedavgl = sorted((value,key) for (key, value) in avgdic.items())
    bestmovie = sortedavgl[len(sortedavgl)-1][1] 
    bestrate = sortedavgl[len(sortedavgl)-1][0]
    bestformat = '{:2f}'.format(bestrate)
    return bestformat, bestmovie
'''
Function bestmovies formats and calculates the values for the best movies
'''
    
def worstmovies(avgdic):
    for (key, value) in avgdic.items():
        sortedavgl = sorted((value, key))
        
    #worstmovie = sortedavgl[0][1]
    worstrate = sortedavgl[0][0]
    worstformat = '{:2f}'.format(worstrate)
    return worstformat
'''
Function worstmovies formats and calulates the values for the worst movies. 
'''

if __name__ == '__main__':    
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    
    minyear = input('Min year => ') 
    print(minyear) 
    
    maxyear = input('Max year => ')
    print(maxyear) 
    
    imdb = input('Weight for IMDB => ')
    print(imdb) 
    imdb = float(imdb)
    
    twitter = input('Weight for Twitter => ')
    print(twitter) 
    twitter = float(twitter) 

    while True:  
        movieyears = dict() 
        average = dict() 
        genres = dict() 
        
        for movie in movies: 
           if int(movies[movie]['movie_year'])  <= int(minyear) and int(movies[movie]['movie_year']) <= int(maxyear): 
               movieyears[movie] = (movies[movie]['movie_year'], movies[movie]['genre'])
           else:
               continue
        
        ratings = movies[movie]['rating']
               
        for g in genres: 
            if genre.lower() == genre.lower():             
                genres[movie] = movies[movie]['movie_year']
        
        average = sum(ratings)/len(ratings)
        if movie not in ratings:
            continue
        else: 
            if len(ratings[movie] < 3):
                continue
            elif movie in genres: 
                total = (imdb * ratings + twitter * average) / (imdb + twitter) 
                average[movie] = total
        
        if len(average) == 0:
            print('No {} movie found in {} through {}'.format(genre().title(), minyear, maxyear))
        
        else: 
            bestmovies(average) 
            print('Best:')
            print('Released in {}, {} has a rating of {}'.format(bestmovies, bestmovies[1], ratings))
                  
            worstmovies(average)
            print('Worst:')
            print('Released in {}, {} has a rating of {}'.format(worstmovies, worstmovies[1], ratings))
           