# Imports
import numpy as np
from datetime import datetime
import glob
import json
import os
import matplotlib.pyplot as plt
from matplotlib import cm
import pickle
import pandas
import re
import seaborn as sns
import six

sns.set()
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
pandas.options.mode.chained_assignment = None

CSV = [i for i in glob.glob('*.{}'.format('csv'))]

# Reading CSV
dataframes = [] # list to store each frame
for csv in CSV:
  df = pandas.read_csv(csv)
  dataframes.append(df)

dataframes[0].head()

for df in dataframes:
  df['show_id'] = pandas.Series(df['show_id'], dtype="string")

  df['date_added'] = df['date_added'].astype('str')
  date_pieces = (df['date_added'].str.split(' '))

  # df['Year'] = date_pieces.str[3].astype(int)
  # df['Day'] = date_pieces.str[1].astype(int)
  # df['Month'] = date_pieces.str[0].astype(int)
