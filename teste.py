import pandas as pd
import numpy as np
import csv
import json
import re

nos = pd.read_csv('./csv/nodes.csv')
arestas = pd.read_csv('./csv/edges.csv')

print(nos.head())

print(arestas.head())
