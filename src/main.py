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
def update_output(topic, n_clicks, stocks, compare, exp_btn_id):
    ctx = dash.callback_context
    trigger = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger == 'exp_btn_id':
        last_task = '_compare' if stocks else '_search' if topic else ''
        if last_task:
            return generate_pdf(last_task)

    if not topic and not stocks:
        return html.P('You have not entered anything yet.', id='output-text')

    inputs = {'topic': topic or stocks}

    if trigger == 'search-button':
        result = StockExpertsSearchCrew().crew().kickoff(inputs=inputs)
    elif trigger == 'compare-button':
        result = StockExpertsCompareCrew().crew().kickoff(inputs=inputs)
    else:
        return html.P('Please provide an input and click a button to start.', id='output-text')

    return dcc.Markdown(str(result.tasks_output[1]))


def run():
    app.run_server(debug=True)



