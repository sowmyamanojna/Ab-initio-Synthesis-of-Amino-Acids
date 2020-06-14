import os
import csv
import numpy as np
import pandas as pd
import scipy.constants as sc

data = pd.read_csv('data.csv')
data = data.T.reset_index().T
data = data.rename(columns={1:})