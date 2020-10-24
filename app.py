import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash.dash import no_update
from flask import request
import flask

import serial
import numpy as np
import pandas as pd

import layout.Dashboard as Home

import processSerialData.processSerialData as psd
import plotGenerator.plotGenerator as pg

from flaskwebgui import FlaskUI #get the FlaskUI class
server = flask.Flask(__name__)
ui = FlaskUI(app=server,
		port=5020,
		height = 720,
		width = 1380)

home__layout = Home.Layout

PROCESS = True

app = dash.Dash(
	__name__,
	server = server,
	title = 'Water Hammer'
)

app.layout = html.Div(
	children=  [
		home__layout
	],

	id = 'body'
)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

#START A TEST
@app.callback([Output('controls__start', 'style'),
			   Output('controls__stop', 'style'),
			   Output('controls__input', 'style'),
			   Output('interval__scatter', 'disabled')],
			 [Input('controls__start', 'n_clicks'),
			  Input('controls__stop', 'n_clicks'),
			  Input('test__id', 'value'),
			  Input('device__port', 'value')])
def start_test(start__btn, stop_btn, test__id, dev_port):
	changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

	if 'controls__start' in changed_id and test__id != '' and dev_port:
		psd.process = True
		return {'width': '80%',
				'fontWeight': '500',
				'fontSize': '15px',
				'marginLeft': '10%',
				'display': 'none'}, {
							'width': '80%',
							'fontWeight': '500',
							'fontSize': '15px',
							'marginLeft': '10%',
							'display': 'block'
									}, {
										'display':'flex', 
										'width': '80%', 
										'marginLeft': '10%', 
										'marginBottom': '5px',
										'display': 'none'
									},False
	elif 'controls__stop' in changed_id and test__id != '' and dev_port:
		# arduino = serial.Serial('COM16', 9600)
		# arduino.close()
		psd.process = False
		return {'width': '80%',
				'fontWeight': '500',
				'fontSize': '15px',
				'marginLeft': '10%',
				'display': 'block'}, {
							'width': '80%',
							'fontWeight': '500',
							'fontSize': '15px',
							'marginLeft': '10%',
							'display': 'none'
						}, {
							'display':'flex', 
							'width': '80%', 
							'marginLeft': '10%', 
							'marginBottom': '5px',
							'display': 'flex'
							},True
	else:
		raise PreventUpdate()

@app.callback(Output('activate__serial', 'children'),
			 [Input('controls__start', 'n_clicks'),
			  Input('test__id', 'value'),
			  Input('device__port', 'value')])
def activate_serial(btn, test__id, dev_port):
	changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
	try:
		if 'controls__start' in changed_id and test__id != '' and dev_port:
			psd.upload_generate(table = test__id, port = dev_port)
			return no_update
		else:
			return no_update
	except:
		raise PreventUpdate()

@app.callback(Output('graph__scatter', 'figure'),
			 [Input('controls__start', 'n_clicks'),
			  Input('interval__scatter', 'n_intervals'),
			  Input('test__id', 'value'),
			  Input('interval__scatter', 'disabled'),
			  Input('controls__checkTest', 'n_clicks'),
			  Input('controls__input__checkData', 'value'),
			  Input('controls__exportData', 'n_clicks'),
			  Input('controls__input__exportData', 'value')])
def update__scatter(start__btn, interval__scatter, test__id, n_running, check__btn, check__input, export__btn, export__input):
	changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
	
	try:
		if n_running == False:
			df = psd.get_dataframe(table=test__id)
			fig = pg.get_scatter(df)
			return fig
		elif 'controls__checkTest' in changed_id:
			df = psd.get_dataframe(table=check__input)
			fig = pg.get_scatter(df)
			return fig
		elif 'controls__exportData' in changed_id:
			df = psd.get_dataframe(table=export__input)
			df.columns = ['Pressure S1', 'Pressure S2']
			df.to_csv('./csv_files/'+ export__input + '.csv')
			return no_update
		else:
			return no_update
	except:
		raise PreventUpdate()

@app.callback([Output('td__min', 'children'),
			   Output('td__max', 'children'),
			   Output('td__mean', 'children'),
			   Output('td__median', 'children'),
			   Output('td__min1', 'children'),
			   Output('td__max1', 'children'),
			   Output('td__mean1', 'children'),
			   Output('td__median1', 'children'),
			   Output('td__testID', 'children')],
			   [Input('controls__checkTest', 'n_clicks'),
			    Input('controls__input__checkData', 'value')])
def update__statistics(check__btn, check__input):
	changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
	try:
		if 'controls__checkTest' in changed_id:
			df = psd.get_dataframe(table=check__input)
			td__testID = 'Test ID: {}'.format(check__input)
			return str(np.min(df.S1).round(2)), str(np.max(df.S1).round(2)), str(np.mean(df.S1).round(2)), str(np.median(df.S1).round(2)), \
				str(np.min(df.S2).round(2)), str(np.max(df.S2).round(2)), str(np.mean(df.S2).round(2)), str(np.median(df.S2).round(2)), td__testID
		else:
			return no_update
	except:
		raise PreventUpdate()

@app.callback([Output('graph__dist1', 'figure'),
			   Output('graph__dist2', 'figure')],
			  [Input('controls__checkTest', 'n_clicks'),
			   Input('controls__input__checkData', 'value')])
def update__distGraphs(check__btn, check__input):
	changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
	try:
		if 'controls__checkTest' in changed_id:

			df = psd.get_dataframe(table=check__input)
			fig1 = pg.get_bar(title='Sensor 1', df = df['S1'])
			fig2 = pg.get_bar(title='Sensor 2', df = df['S2'], color = 'rgb(36, 121, 108)')
			return fig1, fig2
		else:
			return no_update, no_update
	except:
		raise PreventUpdate()

@app.callback(Output('activate__shutdown', 'children'),
			 [Input('server__shutdown', 'n_clicks')])
def close(shutdown__btn):
	changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
	try:
		if 'server__shutdown' in changed_id:
			shutdown_server()
			return no_update
		else:
			return no_update
	except:
		raise PreventUpdate()



if __name__ == '__main__':
	#app.run_server(debug=True, port=2020)
	ui.run()

