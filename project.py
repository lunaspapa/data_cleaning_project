# Imports
import numpy as np
from datetime import datetime
import glob
import json
import os
import matplotlib.pyplot as plt
from matplotlib import cm
import pickle
import pandas as pd
import re
import seaborn as sns
import six

sns.set()
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.mode.chained_assignment = None

CSV = [i for i in glob.glob('*.{}'.format('csv'))]
