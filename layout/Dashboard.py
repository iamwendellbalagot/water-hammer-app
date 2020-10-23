import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotGenerator.plotGenerator as pg

row1 = html.Tr([html.Td("Minimum PSI"), html.Td("2.4")])
row2 = html.Tr([html.Td("Maximum PSI"), html.Td("34.76")])
row3 = html.Tr([html.Td("Mean"), html.Td("10.8")])
row4 = html.Tr([html.Td("Median"), html.Td("22.18")])

table_body = [html.Tbody([row1, row2, row3, row4])]



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
								    	'borderRadius': '10px',
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
								'marginLeft': '10%'
							},
							children=  'Stop the process'
						),
						html.Hr(
							style = {
								'borderTop': '1px solid #eeeee',
								'width': '80%',
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
						html.Div(
			                children=[
			                    html.Div(
			                        children=[
			                            html.Button(
			                                children='Check',
			                                id = 'controls__checkTest',
			                                className='btn btn-primary',
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
			            html.Div(
			                children=[
			                    html.Div(
			                        children=[
			                            html.Button(
			                                children='Export',
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
						html.Hr(
							style = {
								'position': 'absolute',
								'borderTop': '1px solid #eeeee',
								'width': '50%',
								'right': '5%',
								'marginTop': '3.7%'
							}	
						),
						dcc.Graph(
							id = 'graph__scatter',
							style = {
								'display': 'absolute'
							},
							figure = pg.get_scatter()
						)
					]
				)
			]
		)
	]
)