import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025))
            &(df['value'] <= df['value'].quantile(0.975))]

df.loc[:, ['year']] = df['date'].dt.year
df.loc[:, ['month']] = df['date'].dt.month


def draw_line_plot():
    # Draw line plot
    df.plot(x='date', y='value', kind='line', figsize=(32,10), color='red', fontsize=16, legend=False)
    plt.xlabel("Date", fontsize=20)
    plt.ylabel("Page Views", fontsize=20)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=20)





    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return plt

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.loc[:, ['year']] = df_bar['date'].dt.year
    df_bar.loc[:, ['month']] = df_bar['date'].dt.month
    df_bar = df_bar.groupby(['year', 'month']).agg({'value' : 'mean'})
    df_bar = df_bar.unstack()

    # Draw bar plot
    df_bar.plot.bar(legend=True, xlabel='Years', ylabel='Average Page Views', figsize=(10,7))
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September', 'October', 'November', 'December'])
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)

    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return plt

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()

    # Draw box plots (using Seaborn)
    sns.set_context('talk')
    sns.set_theme(palette='pastel')

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(28.80, 10.80))
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_ylabel('Page views')
    ax1.set_xlabel('Year')
    ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nove', 'Dec'])
    ax2.set_ylabel('Page views')
    ax2.set_xlabel('Month')
    ax2.set_title('Month-wise Box Plot (Seasonality)')



    sns.boxplot(ax=ax1, data=df_box, x='year', y='value')
    sns.boxplot(ax=ax2, data=df_box, x='month', y='value')

    plt.tight_layout()





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()

