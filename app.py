import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash.dash import no_update

import layout.Dashboard as Home

import processSerialData.processSerialData as psd
import plotGenerator.plotGenerator as pg

home__layout = Home.Layout

app = dash.Dash(
	__name__,
	title = 'Water Hammer'
)

app.layout = html.Div(
	children=  [
		home__layout
	],

	id = 'body'
)

#START A TEST
@app.callback(Output('graph__scatter', 'figure'),
			 [Input('controls__start', 'n_clicks')])
def start_test(start__btn):
	changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
	odds = [1,3,5,7,9,11,13]
	even = [2,4,6,8,10,12,14]
	if 'controls__start' in changed_id:
		df = psd.get_serial()
		fig = pg.get_scatter(df)
		return fig
	else:
		raise PreventUpdate()

if __name__ == '__main__':
	app.run_server(debug=True, port=2020)

