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
            dbc.NavItem(dbc.NavLink("Hobbies", href="#leadership")),  
            dbc.NavItem(dbc.NavLink("Contact", href="#contact")),  
        ],  
        brand="Maria Ley Flores, PhD Candidate",  
        brand_href="#",  
        sticky="top",  
        color="primary",  
        dark=True  
    ),  

    # Hero Section  
    dbc.Row(  
        dbc.Col(  
            html.Div([  
                html.H1("Polymer Physicist & Computational Researcher"),  
                html.P("PhD candidate at the University of Chicago specializing in polymer simulations, machine learning, and sustainable energy materials."),  
                dbc.Button("Download CV", color="primary", className="me-2"),  
                dbc.Button("GitHub", color="secondary", href="https://github.com/mleyf"),  
            ], className="text-center mt-5"),  
            width=12  
        )  
    ),  
], fluid=True)  



############# INTERACTIVE PLOT EXAMPLE ###############

import plotly.express as px  

# Sample data  
df = pd.DataFrame({  
    "Concentration (%)": [10, 30, 50],  
    "Diffusion Coefficient (m²/s)": [2.1e-9, 1.5e-9, 0.8e-9]  
})  

fig = px.line(df, x="Concentration (%)", y="Diffusion Coefficient (m²/s)", title="Diffusion vs. Concentration")  

app.layout += dbc.Row([  
    dbc.Col(dcc.Graph(figure=fig), width=8)  
])  


############# LEADERSHIP CARD ###############

leadership_card = dbc.Card([  
    dbc.CardHeader("Leadership"),  
    dbc.CardBody([  
        html.H5("Society of Hispanic Professional Engineers (SHPE)"),  
        html.P("President | Organized Chicagoland Día de Ciencias (500+ attendees)."),  
        html.Hr(),  
        html.H5("MRSEC Grad Student Advisory Committee"),  
        html.P("Advocated for inclusive policies and outreach programs."),  
    ])  
])  

app.layout += dbc.Row(dbc.Col(leadership_card, width=8), className="mt-4")  



############# CONTACT CARD ###############

contact_form = dbc.Card([  
    dbc.CardHeader("Get in Touch"),  
    dbc.CardBody([  
        dbc.Input(type="email", placeholder="Your email", className="mb-2"),  
        dbc.Textarea(placeholder="Message", className="mb-2"),  
        dbc.Button("Send", color="primary"),  
    ])  
])  

app.layout += dbc.Row(dbc.Col(contact_form, width=6), className="mt-4")  
