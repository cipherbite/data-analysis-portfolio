# dashboard/app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# Dodajemy ścieżkę do modułów
sys.path.append(os.path.abspath('../'))

# Importujemy własne moduły
from src.data import load_processed_data
from src.visualization import create_brazil_map

# Konfiguracja strony
st.set_page_config(page_title="E-commerce Dashboard", page_icon="🛍️", layout="wide")

# Tytuł
st.title("🛍️ Brazilian E-commerce Dashboard")
st.markdown("### Analiza danych sprzedażowych platformy Olist")

# Wczytanie danych
@st.cache_data
def load_data():
    data = load_processed_data()
    return data

data = load_data()

# Filtry w panelu bocznym
st.sidebar.header("Filtry")

# Filtr daty (jeśli mamy orders_clean w danych)
if 'orders_clean' in data:
    # Konwersja dat
    data['orders_clean']['order_purchase_timestamp'] = pd.to_datetime(data['orders_clean']['order_purchase_timestamp'])
    
    min_date = data['orders_clean']['order_purchase_timestamp'].min().date()
    max_date = data['orders_clean']['order_purchase_timestamp'].max().date()
    
    date_range = st.sidebar.date_input(
        "Zakres dat",
        [min_date, max_date]
    )

# Układ dashboardu
tab1, tab2, tab3, tab4 = st.tabs(["Sprzedaż", "Produkty", "Regiony", "Klienci"])

with tab1:
    st.header("Analiza sprzedaży")
    
    # KPI
    col1, col2, col3, col4 = st.columns(4)
    
    if 'orders_clean' in data:
        with col1:
            st.metric("Liczba zamówień", f"{len(data['orders_clean']):,}")
        
        with col2:
            total_sales = data['orders_clean']['payment_value'].sum()
            st.metric("Całkowita sprzedaż", f"R$ {total_sales:,.2f}")
        
        with col3:
            avg_order = data['orders_clean']['payment_value'].mean()
            st.metric("Średnia wartość zamówienia", f"R$ {avg_order:,.2f}")
        
        with col4:
            delivered = (data['orders_clean']['order_status'] == 'delivered').sum()
            delivery_rate = delivered / len(data['orders_clean'])
            st.metric("Procent dostarczonych", f"{delivery_rate:.1%}")
    
    # Wykres trendu sprzedaży
    if 'monthly_orders' in data:
        st.subheader("Trend sprzedaży miesięcznej")
        fig = px.line(
            data['monthly_orders'], 
            x='yearmonth', 
            y='total_sales',
            title='Miesięczna wartość sprzedaży',
            labels={'yearmonth': 'Miesiąc', 'total_sales': 'Wartość sprzedaży (R$)'}
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Analiza produktów")
    
    # Top kategorie
    if 'product_categories' in data:
        st.subheader("Najpopularniejsze kategorie produktów")
        fig = px.bar(
            data['product_categories'].head(10), 
            x='order_count', 
            y='category',
            title='Top 10 najpopularniejszych kategorii',
            labels={'category': 'Kategoria', 'order_count': 'Liczba zamówień'},
            orientation='h'
        )
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Analiza regionalna")
    
    # Mapa sprzedaży
    if 'state_sales' in data:
        st.subheader("Sprzedaż według stanów")
        fig = create_brazil_map(
            data['state_sales'],
            'state',
            'total_sales',
            'Wartość sprzedaży według stanów Brazylii'
        )
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.header("Analiza klientów")
    
    # Segmenty klientów
    if 'customer_segments' in data:
        st.subheader("Segmenty klientów")
        fig = px.pie(
            data['customer_segments'], 
            names='segment', 
            values='customer_count',
            title='Rozkład klientów według segmentów'
        )
        st.plotly_chart(fig, use_container_width=True)

# Stopka
st.markdown("---")
st.markdown("Dashboard stworzony na podstawie danych Olist dostępnych na Kaggle")