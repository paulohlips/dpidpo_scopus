import os
import glob
import pandas as pd

dfs = glob.glob('scopus/*.csv')

result = pd.concat([pd.read_csv(df)
                    for df in dfs], ignore_index=True, sort=True)

result.to_csv('scopus/merge.csv')
