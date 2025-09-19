import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Ler os dados os dados do arquivo CVS
    df = pd.read_csv('epa-sea-level.csv')

    # scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lr_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = np.arange(df['Year'].min(), 2051)   # e.g. 1880..2050 inclusive
    y_all = lr_all.intercept + lr_all.slope * x_all
    plt.plot(x_all, y_all, label='Fit: 1880-2014')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    lr_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = np.arange(2000, 2051)  # 2000..2050 inclusive
    y_recent = lr_recent.intercept + lr_recent.slope * x_recent
    plt.plot(x_recent, y_recent, label='Fit: 2000-2014')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()