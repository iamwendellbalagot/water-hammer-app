import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import sys


def get_scatter(df=None):

	if df is None:
		x=[0, 50, 100, 200, 300, 400, 500, 600]
		y=[0, 1.5, 2, 4, 7.5, 12.5, 20, 40.6]
		y1=[0, 1.7, 3, 5, 8.5, 15.5, 24, 42.6]
	else:
		x = np.arange(len(df))
		y = df['S1']
		y1 = df['S2']

	fig = go.Figure()
	fig.add_trace(go.Scatter(x=x,
	                         y=y,
	                         name='Sensor 1',
	                         marker_color='steelblue'))
	fig.add_trace(go.Scatter(x=x,
	                         y=y1,
	                         name='Sensor 2',
	                         marker_color='lightgreen'))

	fig.update_layout(title=dict(
	    x=0.5,
	    y=0.8,
	                      font=dict(size=20, color='black')),
	                  template='plotly_dark',
	                  height=330,
	                  width=800,
	                  font=dict(family="Courier",
	                            size=12, color='black'),
	                  paper_bgcolor='rgba(0,0,0,0)',
	                              plot_bgcolor='gray')
	fig.update_xaxes(title='Time Interval')
	fig.update_yaxes(title='PRESSURE in PSI')
	return fig


def get_bar(color='steelblue', title = ''):
    d1 = np.random.normal(5, 0.5, 200)
    d2 = np.random.normal(30, 1.2, 60)
    d3 = np.random.normal(6, 1, 60)

    data = np.concatenate((d1, d2, d3))
    df = pd.DataFrame()
    df['data'] = data
    x = []

    for i in range(int(len(data)/20)):
        for r in range(20):
        	x.append(i)

    df['bin'] = np.array(x)


    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['bin'],
                         y=df['data'],
                         name='Sensor 1',
                         marker_color= color))

    fig.update_layout(title=dict(
    						text = "<b>{}</b>".format(title),
					        x=0.5,
					        y= 0.8,
                          	font=dict(size=20, color='black')),
                      template='plotly_dark',
                      height=330,
                      width= 400,
                      font=dict(family="Courier",
                                size=12, color='black'),
                      paper_bgcolor='rgba(0,0,0,0)',
                                  plot_bgcolor='gray')
    fig.update_xaxes(title='Time Interval')
    fig.update_yaxes(title='PRESSURE in PSI')
    return fig
