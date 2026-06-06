
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df=pd.read_csv('Housing.csv')


Floor=df["stories"].value_counts()

Bedrooms=df["bedrooms"].value_counts()

Floor = df["stories"].value_counts()

fig1 = px.pie(
    values=Floor.values,
    names=Floor.index,
    title='PERCENTAGE OF HOUSES SOLD WITH RESPECT TO FLOORS',
    template='plotly_dark'
)

fig1.update_traces(
    textposition='inside',
    textinfo='percent+label'
)
bedroom_avg_price = df.groupby('bedrooms')['price'].mean().reset_index()

fig_bedrooms = px.bar(
    bedroom_avg_price,
    x='bedrooms',
    y='price',
    color='bedrooms',
    text_auto=True,
    title='HOUSE PRICES BY NUMBER OF BEDROOMS',
    template='plotly_dark'
)

fig_bedrooms.update_layout(
    xaxis_title='Bedrooms',
    yaxis_title='Price'
)

Bathrooms=df["bathrooms"].value_counts()
Bathrooms

fig3=px.bar(df.head(200),x='bathrooms',y='price',color='bathrooms',title='MONEY SPEND ON HOUSES BASED ON BATHROOMS',template='plotly_dark')

fig5=px.box(df.head(300),y='price',x='furnishingstatus',color='furnishingstatus',title='HOUSES SOLD BASED ON FURNISHING STATUS ',template="plotly_dark")

fig6=px.strip(df.head(500),x='mainroad',y='price',color='mainroad',title="HOUSES SOLD BESIDE MAINROAD ",template='plotly_dark')

fig7=px.bar(df.head(100),y='parking',x='price',color='parking',template='plotly_dark',title="MONEY SPENT ON HOUSES BASED ON PARKING AREA ",orientation="h")

fig8=px.scatter(df.head(250),x='area',y='price',color="area",title="MONEY SPENT ACCORDING TO AREA OF HOUSES",template='plotly_dark')

fig9=px.bar_polar(df.head(200),r='price',theta='airconditioning',color='airconditioning',title='PEPOLE BUYED HOUSES ACCORDING TO AIR CONDITIONERS AVAILABILITY',template='plotly_dark')



import dash
from dash import html
import dash.dcc as dcc
import plotly.express as px
import plotly.graph_objects as go
app = dash.Dash(__name__)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='HOUSE PRICE ANALYSIS DASHBOARD',
        style={
            'textAlign': 'center',
            'color': colors['text'] }   ),
html.Div(children='  - By SK ADIL', style={
        'textAlign': 'center',
        'color': colors['text']  } ),
   dcc.Graph(
    id='bedrooms-average-price',
    figure=fig_bedrooms,
    style={'width':'50%','display':'inline-block'}
),

    dcc.Graph(id='firstgraph1',figure=fig1,style={'width':'50%','display':'inline-block','backgroundColor': colors['background']}),
    dcc.Graph(id='firstgraph3',figure=fig3,style={'width':'50%','display':'inline-block','backgroundColor': colors['background']}),
    dcc.Graph(id='firstgraph5',figure=fig5,style={'width':'50%','display':'inline-block','backgroundColor': colors['background']}),
    dcc.Graph(id='firstgraph6',figure=fig6,style={'width':'50%','display':'inline-block','backgroundColor': colors['background']}),
    dcc.Graph(id='firstgraph7',figure=fig7,style={'width':'50%','display':'inline-block','backgroundColor': colors['background']}),
    dcc.Graph(id='firstgraph8',figure=fig8,style={'width':'50%','display':'inline-block','backgroundColor': colors['background']}),
    dcc.Graph(id='firstgraph9',figure=fig9,style={'width':'50%','display':'inline-block','backgroundColor': colors['background']}),
])

if __name__ == '__main__':
    app.run(debug=True)



