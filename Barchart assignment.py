# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:57:51 2023

@author: SNEHA MARTIN
"""

import matplotlib.pyplot as plt
import pandas as pd
movies_data = pd.read_csv("Movies_data.csv")

title = movies_data['title'].astype(str)
popularity = movies_data['popularity'].astype(str)

plt.figure(figsize=(9,5))
df_sorted = movies_data.sort_values("popularity")
plt.bar(title, df_sorted)
plt.show()