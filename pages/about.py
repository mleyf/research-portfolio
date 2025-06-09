import dash
from dash import html

dash.register_page(__name__, path="/about")

layout = html.Div([
    html.H2("About Me"),
    html.P("PhD candidate specializing in polymer simulations, machine learning, and sustainable energy materials."),
    # Add more content here
])
