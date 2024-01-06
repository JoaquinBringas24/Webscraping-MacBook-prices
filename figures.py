import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import datetime as dt

df = pd.read_csv('C:/Users/joaco/OneDrive/Escritorio/Python/MercadoLibre/mercadolibre_datos.csv')

df.dropna(subset=['price'], inplace=True)

df['day'] = pd.to_datetime(df['day'], format='%d/%m/%Y')

df['day'] = df['day'].dt.strftime('%d/%m/%Y')

df['day'].dt.time.sort_values()

fig_kd = ff.create_distplot([df['price']], ['price'])
fig_kd.write_html("C:/Users/joaco/OneDrive/Escritorio/Python/MercadoLibre/kd.html")

fig_hist = px.histogram(df, x='price', animation_frame='day', title='Histogram for each day', nbins=20,
                        template="plotly_white")
fig_hist.write_html("C:/Users/joaco/OneDrive/Escritorio/Python/MercadoLibre/bar.html")

avg_price = df.groupby(by='day', dropna=True)['price'].mean().reset_index()

pd.to_datetime(avg_price['day'], format='%d/%m/%Y')

fig_line = px.line(avg_price, x='day', y='price', title='Average Price', template="plotly_white")

fig_line.write_html("C:/Users/joaco/OneDrive/Escritorio/Python/MercadoLibre/time_series_avg.html")


