import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import sys


def get_scatter(df=None):

	if df is None:
		x = [0, 50, 100, 200, 300, 400, 500, 600]
		y = [0, 1.5, 2, 4, 7.5, 12.5, 20, 40.6]
		y1 = [0, 1.7, 3, 5, 8.5, 15.5, 24, 42.6]
	else:
		x = np.arange(len(df))
		y = df['S1']
		y1 = df['S2']

	fig = go.Figure()
	fig.add_trace(go.Scatter(x=x,
	                         y=y,
	                         name='Sensor 1',
	                         marker_color='#E48F72'))
	fig.add_trace(go.Scatter(x=x,
	                         y=y1,
	                         name='Sensor 2',
	                         marker_color='lightgreen'))

	fig.update_layout(title=dict(
					    x=0.5,
					    y=0.8,
	                    font=dict(size=20, color='black')),
					legend=dict(
				        x=0,
				        y=1,
				        bgcolor = '#373a40',
				        traceorder='normal',
				        font=dict(
				            size=12,
				            color= 'white'),
				    ),
					template='plotly_dark',
					height=330,
					width=800,
					font=dict(family="Courier",
					        size=12, color='black'),
					paper_bgcolor='rgba(0,0,0,0)',
					plot_bgcolor='gray',
				    margin=dict(t=50, b=70, l=80, r=1))
	fig.update_xaxes(title='Time Interval [100ms]')
	fig.update_yaxes(title='PRESSURE in PSI')
	return fig


def get_bar(color='steelblue', title='', df=None):

	SIZE = 10

	if df is None:
	    d1 = np.random.normal(5, 0.5, 200)
	    d2 = np.random.normal(30, 1.2, 60)
	    d3 = np.random.normal(6, 1, 60)

	    data = np.concatenate((d1, d2, d3))
	    df = pd.DataFrame()
	    df['data'] = data
	else:
		
		data = df.values
		modulo = len(data) % SIZE
		df = pd.DataFrame()
		df['data'] = data
		if modulo> 0:
			df = df[:-modulo]
		df.dropna(inplace = True)

	x = []
	for i in range(int(len(df.data)/SIZE)):
	    for r in range(SIZE):
	    	x.append(i)
	df['bin'] = np.array(x)
	df = df.groupby('bin').max()
	


	fig = go.Figure()
	fig.add_trace(go.Bar(x=df.index,
	                     y=df.values.flatten(),
	                     name='Sensor 1',
	                     marker_color= color))

	fig.update_layout(title=dict(
						text = "<b>{}</b>".format(title),
				        x=0.6,
				        y= 0.8,
                      	font=dict(size=20, color='black')),
					template='plotly_dark',
					height=330,
					width= 400,
					font=dict(family="Courier",
					        size=12, color='black'),
					paper_bgcolor='rgba(0,0,0,0)',
					plot_bgcolor='gray',
				    margin=dict(r=1))
	fig.update_xaxes(title='Time Interval [1s]')
	fig.update_yaxes(title='PRESSURE in PSI')
	return fig
