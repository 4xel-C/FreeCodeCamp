import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], s=5)

    # Create first line of best fit
    x_pred = pd.Series([i for i in range(1880,2051)])
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    y_pred = intercept + (slope * x_pred)
    plt.plot(x_pred, y_pred, color='red')

    # Create second line of best fit
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df.loc[df['Year'] >= 2000,'Year'], df.loc[df['Year'] >= 2000,'CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series([i for i in range(2000,2051)])
    y_pred2 = intercept2 + (slope2 * x_pred2)
    plt.plot(x_pred2, y_pred2, color='green')
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()