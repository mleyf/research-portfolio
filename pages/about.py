# pages/home.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import dcc


dash.register_page(__name__, path="/about", name="About Me", index=True)


locations = pd.DataFrame({
    'City': ['Hermosillo', 'Hermosillo', 'Chicago', 'Leuven'],  # Add your cities
    'Country': ['Mexico', 'Mexico', 'USA', 'Belgium'],  # Add your countries
    'Latitude': [41.083616716170432, 29.146612964084298, 41.79236723741779, 50.863569221261194],    # Add your latitudes
    'Longitude': [-87.96002414617216, -110.88545175347738, -87.60044941287656, 4.676122324474524],     # Add your longitudes
    'Label': [
        'Universidad de Sonora',
        'GSE Biomedical',
        'University of Chicago',
        'KU Leuven',
    ]  # Add your labels
})


# Improved map
fig = px.scatter_geo(
    locations,
    lat='Latitude',
    lon='Longitude',
    hover_name='Label',
    projection='natural earth',
    template='plotly_white',
    size_max=12,
)
fig.update_traces(marker=dict(size=14, color='#800000', line=dict(width=2, color='white')))
fig.update_layout(
    margin={'r':0, 't':0, 'l':0, 'b':0},
    geo=dict(
        showcountries=True,
        showland=True,
        landcolor='#f8f9fa',
        showocean=True,
        oceancolor='#e3e6ea',
        showframe=False,
        projection_scale=1.1,
    ),
    height=340,
    showlegend=False
)





layout = dbc.Container([

    # About Me Card
    dbc.Row(
        dbc.Col(
            html.Div([
                html.H4("About Me", className="mb-3"),
                html.P("I am passionate about advancing the field of materials science through innovative research and collaboration. My goal is to contribute to the development of sustainable materials that can address global challenges."),
                html.P("In addition to my research, I am actively involved in leadership roles within the academic community, including serving as the President of the Society of Hispanic Professional Engineers (SHPE) and participating in the MRSEC Grad Student Advisory Committee."),
                html.P("I am also committed to outreach and education, aiming to inspire the next generation of scientists and engineers through mentorship and community engagement."),
            ], className="text-left"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "24px", "border-radius": "12px", "margin-bottom": "24px"}
    ),

    # Map + Education/Experience card
    dbc.Row(
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5("International Study and Work Locations", className="mb-4 mt-2 text-center", style={"color": "#800000"}),
                    dbc.Row([
                        dbc.Col(
                            dcc.Graph(
                                figure=fig,
                                config={'displayModeBar': False},
                                style={'height': '320px', 'width': '100%'}
                            ), width=5
                        ),
                        dbc.Col([
                            html.H5("Education", className="mb-2"),
                            html.Ul([
                                html.Li("PhD Candidate in Molecular Engineering, University of Chicago (2020 - Present)"),
                                html.Li("Bachelor of Science in Materials Engineering, Universidad de Sonora, Mexico (2013 - 2018)"),
                            ]),
                            html.H5("Research Experience", className="mb-2 mt-3"),
                            html.Ul([
                                html.Li("Visiting Graduate Researcher, KU Leuven, Belgium (Jan 2025 - Present)"),
                                html.Li("Graduate Research Assistant, University of Chicago (Jan 2021 - Dec 2024)"),
                                html.Li("Materials Research Intern, GSE Biomedical (Jan 2018 - Dec 2018)"),
                                html.Li("Undergraduate Researcher, Universidad de Sonora (2015 - 2018)"),
                            ]),
                        ], width=7)
                    ])
                ]),
                className="shadow-sm",
                style={"border-radius": "12px", "margin-bottom": "24px"}
            ), width=12
        )
    ),


    dbc.Row(
        dbc.Col(
            html.Div([

                html.H4("Awards and Honors"),
                html.Ul([
                    html.Li("Fulbright Fellowship for PhD at UChicago (2020 - Present)"),
                    html.Li("SHPE Graduate Award, Society of Hispanic Professional Engineers (2024)"),
                    html.Li("Best Oral Presentation, Organic Battery Days 2025"),
                    html.Li("Best Poster Presentation, MindBytes Conference 2023"),
                ]),

            ], className="text-left mt-4"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px"}
    ),

    dbc.Row(
        dbc.Col(
            html.Div([
                html.H4("Skills"),
                html.Ul([
                    html.Li("Expert in GROMACS, LigParGen, Polyply, Python, and Machine Learning"),
                    html.Li("Fluent in English and Spanish"),
                    html.Li("Strong communication and leadership skills"),
                ]),

            ], className="text-left mt-4"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px"}
    ),

    dbc.Row(
        dbc.Col(
            html.Div([
                html.H4("Publications"),
                html.Ul([
                    html.Li("Flores, M. L., et al. (2024). 'Molecular Dynamics Simulations of Polymer Blends for Energy Applications.' Journal of Materials Science."),
                    html.Li("Flores, M. L., et al. (2023). 'Machine Learning Approaches for Predicting Polymer Properties.' Advanced Materials."),
                ]),
            ], className="text-left mt-4"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px"}
    ),

   ], fluid=True)
