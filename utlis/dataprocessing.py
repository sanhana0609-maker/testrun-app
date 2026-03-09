import pandas as pd

import pandas as pd

path = r"D:\EMJ 2025-2027\quantitivie research\python workshop\CrimesOnWomenData - Copy.csv"
data = pd.read_csv(path, sep=None, engine='python', on_bad_lines='skip')

print(data.head())  
print(data.tail())

import streamlit as st


