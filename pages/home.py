# pages/home.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/home", name="Home", index=True)

layout = dbc.Container([
    # Hero Section with Photo, Name, and Tagline
    dbc.Row([

        dbc.Col([
            html.Div([
                html.H3("Key Achievements & Skills"),
                html.Ul([
                    html.Li("Fulbright Fellowship for PhD at UChicago"),
                    html.Li("Best Oral Presentation, Organic Battery Days 2025"),
                    html.Li("Best Poster Presentation, MindBytes Conference 2023"),
                    html.Li("President, Society of Hispanic Professional Engineers (SHPE)"),
                    html.Li("MRSEC Grad Student Advisory Committee"),
                    html.Li("Expert in GROMACS, LigParGen, Polyply, Python, and Machine Learning"),
                ]),
            ], style={"margin-top": "20px", "margin-left": "20px"}),
        ], width=6),

        dbc.Col([
            html.Div([
                html.H3("Key Achievements & Skills"),
                html.Ul([
                    html.Li("Fulbright Fellowship for PhD at UChicago"),
                    html.Li("Best Oral Presentation, Organic Battery Days 2025"),
                    html.Li("Best Poster Presentation, MindBytes Conference 2023"),
                    html.Li("President, Society of Hispanic Professional Engineers (SHPE)"),
                    html.Li("MRSEC Grad Student Advisory Committee"),
                    html.Li("Expert in GROMACS, LigParGen, Polyply, Python, and Machine Learning"),
                ]),
            ], style={"margin-top": "20px"}),
        ], width=6),
    ], className="mt-4"),

    # Quick Links and Call to Action
    dbc.Row(
        dbc.Col(
            html.Div([
                html.H4("Let’s Connect!"),
                html.P("Explore my research projects and leadership initiatives, or get in touch to discuss opportunities."),
                dbc.Button("Download CV", color="primary", className="me-2", id="cv-button"),
                dbc.Button("LinkedIn", color="secondary", href="https://www.linkedin.com/in/mleyf/", className="me-2"),
                dbc.Button("Google Scholar", color="info", href="https://scholar.google.com/citations?user=_VPhV1UAAAAJ&hl=en&oi=ao", className="me-2"),
                dbc.Button("Contact", href="/contact", color="dark"),
            ], className="text-center mt-4"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px"}
    ),

], fluid=True)
