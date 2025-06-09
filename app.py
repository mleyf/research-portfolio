import dash  
from dash import html, dcc  
import dash_bootstrap_components as dbc  

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])  
server = app.server  

app.layout = dbc.Container([  
    # Navigation Bar  
    dbc.NavbarSimple(  
        children=[  
            dbc.NavItem(dbc.NavLink("About", href="#about")),  
            dbc.NavItem(dbc.NavLink("Research", href="#research")),  
            dbc.NavItem(dbc.NavLink("Leadership", href="#leadership")),  
            dbc.NavItem(dbc.NavLink("Contact", href="#contact")),  
        ],  
        brand="Dr. Maria Leyva",  
        brand_href="#",  
        sticky="top",  
        color="primary",  
        dark=True  
    ),  

    # Hero Section  
    dbc.Row(  
        dbc.Col(  
            html.Div([  
                html.H1("Soft Matter Physicist & Computational Researcher"),  
                html.P("PhD candidate at the University of Chicago specializing in polymer simulations, machine learning, and sustainable energy materials."),  
                dbc.Button("Download CV", color="primary", className="me-2"),  
                dbc.Button("GitHub", color="secondary", href="https://github.com/mleyf"),  
            ], className="text-center mt-5"),  
            width=12  
        )  
    ),  
], fluid=True)  

