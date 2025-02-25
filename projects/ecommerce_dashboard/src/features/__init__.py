# src/features/__init__.py
import pandas as pd
import numpy as np

def add_date_features(df, date_column):
    """
    Dodaje cechy związane z datą do DataFrame.
    """
    df[f'{date_column}_year'] = df[date_column].dt.year
    df[f'{date_column}_month'] = df[date_column].dt.month
    df[f'{date_column}_day'] = df[date_column].dt.day
    df[f'{date_column}_dayofweek'] = df[date_column].dt.dayofweek
    df[f'{date_column}_hour'] = df[date_column].dt.hour
    df[f'{date_column}_yearmonth'] = df[date_column].dt.strftime('%Y-%m')
    
    return df

def create_rfm_features(df, customer_id_column, date_column, amount_column):
    """
    Tworzy cechy RFM (Recency, Frequency, Monetary)
    """
    # Data końcowa
    end_date = df[date_column].max()
    
    # Obliczanie metryk RFM
    rfm = df.groupby(customer_id_column).agg({
        date_column: lambda x: (end_date - x.max()).days,  # Recency
        'order_id': 'count',  # Frequency
        amount_column: 'sum'  # Monetary
    })
    
    # Zmiana nazw kolumn
    rfm.columns = ['recency_days', 'frequency', 'monetary']
    
    return rfm