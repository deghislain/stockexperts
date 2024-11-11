#!/usr/bin/env python
from stockexperts.crew import StockExpertsSearchCrew
from stockexperts.crew import StockExpertsCompareCrew
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from stock_search_layout import main_layout
from stockexperts.pdf_generator import generate_pdf

topic = ""

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = main_layout()


# Define the callback to update the output text based on the input
@app.callback(
    Output('result-id', 'children'),
    [Input('input-text', 'value'),
     Input("search-button", "n_clicks"),
     Input('input-stock-id', 'value'),
     Input("compare-button", "n_clicks"),
     Input("exp_btn_id", "n_clicks")]
)
def update_output(topic, n_clicks, stocks, compare,exp_btn_id):
    ctx = dash.callback_context
    trigger = ctx.triggered[0]['prop_id'].split('.')[0]
    if trigger == 'exp_btn_id':
        return generate_pdf()
    if stocks:
        topic = stocks
    if topic is None or topic == '':
        return html.P('You have not entered anything yet.', id='output-text')
    else:
        task_type = "compare"

        if trigger == 'search-button':
            task_type = "search"
            topic = topic + '-related'

        inputs = {
            'topic': topic
        }
        result = None
        if task_type == 'search':
            result = StockExpertsSearchCrew().crew().kickoff(inputs=inputs)
        else:
            result = StockExpertsCompareCrew().crew().kickoff(inputs=inputs)
        if result:
            return dcc.Markdown(str(result.tasks_output[1]))


def run():
    app.run_server(debug=True)



