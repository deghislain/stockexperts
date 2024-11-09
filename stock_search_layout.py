from dash import dcc, html


# Style dictionaries
INPUT_STYLE = {'textAlign': 'center', "fontSize": "20px", 'width': '50%'}
BUTTON_STYLE = {'textAlign': 'center', "fontSize": "20px", 'border-radius': '10px'}
CONTAINER_STYLE = {'border': '1px solid #000', 'width': '50%', 'margin': 'auto', 'display': 'block', 'overflow': 'hidden', 'background-color': 'SlateBlue', 'border-radius': '15px'}
RESULT_STYLE = {'border': '1px solid #000', 'width': '50%', 'height': '80%', 'margin': 'auto', 'overflow': 'auto', 'background-color': 'white', 'border-radius': '15px'}


def main_layout():
    return html.Main([
        html.H1("Online Stock Search Engine", style={'textAlign': 'center', 'color': 'blue'}),

        html.Section([
            dcc.Input(id='input-text', type='text', placeholder='Type industry/sector here...e.g Technology/IT',
                      debounce=True, style=INPUT_STYLE),
            html.Button("Search", id="search-button", n_clicks=0, style=BUTTON_STYLE),
            dcc.Input(id='input-stock-id', type='text', placeholder='Type 2 to 3 stocks symbols here',
                      debounce=True, style={'textAlign': 'center', "fontSize": "20px", 'width': '50%', 'margin-left': '9%', 'margin-top': '5%'}),
            html.Button("Compare Stocks", id="compare-button", n_clicks=0, style=BUTTON_STYLE),
            html.Br(),
            html.Button("Export as PDF", id="export-button", n_clicks=0, style=BUTTON_STYLE),
        ], style=CONTAINER_STYLE),

        html.Div(id='result-id', style=RESULT_STYLE)
    ], style={
        'width': '100vw',
        'height': '100vh',
        'position': 'absolute',
        'top': 0,
        'left': 0,
        'right': 0,
        'bottom': 0,
        'overflow': 'auto',
        'background': '#87CEEB',
        'textAlign': 'center'
    }, id="main-layout")