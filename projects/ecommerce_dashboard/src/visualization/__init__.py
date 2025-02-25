# src/visualization/__init__.py
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

def plot_time_series(df, x_column, y_column, title, xlabel, ylabel, figsize=(12, 6)):
    """
    Tworzy wykres szeregu czasowego.
    """
    plt.figure(figsize=figsize)
    plt.plot(df[x_column], df[y_column], marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return plt

def plot_category_distribution(df, category_column, count_column, title, xlabel, ylabel, figsize=(12, 6), top_n=10):
    """
    Tworzy wykres słupkowy dla rozkładu kategorii.
    """
    top_categories = df.sort_values(count_column, ascending=False).head(top_n)
    
    plt.figure(figsize=figsize)
    sns.barplot(x=category_column, y=count_column, data=top_categories)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return plt

def create_brazil_map(df, state_column, value_column, title):
    """
    Tworzy mapę Brazylii z wartościami według stanów.
    """
    fig = px.choropleth(
        df,
        locations=state_column,
        color=value_column,
        scope="south america",
        title=title,
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='natural earth'
        )
    )
    
    return fig