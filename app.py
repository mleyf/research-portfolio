# app.py
from dash import Dash, html, page_container
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    # Navigation Bar
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("About", href="/about")),
            dbc.NavItem(dbc.NavLink("Research", href="/research")),
            #dbc.NavItem(dbc.NavLink("Leadership", href="/leadership")),
            dbc.NavItem(dbc.NavLink("Teaching", href="/teaching")),
            #dbc.NavItem(dbc.NavLink("Presentations", href="/presentations")),
            dbc.NavItem(dbc.NavLink("Outreach", href="/outreach")),
            #dbc.NavItem(dbc.NavLink("Awards", href="/awards")),
            dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
        ],
        brand="Maria Ley Flores, PhD Candidate",
        brand_href="/",  # <-- Link to home page
        sticky="top",
        color="#800000", # Maroon color
        dark=True,
    ),

    # Hero Section (Two Columns)
    dbc.Row([
        # Left Column: Photo
        dbc.Col(
            html.Div([
                html.Img(
                    src="assets/images/profile_picture.jpeg",
                    style={
                        "width": "150px",
                        "border-radius": "80%",
                        "margin": "auto",  # Center the image
                        "display": "block",  # Center the image
                        "margin-top": "20px",
                        "margin-bottom": "20px",
                        "margin-left": "180px",
                    }
                )
            ], className="text-center"),
            width={"size": 3, "offset": 0},
        ),
        # Right Column: Info
        dbc.Col(
            html.Div([
                html.H1("Computational Polymer Researcher"),
                html.P(
                    "Specializing in molecular dynamics simulations of polymers, machine learning for materials property prediction, and sustainable energy materials at the University of Chicago."
                ),
                # Uncomment if you want buttons here
                # dbc.Button("Download CV", color="primary", className="me-2"),
                # dbc.Button("LinkedIn", color="secondary", href="https://www.linkedin.com/in/mleyf/"),
            ], className="text-left mt-5"),
            width={"size": 8, "offset": 0},
        ),
    ], className="mt-4 mb-4"),

    # Page Container (for multi-page content)
    html.Div(page_container)
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
