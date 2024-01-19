
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import datetime as dt

df = pd.read_csv('C:/Users/joaco/OneDrive/Escritorio/Python/MercadoLibre/mercadolibre_datos.csv')

df.dropna(subset=['price'], inplace=True)

df['day'] = df['day'].astype('string')

df['day'] = pd.to_datetime(df['day'], errors='coerce', dayfirst=True)

df = df.sort_values(by='day')

fig_hist = px.histogram(df, x='price', animation_frame='day', title='Histogram for each day', template="plotly_white", nbins=20)

avg_price = df.groupby(by='day', dropna=True)['price'].mean().reset_index()


avg_price['day'] = pd.to_datetime(avg_price['day'], format='%d/%m/%Y')

fig_line = px.line(avg_price, x='day', y='price', title='Average Price', template="plotly_white")



def main():

    st.set_page_config(page_title='McBook')

    st.title('MacBook Prices in Mercado Libre')

    st.plotly_chart(fig_line)
    st.plotly_chart(fig_hist)

if __name__ == '__main__':
    main()

