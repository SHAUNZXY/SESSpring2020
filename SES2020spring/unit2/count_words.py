# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:50:52 2020

@author: zouxiaoyang

This homework2 for SES2020spring
"""
import os
def count_word(path):
    with open(path,'r') as f:
        lines = f.readlines()
        words_num = 0
        for line in lines:
            if line == '\n':
                continue
            else:
                for symbol in ['\n','#',' ']:
                    line = line.strip(symbol)
                words = line.split(' ')
                words_num += len(words)
    return words_num

fn = "readme.md"
if os.path.isfile(fn):
    words_num = count_word(fn)
    print('There are {} words in file {}.'.format(words_num,fn))
else:
    print('The file does not exist.')

 


    
