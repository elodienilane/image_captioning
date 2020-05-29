# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:17:19 2020

@author: ElodieNilane
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import codecs, json, os

# Constants for file names
prefix = 'train'
json_file_name = prefix + ".json"
train_dataset_file_name = prefix + '_translated_new.txt'
translated_file_name = prefix + '_translated_.txt'
train_ja_path = prefix + '_new.json'

# Importing the dataset
translated_comments = pd.read_table(train_dataset_file_name, names=['comment'])
orig_file = pd.read_json(json_file_name)


#Parse file to save only text to translate
def translate_file(json_file_path, comments_file_path, dest_file_path):
  data = ""
  characters_read = 0
  number_of_chunks = 0
  j = 0
  total = 0
  #dest = open(json_file_path, "w+")

  with codecs.open(json_file_path, 'r', 'utf8') as comments_file:    
      data = json.load(comments_file)
      for json_object in data:
        for key in json_object:
          if key=="comment":
            json_object[key] = translated_comments.iloc[total, 0]
            total = total + 1
        j+=1
      print(total)

      #os.remove(json_file_path)
      with codecs.open(dest_file_path, 'w', 'utf8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

translate_file(json_file_name, train_dataset_file_name, train_ja_path)