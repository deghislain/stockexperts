from dash import dcc, html


def main_layout():
    return html.Div([
        html.H1("Online Stock Search Engine", style={'textAlign': 'center', 'color': 'blue'}),

        html.Div([
            # Input field for user text
            dcc.Input(id='input-text', type='text', placeholder='Type industry here...', debounce=True, style={'textAlign': 'center', "fontSize": "24px"}),
            html.Button("Search", id="search_id", n_clicks=0, style={'textAlign': 'center', "fontSize": "24px"}),

            # Div to display the output based on input
            html.Div(id='output-text', style={'margin-top': '20px', 'font-size': '20px'})
        ], style={
            'border': '1px solid #000',
            'padding': '20px',
            'width': '50%',
            'height': '50%',
            'margin': 'auto',
            'background-color': '#f0f0f0',
            'border-radius': '10px'

        })
    ], style={
        'textAlign': 'center',
        'width': '100vw',
        'height': '100vh',
        'background': '#87CEEB',
        'margin': '0',
        'padding': '0',
        'overflow': 'hidden',
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'center',
        'alignItems': 'center'
    }, id="main_layout")