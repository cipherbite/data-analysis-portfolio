# src/data/__init__.py
import pandas as pd
import os

def load_raw_data(data_path='../../data/raw/brazilian-ecommerce/'):
    """
    Wczytuje surowe dane z plików CSV.
    """
    files = os.listdir(data_path)
    data_dict = {}
    
    for file in files:
        if file.endswith('.csv'):
            file_name = file.split('.')[0]
            data_dict[file_name] = pd.read_csv(f"{data_path}{file}")
    
    return data_dict

def load_processed_data(data_path='../../data/processed/'):
    """
    Wczytuje przetworzone dane z plików CSV.
    """
    files = os.listdir(data_path)
    data_dict = {}
    
    for file in files:
        if file.endswith('.csv'):
            file_name = file.split('.')[0]
            data_dict[file_name] = pd.read_csv(f"{data_path}{file}")
    
    return data_dict