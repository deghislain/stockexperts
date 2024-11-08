from dash import dcc, html


def main_layout():
    return html.Main([
        html.H1("Online Stock Search Engine", style={'textAlign': 'center', 'color': 'blue'}),

        html.Div([
            # Input field for user text
            dcc.Input(id='input-text', type='text', placeholder='Type industry/sector here...e.g Technology/IT', debounce=True,
                      style={'textAlign': 'center', "fontSize": "20px",  'width': '50%'}),
            html.Button("Search", id="search_id", n_clicks=0, style={'textAlign': 'center', "fontSize": "20px"})
        ], style={
            'border': '1px solid #000',
            'width': '50%',
            'height': '20%',
            'margin': 'auto',
            'display': 'block',
            'overflow': 'hidden',
            'background-color': 'SlateBlue',
            'border-radius': '10px'

        }),
        html.Div(id='result_id', style={
            'border': '1px solid #000',
            'width': '50%',
            'height': '80%',
            'margin': 'auto',
            'overflow': 'auto',
            'background-color': 'white',
            'border-radius': '10px'
        })
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
    }, id="main_layout")