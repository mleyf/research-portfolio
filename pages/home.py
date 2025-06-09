# pages/home.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/", name="Home", index=True)

# Sample data for interactive plot
df = pd.DataFrame({
    "Concentration (%)": [10, 30, 50],
    "Diffusion Coefficient (m²/s)": [2.1e-9, 1.5e-9, 0.8e-9]
})
fig = px.line(df, x="Concentration (%)", y="Diffusion Coefficient (m²/s)", 
              title="Diffusion Coefficient vs. Concentration in Polymer Blends",
              labels={"Concentration (%)": "Concentration (%)", "Diffusion Coefficient (m²/s)": "Diffusion Coefficient (m²/s)"})

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
                dbc.Button("GitHub", color="info", href="https://github.com/mleyf", className="me-2"),
                dbc.Button("Contact", href="/contact", color="light"),
            ], className="text-center mt-4"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px"}
    ),

    # Interactive Plot Example
    dbc.Row(
        dbc.Col(
            dcc.Graph(figure=fig, id="diffusion-plot"),
            width=12
        )
    ),
], fluid=True)
