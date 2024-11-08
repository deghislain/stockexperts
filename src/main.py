#!/usr/bin/env python
from stockexperts.crew import StockexpertsCrew
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from stock_search_layout import main_layout
import stockexperts.test as t

topic = ""

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = main_layout()


# Define the callback to update the output text based on the input
@app.callback(
    Output('result_id', 'children'),
    [Input('input-text', 'value'),
     Input("search_id", "n_clicks")]
)
def update_output(topic, n_clicks):
    if topic is None or topic == '':
        return html.P('You have not entered anything yet.',id='output-text')
    else:
        ctx = dash.callback_context
        trigger = ctx.triggered[0]['prop_id'].split('.')[0]
        if trigger == 'search_id':
            inputs = {
                'topic': topic
            }
            result = StockexpertsCrew().crew().kickoff(inputs=inputs)
            if result:
                return dcc.Markdown(str(result.tasks_output[1]))


def run():
    app.run_server(debug=True)
