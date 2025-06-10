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
        brand="María Ley Flores, PhD Candidate",
        brand_href="/",  # <-- Link to home page
        sticky="top",
        color="#210535", # Dark purple color
        dark=True,
    ),


    # Hero Section with Background Image
    html.Div(
        dbc.Row([
            # Left Column: Photo (right-aligned inside the column)
            dbc.Col(
                html.Div([
                    html.Img(
                        src="assets/images/profile_picture.jpeg",
                        style={
                            "width": "180px",
                            "border-radius": "80%",
                            "margin-top": "20px",
                            "margin-bottom": "20px",
                            "margin-left": "auto",
                            "margin-right": "0",
                            "display": "block",
                        }
                    )
                ], style={"padding-right": "1rem", "padding-left": "0"}),
                width={"size": 3, "offset": 0},
            ),
            # Right Column: Info (left-aligned inside the column)
            dbc.Col(
                html.Div([
                    html.H2("María Ley Flores"),
                    html.H1("Computational Materials Researcher"),
                    html.H5(["Designing next-generation sustainable polymers from the molecular level"], style={"color": "skyblue"}),
                    html.P(
                    #    "Molecular simulation of sustainable polymers | Machine learning for materials design & property prediction"
                    ),
                ], className="text-left", style={"margin-top": "20px", "margin-bottom": "20px", "padding-left": "0"}),
                width={"size": 8, "offset": 0},
            ),
        ], className="mt-4 mb-4 g-2", align="center"),
        style={
            "background-image": "url('/assets/images/hero-bg.png')",
            "background-repeat": "no-repeat",
            "background-position": "center center",
            "background-size": "cover",
          #  "background-color": "rgba(255,255,255,0.5)",  # Optional: adds a semi-transparent black overlay
            "background-color": "rgba(0,0,0,0.3)",  # Optional: adds a semi-transparent black overlay

            "background-blend-mode": "overlay",           # Optional: blends image with background color
           # "border-radius": "12px",                      # Optional: rounded corners
            "padding": "0.1rem",                            # Optional: inner padding
            "color": "white",  # <-- Set font color to white
            "text-shadow": "2px 2px 4px rgba(0,0,0,0.8)",
        }
    ),


    # Page Container (for multi-page content)
    html.Div(page_container)
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
