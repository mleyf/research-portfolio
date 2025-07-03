# app.py
from dash import Dash, html, page_container, dcc
import dash_bootstrap_components as dbc

from dash import Input, Output, callback

from dash import html
import dash_bootstrap_components as dbc


app = Dash(__name__, suppress_callback_exceptions=True, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


app.layout = dbc.Container([

    # Custom Navbar with Container for alignment
    dbc.Navbar(
        dbc.Container([
            dbc.NavbarBrand("Personal Website", href="/", className="ps-4"),
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("About", href="/")),
                dbc.NavItem(dbc.NavLink("Research", href="/research")),
                #dbc.NavItem(dbc.NavLink("Engineering", href="/engineering")),
                #dbc.NavItem(dbc.NavLink("Tutorials", href="/tutorials")),
                dbc.NavItem(dbc.NavLink("Leadership", href="/leadership")),
                dbc.NavItem(dbc.NavLink("Teaching", href="/teaching")),
                dbc.NavItem(dbc.NavLink("Outreach", href="/outreach")),
                dbc.NavItem(dbc.NavLink("Values", href="/values")),
                dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
            ], className="ms-auto", navbar=True),
        ], fluid=True),  # fluid=True to match your page's container
        color="#142850",
        dark=True,
        sticky="top",
    ),

    # Hero Section with Background Image
    html.Div(
        dbc.Row([
            # Left Column: Photo
            dbc.Col(
                html.Div([
                    html.Img(
                        src="assets/images/profile_picture.jpeg",
                        style={
                            "width": "180px",
                            "max-width": "100%",
                            "border-radius": "80%",
                            "margin": "20px auto",
                            "margin-left": "auto",
                            "display": "block",
                        }
                    )
                ]),
                md=3, sm=12,  # Stack on mobile, side-by-side on desktop
            ),
            # Right Column: Info
            dbc.Col(
                html.Div([
                    html.H2("María Ley Flores"),
                    html.H1("Computational Polymer Engineer"),
                    html.H5(
                        "Designing next-generation sustainable materials from the molecular level",
                        style={"color": "skyblue"}
                    ),
                ], className="text-left", style={"margin-top": "20px", "margin-bottom": "20px", "padding-left": "0"}),
                md=8, sm=12,  # Stack on mobile, side-by-side on desktop
            ),
        ], className="mt-4 mb-4 g-2", align="center"),
        style={
            "background-image": "url('/assets/images/hero-bg.png')",
            "background-repeat": "no-repeat",
            "background-position": "center center",
            "background-size": "cover",
            "background-color": "rgba(0,0,0,0.3)",
            "background-blend-mode": "overlay",
            "padding": "1rem",
            "color": "white",
            "text-shadow": "2px 2px 4px rgba(0,0,0,0.8)",
        }
    ),

    # Page Container (for multi-page content)
    html.Div(page_container),

], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
