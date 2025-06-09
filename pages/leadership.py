# pages/home.py
import dash
from dash import html

dash.register_page(__name__, path="/leadership", name="Home", index=True)

layout = html.Div([
    html.H2("Leadership Roles and Contributions"),
    html.P("This page will showcase my leadership roles and contributions during my career."),
])
