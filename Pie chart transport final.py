# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:26:49 2023

@author: SNEHA MARTIN
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:33:47 2023

@author: SNEHA MARTIN
"""

import pandas as pd
import matplotlib.pyplot as plt

def Transportation(year):
        
        # Filter data for the year 1950
        year_1950 = df[df["Year"] == 1950]
        
        # Group by transportation modes and count occurrences
        counts_national_rail = year_1950['National Rail network '].values
        counts_london_underground = year_1950['London Underground'].values
        counts_first_generation_trams = year_1950['First Generation Trams '].values
        counts_trolley_buses = year_1950['Trolley buses'].values
        counts_local_bus = year_1950['Local bus services '].values
        
        # Convert counts to a 1D array
        values_1950_array = [
            counts_national_rail[0],
            counts_london_underground[0],
            counts_first_generation_trams[0],
            counts_trolley_buses[0],
            counts_local_bus[0]
            ]
        
        #second Pie
        
        # Filter data for the year 1950
        year_1960 = df[df["Year"] == 1960]
        
        # Group by transportation modes and count occurrences
        counts_national_rail = year_1960['National Rail network '].values
        counts_london_underground = year_1960['London Underground'].values
        counts_first_generation_trams = year_1960['First Generation Trams '].values
        counts_trolley_buses = year_1960['Trolley buses'].values
        counts_local_bus = year_1960['Local bus services '].values
        
        # Convert counts to a 1D array
        values_1960_array = [
            counts_national_rail[0],
            counts_london_underground[0],
            counts_first_generation_trams[0],
            counts_trolley_buses[0],
            counts_local_bus[0]
            ]
        
        plt.figure(figsize=(21, 10))
        plt.subplot(1,2,1)
        plt.pie(values_1950_array,labels=['National Rail', 'London Underground', 'First Gen. Trams', 'Trolley Buses', 'Local Bus'], autopct='%1.1f%%', startangle=140)
        plt.title('Distribution of Transportation Modes in 1950')
        plt.subplot(1,2,2)
        plt.pie(values_1960_array,labels=['National Rail', 'London Underground', 'First Gen. Trams', 'Trolley Buses', 'Local Bus'], autopct='%1.1f%%', startangle=140)
        plt.title('Distribution of Transportation Modes in 1960')
        plt.show()
        
year = 1950
df = pd.read_csv("public transportation.csv")
Transportation(year)
