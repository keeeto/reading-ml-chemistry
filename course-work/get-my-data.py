import pandas as pd
import numpy as np
import random
from os.path import exists

NUM_OUTLIERS = 3
OUTLIER_VALUE = 1e5
NUM_DUPS = 2
newnames = ['LUMO values', 'Periodic nature']
#wget the data
orig_data = pd.read_csv('base-data.csv')

if exists('coursework-data.csv'):
    print('File already exists no more to see here.')
else:
    change = orig_data.sample(NUM_OUTLIERS).index
    cols = random.sample(range(0, 12), NUM_OUTLIERS)
    for j, i in enumerate(change):
        n = cols[j]
        name = orig_data.columns[n]
        orig_data.loc[i, name] = OUTLIER_VALUE

## Duplicate two random columns
    names = orig_data.columns
    
    for i in range(NUM_DUPS):
        index = np.random.randint(0, len(names)-1)
        n = names[index]
        orig_data[newnames[i]] = orig_data.loc[:, n]

    orig_data = orig_data.sample(frac=1, axis=1)

## This is for my data to clean up the names
    orig_data = orig_data.rename(columns={'MagpieData avg_dev Number' : 'Number dev',  'MagpieData avg_dev AtomicWeight' : 'Weight dev', 'MagpieData mean NValence' : 'NValence mean', 'MagpieData avg_dev MeltingT': 'MeltT dev', 'MagpieData mean MeltingT': 'MeltT mean', 'MagpieData avg_dev CovalentRadius': 'CovRad dev', 'MagpieData avg_dev SpaceGroupNumber': 'Spg dev','MagpieData avg_dev GSvolume_pa': 'GS dev', 'MagpieData mean GSvolume_pa': 'GS mean', 'MagpieData avg_dev NdValence': 'NdValence dev', 'MagpieData avg_dev MendeleevNumber': 'Mendeleev dev', 'MagpieData avg_dev Electronegativity': 'Eneg dev'})

    orig_data.to_csv('coursework-data.csv', index=False)
