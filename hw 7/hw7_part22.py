#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:10:13 2019

@author: kaitlin
"""
import json

if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    
    minyear = input('Min year  => ') 
    print(minyear) 
    
    maxyear = input('Max year => ')
    print(maxyear) 
    
    imdb = input('Weight for IMDB => ')
    print(imdb) 
    imdb = float(imdb)
    
    twitter = input('Weight for Twitter => ')
    print(twitter) 
    twitter = float(twitter) 
    #stop = False
    
    while True:
        genreinput = input('what genre do you want to see? ') 
        print(genreinput)
        genreinput = genreinput.lower() 
        if genreinput == 'stop':
            stop = True
            break 
        
        moveinyeardic = {}
        avgdic = {} 
        genredic = {} 
        
        for movie in movies: 
            if int(movies[movie]['movie_year']) >= int(minyear) and int(movies[movie]['movie_year'] <= int(maxyear)):
                moveinyeardic[movie] = (movies[movie]['movie_year'], movies[movie]['genre'])
            else:
                continue
            
            imdbrating = movies[movie]['rating'] 
            correctgenre = False
            
            genrelist = moveinyeardic[movie][1]
            for genre in genrelist:
                if genreinput.lower() == genre.lower():
                    correctgenre = True 
                    genredic[movie] = movies[movie]['movie_year']
            
            if movie not in ratings:
                continue
            else:
                if len(ratings[movie]) < 3:
                    continue
                elif movie in genredic:
                    avgtrate = sum(ratings[movie])/len(ratings[movie])
                    total = (imdb * imdbrating + twitter * avgtrate) / (imdb + twitter) 
                    avgdic[movie] = total 
        
        if len(avgdic) == 0:
            print() 
            print(f'No {genreinput.title()} movie found in {minyear} through {maxyear}')
            print() 
            
        else: 
            sortedavgl = sorted((value,key) for (key, value) in avgdic.items())
            bestmovie = sortedavgl[len(sortedavgl)-1][1] 
            bestrate = sortedavgl[len(sortedavgl)-1][0]
            bestformat = '{:2f}'.format(bestrate)
            print()
            print('Best:')
            print(f'\tReleasted in {movies[bestmovie]["movie_year"]}, {movies[bestmovie]["name"]} has a rating of {movies[bestmovie]["rating"]}')
            print() 
            
            worstmovie = sortedavgl[0][1]
            worstrate = sortedavgl[0][0]
            worstformat = '{:2f}'.format(worstrate)
            print('Worst:')
            print(f'\tReleasted in {movies[worstmovie]["movie_year"]}, {movies[worstmovie]["name"]} has a rating of {movies[worstmovie]["rating"]}')
            print() 
    
    