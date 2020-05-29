# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:42:33 2020

@author: ElodieNilane
"""

import json 
import pandas as pd

path_to_english_json = 'D:\\Documents\\IA\\ProjectTest\\ParlAI\\data\\personality_captions\\train.json'
path_to_de_trans = r"D:/Documents/IA/ProjectTest/ParlAI/data/personality_captions/German/train_translated_de_utf8.txt"

translated_comments = pd.read_table(path_to_de_trans, names=['comment'])
orig_comments = pd.read_table(r"D:/Documents/IA/ProjectTest/ParlAI/data/personality_captions/train_extract_utf8.txt", names=['comment'])

i = 0

print(translated_comments.iloc[184493, 0])

with open(path_to_english_json, 'r') as file:
     json_data = json.load(file)
     for item in json_data:
        for key in item:
          if key=="comment":
              #print(item[key] + ' ' + translated_comments.iloc[i, 0])
              current_comment = item[key]
              item[key] = translated_comments.iloc[i, 0]
        if i > 60000 and i < 62000:
            print("comment: " + current_comment)

        if current_comment.strip():
            i = i + 1
        #if i > 60000 and i < 62000:
        #    print("comment: " + current_comment)

print(i)
with open('D:\\Documents\\IA\\ProjectTest\\ParlAI\\data\\personality_captions\\new_file.json', 'w') as file:
    json.dump(json_data, file, indent=2)