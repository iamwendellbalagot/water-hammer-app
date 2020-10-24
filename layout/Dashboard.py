import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import serial.tools.list_ports as serialPorts

import plotGenerator.plotGenerator as pg

device = []
ports = []
for pinfo in serialPorts.comports():
	device.append({'label': pinfo.manufacturer + ' ' + pinfo.device,
		'value': pinfo.device})

items = [
    dbc.DropdownMenuItem("Shutdown the Server", id = 'server__shutdown'),
]

row_style = {
	'padding': '5px',
}

col_style = {
	'padding': '7px',
	'backgroundColor': '#373a40',
	'fontWeight': '500'
}

row0 = html.Tr([
	html.Td("Test ID", id = "td__testID",style = col_style),
	html.Td("Sensor 1", id = '', style = col_style), 
	html.Td("Sensor 2", id = '',style = col_style)],)
row1 = html.Tr([
	html.Td("Minimum PSI",style = row_style), 
	html.Td("0.0", id = 'td__min',style = row_style), 
	html.Td("0.0", id = 'td__min1',style = row_style)])
row2 = html.Tr([
	html.Td("Maximum PSI",style = row_style), 
	html.Td("0.0", id = 'td__max',style = row_style), 
	html.Td("0.0", id = 'td__max1',style = row_style)])
row3 = html.Tr([
	html.Td("Mean",style = row_style), 
	html.Td("0.0", id = 'td__mean',style = row_style), 
	html.Td("0.0", id = 'td__mean1',style = row_style)])
row4 = html.Tr([
	html.Td("Median",style = row_style),
	html.Td("0.0", id = 'td__median',style = row_style), 
	html.Td("0.0", id = 'td__median1',style = row_style)])

table_body = [html.Tbody([row0, row1, row2, row3, row4])]



Layout = html.Div(
	id = 'home',
	style = {
		'display': 'flex',
		'overflow': 'hide',
		'backgroundColor': '#eeeeee'
	},
	children = [
		#NAVBAR ELEMENT
		html.Div(
			id = 'navbar',
			style = {
				'position': 'absolute',
				'width': '100%',
				'height': '50px',
				'top': '0px',
				'backgroundColor':'#373a40'
			},
			children = [
				html.Div(
					style = {'display': 'flex'},
					children = [
						html.Div(
							style = {'flex': '0.5', 'marginTop': '6px'},
							children = [
								dbc.Row(
								    [
								        dbc.Col(
								            dbc.DropdownMenu(
								                label="", children=items, right=True
								            )
								        ),
								    ]
								)
							]
						),
						html.Div(
							style = {
								'display': 'flex',
								'justifyContent': 'left',
							},
							children = [
								html.Img(
									src = './assets/tsu.png',
									style = {
										'height': '40px',
										'marginTop': '5px',
										'marginLeft': '5px'
									}
								),
								html.Img(
									src = './assets/cet.png',
									style = {
										'height': '45px',
										'marginTop': '3px',
										'marginLeft': '5px'
									}
								)
							]
						),
					]
				)
			]
		),
		#HOME LEFT
		html.Div(
			id = 'home__left',
			style = {
				'display': 'flex',
				'flexDirection': 'column',
				'flex': '0.4',
				'height': '100vh',
				'justifyContent': 'center',
				'alignItems': 'center',
				'border-right': '1px solid black'
			},
			children = [
				html.Div(
					id = 'left__results',
					style = {
						'flex': '0.5',
						'borderBottom': '1px solid black',
						'width': '100%',
						'justifyContent': 'center',
						'alignItems': 'center'
					},
					children =[
						html.H3('STATISTICS',
							style = {
								'color': '#373a40',
								'fontWeight': '700',
								'textAlign': 'center',
								'margin': '0',
								'marginTop': '55px',
							}
						),
						html.Hr(
							style = {
								'borderTop': '1px solid #eeeee',
								'width': '80%',
							}	
						),
						html.Div(
							style ={
								'width': '80%',
								'margin': '0 auto'
							},
							children =[
								dbc.Table(table_body, 
									bordered=True,
								    hover=True,
								    responsive=True,
								    striped=True,
								    style = {
								    	'backgroundColor': 'gray',
								    	'color': 'white',
								    	'borderRadius': '5px',
								    }
								)
							]
						)
						
					]
				),
				#CONTROLS *****************
				html.Div(
					id = 'left__controls',
					style = {
						'flex': '0.5',
						'borderBottom': '1px solid black',
						'justifyContent': 'center',
						'width': '100%',
						'alignItems': 'center',
					},
					children =[
						html.H3('CONTROLS',
							style = {
								'color': '#373a40',
								'fontWeight': '700',
								'textAlign': 'center',
								'margin': '0',
								'marginTop': '5px',
							}
						),
						html.Hr(
							style = {
								'borderTop': '1px solid #eeeee',
								'width': '80%',
							}	
						),
						html.Div(
							id = 'controls__input',
							style = {
								'display':'flex', 
								'width': '80%', 
								'marginLeft': '10%', 
								'marginBottom': '5px'
							},
							children = [
								dbc.Input(
									placeholder="Enter test ID",
									id = 'test__id',
									type="text",
									style ={
										'flex': '0.5',
										'marginRight': '2px'
									}
								),
								dbc.InputGroup(
									style ={
										'flex': '0.5',
										'marginLeft': '2px',
									},
									children = [
										dbc.Select(
											id = 'device__port',
											options = [item for item in device]
										),
									]
								),
								# dbc.Input(
								# 	placeholder="Device Port",
								# 	id = 'device__port',
								# 	type="text",
								# 	style ={
								# 		'flex': '0.5',
								# 		'marginLeft': '2px'
								# 	}
								# ),
							]
						),
						
						html.Button(
							id = 'controls__start',
							n_clicks=0,
							className = 'btn btn-primary btn-lg btn-block',
							style = {
								'width': '80%',
								'fontWeight': '500',
								'fontSize': '15px',
								'marginLeft': '10%'
							},
							children=  'Start a test'
						),
						html.Button(
							id = 'controls__stop',
							n_clicks=0,
							className = 'btn btn-danger btn-lg btn-block',
							style = {
								'width': '80%',
								'fontWeight': '500',
								'fontSize': '15px',
								'marginLeft': '10%',
								'display': 'none'
							},
							children=  'Stop the process'
						),
						html.Hr(
							style = {
								'borderTop': '1px solid #eeeee',
								'width': '80%',
								'margin': '5px auto'
							}	
						),
						html.Span('Check test Data',
							style = {
								'color': '#eeeee',
								'textAlign': 'left',
								'margin': '0',
								'marginLeft': '10%',
								'fontWeight': '700'
							}
						),
						#CHECK TEST DATA ********************************
						dbc.Form(
							prevent_default_on_submit = True,
			                children=[
			                    html.Div(
			                        children=[
			                            html.Button(
			                                children='Check',
			                                id = 'controls__checkTest',
			                                className='btn btn-primary',
			                                type = 'submit',
			                                style={'height': '30px',
			                                        'fontSize': '12px',
			                                        'padding': '5px',
			                                        'paddingRight': '8px'}
			                            )
			                        ],
			                        className='input-group-prepend'
			                    ),
			                    dcc.Input(
			                        id= 'controls__input__checkData',
			                        placeholder='Test ID',
			                        type='text',
			                        className='form-control',
			                        style={'height': '30px',
			                                'fontSize': '12px',
			                                'padding': '5px'}
			                    )
			                ],
			                className='input-group mb-3',
			                style={'width': '80%', 'margin': '10px auto 30px auto'}
			            ),
			            html.Span('Export Data',
							style = {
								'color': '#eeeee',
								'textAlign': 'left',
								'margin': '0',
								'marginLeft': '10%',
								'fontWeight': '700'
							}
						),
			            #EXPORT DATA ********************************************
			            dbc.Form(
			            	prevent_default_on_submit = True,
			                children=[
			                    html.Div(
			                        children=[
			                            html.Button(
			                                children='Export',
			                                type = 'submit',
			                                id = 'controls__exportData',
			                                className='btn btn-primary',
			                                style={'height': '30px',
			                                        'fontSize': '12px',
			                                        'padding': '5px'}
			                            )
			                        ],
			                        className='input-group-prepend'
			                    ),
			                    dcc.Input(
			                        id= 'controls__input__exportData',
			                        placeholder='Test ID',
			                        type='text',
			                        className='form-control',
			                        style={'height': '30px',
			                                'fontSize': '12px',
			                                'padding': '5px'}
			                    )
			                ],
			                className='input-group mb-3',
			                style={'width': '80%', 'margin': '10px auto 30px auto'}
			            ),
					]
				)
			]
		),
		#HOME RIGHT *****************************
		html.Div(
			id = 'home__right',
			style = {
				'display': 'flex',
				'flexDirection': 'column',
				'flex': '0.6',
				'height': '100vh',
				'justifyContent': 'center',
				'alignItems': 'center'
			},
			children = [
				html.Div(
					id = 'right__distGraph',
					style = {
						'flex': '0.5',
						'width': '100%',
						'borderBottom': '1px solid black'
					},
					children = [
						html.Div(
							style ={'display': 'flex'},
							children = [
								dcc.Graph(
									id = 'graph__dist1',
									figure = pg.get_bar(title = 'Sensor 1')
								),
								dcc.Graph(
									id = 'graph__dist2',
									figure = pg.get_bar(color = 'rgb(36, 121, 108)',
										title = 'Sensor 2')
								)
							]
						),
						
					]
				),
				html.Div(
					id = 'right__scatterGraph',
					style = {
						'flex': '0.5',
						'width': '100%',
						'borderBottom': '1px solid black'
					},
					children = [
						html.H3('REALTIME DATA DISPLAY',
							style = {
								'position': 'absolute',
								'color': '#373a40',
								'fontWeight': '700',
								'textAlign': 'center',
								'margin': '0',
								'marginTop': '5px',
								'right': '20%',
							}
						),
						dcc.Graph(
							id = 'graph__scatter',
							style = {
								'display': 'absolute'
							},
							figure = pg.get_scatter()
						),
						dcc.Interval(
							id = 'interval__scatter',
							interval = 1000,
							n_intervals = 0,
							disabled = True
						)
					]
				)
			]
		),
		#DUMMIE ELEMENTS
		html.Div(
			id=  'activate__serial',
			style ={'display': 'none'}
		),
		html.Div(
			id=  'activate__shutdown',
			style ={'display': 'block'}
		)

	]
)