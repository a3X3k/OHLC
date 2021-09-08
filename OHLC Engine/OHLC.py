import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_table as dt
import plotly.graph_objs as go
import random
import pickle
import pandas as pd
import plotly.express as px
colors = {"background": "#DC143C", "text": "#FAF0E6","dash": "#000000"}

# ticker file -pdf last point
data= pd.read_json('stock list.json')
ticker_list = data['symbol'].unique()
external_stylesheets = [dbc.themes.SLATE]

# adding css
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div(
    style={"dash" : colors["background"]},
    children=[
        html.Div(
            [  # header Div
                dbc.Row(
                    [
                        dbc.Col(
                            html.Header(
                                [
                                    html.H1(
                                        "Stock Dashboard",
                                        style={
                                            "textAlign": "center",
                                            "color": colors["text"],
                                        },
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(
            [  # Dropdown Div
                dbc.Row(
                    [
                        dbc.Col(  # Tickers
                            dcc.Dropdown(
                                id="stock_name",
                                options=[
                                    {
                                        "label": str(ticker_list[i]),
                                        "value": str(ticker_list[i]),
                                    }
                                    for i in range(len(ticker_list))
                                ],
                                searchable=True,
                                value=str(
                                    random.choice(
                                        [
                                            "TSLA",
                                            "GOOGL",
                                            "F",
                                            "GE",
                                            "AAL",
                                            "DIS",
                                            "DAL",
                                            "AAPL",
                                            "MSFT",
                                            "CCL",
                                            "GPRO",
                                            "ACB",
                                            "PLUG",
                                            "AMZN",
                                        ]
                                    )
                                ),
                                placeholder="enter stock name",
                            ),
                            width={"size": 3, "offset": 3},
                        ),
                        dbc.Col(  # Graph type
                            dcc.Dropdown(
                                id="chart",
                                options=[
                                    {"label": "bar", "value": "Bar"},
                                    {"label": "candlestick",
                                        "value": "Candlestick"},
                                    {"label": "OHLC", "value": "OHLC"},
                                ],
                                value="Bar",
                                style={"color": "#000000"},
                            ),
                            width={"size": 3},
                        ),
                        dbc.Col(  # button
                            dbc.Button(
                                "Plot",
                                id="submit-button-state",
                                className="mr-1",
                                n_clicks=1,
                                target ='www.google.com'
                            ),
                            width={"size": 2},
                        ),
                    ]
                )
            ]
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(
            [
                
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(
                                id="graph",
                                config={
                                    "displaylogo": False,
                                    "modeBarButtonsToRemove": ["pan2d", "lasso2d"],
                                },
                            ),
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dt.DataTable(
                                id="info",
                                style_table={"height": "auto"},
                                style_cell={
                                    "white_space": "normal",
                                    "height": "auto",
                                    "backgroundColor": colors["background"],
                                    "color": "white",
                                    "font_size": "16px",
                                },
                                style_data={"border": "#4d4d4d"},
                                style_header={
                                    "backgroundColor": colors["background"],
                                    "fontWeight": "bold",
                                    "border": "#4d4d4d",
                                },
                                style_cell_conditional=[
                                    {"if": {"column_id": c}, "textAlign": "center"}
                                    for c in ["attribute", "value"]
                                ],
                            ),
                            width={"size": 6, "offset": 3},
                        )
                    ]
                ),
            ]
        ),
    ],
)

# Callback to the main graph
@app.callback(
    # output
    Output("graph", "figure"),
    # input
    [Input("submit-button-state", "n_clicks")],
    # state
    [State("stock_name", "value"), State("chart", "value")],
)

#Graph function
def graph_genrator(n_clicks, ticker, chart_name):
    def ohlc(sym,chart_name):
        dataset= pd.read_json('Stock list.json')
        dataset.head(1)
        df1 = dataset[dataset['symbol'] == sym]
        print(chart_name)
        if chart_name=='OHLC':
            fig = go.Figure(data=go.Ohlc(x=df1['date'],
            open=df1['open'],
            high=df1['high'],
            low=df1['low'],
            close=df1['close']))
            fig.update_layout(title='Prices over time',
            xaxis_title='Dates',
            yaxis_title='Prices'
            ),
            fig.update_xaxes(
                rangeslider_visible=True,
                rangeselector=dict(
                    activecolor="blue",
                    bgcolor=colors["background"],
                    buttons=list(
                        [
                            dict(count=7, label="10D",
                                 step="day", stepmode="backward"),
                            dict(
                                count=15, label="15D", step="day", stepmode="backward"
                            ),
                            dict(
                                count=1, label="1m", step="month", stepmode="backward"
                            ),
                            dict(
                                count=3, label="3m", step="month", stepmode="backward"
                            ),
                            dict(
                                count=6, label="6m", step="month", stepmode="backward"
                            ),
                            dict(count=1, label="1y", step="year",
                                 stepmode="backward"),
                            dict(count=5, label="5y", step="year",
                                 stepmode="backward"),
                            dict(count=1, label="YTD",
                                 step="year", stepmode="todate"),
                            dict(step="all"),
                        ]
                    ),
                ))
        elif chart_name=='Candlestick':
            
            df1 = dataset[dataset['symbol'] == sym]
            fig= go.Figure(data=go.Candlestick(x=df1['date'],
            open=df1['open'],
            high=df1['high'],
            low=df1['low'],
            close=df1['close']))
            fig.update_layout(title='Prices over time',
            xaxis_title='Dates',
            yaxis_title='Prices'
            ),
            fig.update_xaxes(
                rangeslider_visible=True,
                rangeselector=dict(
                    activecolor="blue",
                    bgcolor=colors["background"],
                    buttons=list(
                        [
                            dict(count=7, label="10D",
                                 step="day", stepmode="backward"),
                            dict(
                                count=15, label="15D", step="day", stepmode="backward"
                            ),
                            dict(
                                count=1, label="1m", step="month", stepmode="backward"
                            ),
                            dict(
                                count=3, label="3m", step="month", stepmode="backward"
                            ),
                            dict(
                                count=6, label="6m", step="month", stepmode="backward"
                            ),
                            dict(count=1, label="1y", step="year",
                                 stepmode="backward"),
                            dict(count=5, label="5y", step="year",
                                 stepmode="backward"),
                            dict(count=1, label="YTD",
                                 step="year", stepmode="todate"),
                            dict(step="all"),
                        ]
                    ),
                ))
        else:
            df1 = dataset[dataset['symbol'] == sym]
            fig = px.bar(df1, y=df1['high'], x='date')

   
        return fig
    
    #print('Hi')
    return ohlc(ticker,chart_name)
    
if __name__ == "__main__":
    app.run_server()