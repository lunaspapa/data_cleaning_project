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

# Months object to convert Year to Integer

month_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}

dataframes[0].head()

print(CSV)
