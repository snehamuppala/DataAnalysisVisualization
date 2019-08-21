#!/usr/bin/env python
"""mapper.py"""
import sys

topwords = ['hitter', 'game','first','player','baseball','league','season','hit','one','team']
#input comes from STDIN (standard input)
for article in sys.stdin:
    #words = article.split('\n')
    for topword in topwords:
        if topword in article:
            article = article.strip()
            eachWords = article.split(" ")
            for eachWord in eachWords:
                if eachWord != topword:
                    if eachWord > topword:
                        string = topword + ',' + eachWord
                    else:
                        string = eachWord + ',' + topword
                    print '%s\t%s' % (string, 1)
