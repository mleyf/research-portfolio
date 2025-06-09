# pages/home.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/contact", name="Contact", index=True)


layout = dbc.Container([

    # Quick Links and Call to Action
    dbc.Row(
        dbc.Col(
            html.Div([

                html.H4("Contact Information"),
                html.P("Feel free to reach out for collaboration, inquiries, or just to connect!"),
                html.P("Email:  mleyf@uchicago.edu"),
                html.P("Phone: (+352)691-161-456"),  # Placeholder phone number

                dbc.Button("Download CV", color="primary", className="me-2", id="cv-button"),
                dbc.Button("LinkedIn", color="secondary", href="https://www.linkedin.com/in/mleyf/", className="me-2"),
                dbc.Button("GitHub", color="info", href=""),
                dbc.Button("Email", color="success", href="mailto:mleyf@uchicago.edu", className="me-2"),
            ], className="text-center mt-4"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px"}
    ),

], fluid=True)
