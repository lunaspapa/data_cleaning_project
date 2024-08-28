# Imports
import numpy as np
import calendar
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

sns.set_theme()
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
pandas.options.mode.chained_assignment = None

CSV = [i for i in glob.glob('*.{}'.format('csv'))]

print(CSV)

# Reading CSV
dataframes = [] # list to store each frame
for csv in CSV:
  df = pandas.read_csv(csv, encoding="ISO-8859-1")
  dataframes.append(df)

print(dataframes)
