# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:47:55 2023

@author: SNEHA MARTIN
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_netflix_revenue(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(df['Year'], df['US & Canada'], label='US & Canada', color="orange")
    plt.plot(df['Year'], df['EMEA'], label='EMEA', color="red")
    plt.plot(df['Year'], df['Latin America'], label='Latin America', color="blue")
    plt.plot(df['Year'], df['Asia-Pacific'], label='Asia-Pacific', color="green")

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Netflix revenue of different countries')
    plt.legend()

    plt.show()

# Call the function with the file path
plot_netflix_revenue('Netflix Revenue and Usage Statistics.csv')
