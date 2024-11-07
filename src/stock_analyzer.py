import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    # Input field for user text
    dcc.Input(id='input-text', type='text', placeholder='Type something here...', debounce=True),

    # Div to display the output based on input
    html.Div(id='output-text', style={'margin-top': '20px', 'font-size': '20px'})
])


# Define the callback to update the output text based on the input
@app.callback(
    Output('output-text', 'children'),
    [Input('input-text', 'value')]
)
def update_output(input_value):
    if input_value is None or input_value == '':
        return 'You have not entered anything yet.'
    else:
        return f'You typed: {input_value}'


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
