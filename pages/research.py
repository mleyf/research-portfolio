import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

# Example dummy data: diffusion coefficient vs. concentration
dummy_data = pd.DataFrame({
    "Concentration (%)": [10, 20, 30, 40, 50],
    "Diffusion Coefficient (m²/s)": [2.1e-9, 1.7e-9, 1.5e-9, 1.3e-9, 0.8e-9]
})

# Create the plot
fig = px.line(
    dummy_data,
    x="Concentration (%)",
    y="Diffusion Coefficient (m²/s)",
    title="Diffusion Coefficient vs. Concentration",
    labels={"Concentration (%)": "Concentration (%)", "Diffusion Coefficient (m²/s)": "Diffusion Coefficient (m²/s)"}
)

# Optional: Customize the plot
fig.update_layout(
    height=300,
    margin={"l": 40, "r": 40, "t": 40, "b": 40}
)



dash.register_page(__name__, path="/research", name="Research")

layout = dbc.Container([
    html.H2("Research Overview", className="mt-4 mb-4"),
    html.P("My research explores the intersection of materials modeling, machine learning, and polymer informatics, with a focus on sustainable energy solutions. I use advanced simulation techniques and data-driven approaches to predict material properties and enable rational design of polymer materials for circular economy applications."),

    # Project 1
    dbc.Card([
        dbc.CardHeader("Numerical Study of Polymer Blends for Catalytic Recycling of Plastics"),
        dbc.CardBody([
            html.P("Investigated the diffusion of polyethylene binary mixtures through Statistical Associating Fluid Theory (SAFT), high-throughput molecular simulations and machine learning."),
            html.P(["Key tools: ", html.B("SAFT-γ Mie EoS, GROMACS, Python, Tensorflow"), "."]),
            html.P("Developed a model to predict diffusion coefficients based on temperature, pressure, oligomer length and blend concentration."),
            
            
            # Two columns: Video and Plot
            dbc.Row([
                dbc.Col(
                    html.Div([
                        html.Img(
                            src="assets/images/binary_mixtures.png",  # Update path as needed
                            style={"width": "80%", "border-radius": "8px"}
                        )
                    ]),
                    width=6
                ),
                dbc.Col(
                    html.Div([
                        html.H5("Diffusion Coefficient vs. Concentration", className="mt-3 mb-2"),
                        dcc.Graph(
                            id='diffusion-plot',
                            figure=fig,  # Replace with your actual figure
                            style={"width": "100%", "height": "300px"}
                        )
                    ]),
                    width=6
                ),
            ], className="mt-4"),


            ##### Publicatios and Posters #####            
            html.P([
                "Publication: Ley-Flores et al. (2025) ",
                html.I("[In-Review] "),
                html.A("arXiv preprint arXiv:2404.09676", href="https://doi.org/10.48550/arXiv.2404.09676", target="_blank"),
                "."
            ]),

            html.P([
                "Poster: Best Poster Presentation, ",
                html.A("MindBytes Conference 2023", href="https://legacy.mindbytes.rcc.uchicago.edu/2023/", target="_blank"),
                "."
            ])
        ])
    ], className="mb-4"),


    # Project 2
    dbc.Card([
        dbc.CardHeader("Circular-by-Design Polymers for Sustainable Plastics"),
        dbc.CardBody([
            html.P("Simulated, analyzed and benchmarked a library of 10 polyethylene-like materials featuring cleavable bonds for circular polymer design using molecular dynamics simulations, and automated topology builders."),
            html.P(["Key tools: ", html.B("GROMACS, LigParGen, Polyply, Python"), "."]),
            html.P("Analyzed thermodynamic, transport and crystallization properties of the materials."),
            #dcc.Graph(figure=another_plotly_figure),
            html.P([
                "Publication: Ley-Flores et al. (2025) ",
                html.I("[In-Review] "),
                html.A("arXiv preprint arXiv:2404.09341", href="https://doi.org/10.48550/arXiv.2404.09341", target="_blank"),
                "."
            ]),
            html.P([
                "Poster: Best Poster Award, ",
                html.A("Center for Plastics Innovation (CPI) Annual Meeting 2023", href="https://cpi.udel.edu/", target="_blank"),
                "."
            ]),
        ])
    ], className="mb-4"),

    # Project 3
    dbc.Card([
        dbc.CardHeader("Phenothiazine-Based Polymers for Organic Batteries"),
        dbc.CardBody([
            html.P("Simulated and analyzed a library of 6 phenothiazine-based polymers for organic battery applications using molecular dynamics simulations and quantum chemistry calculations."),
            html.P(["Key tools: ", html.B("Gaussian, GROMACS, LigParGen, Polyply, Python"), "."]),
            html.P("Analyzed swelling behavior and state-of-charge effects on polymer properties."),
            #dcc.Graph(figure=another_plotly_figure),
            html.P([
                "Oral Contribution: Best Oral Presentation, ",
                html.A("Organic Battery Days 2025", href="https://www.obd2025.com.au/", target="_blank"),
                "."
            ]),

        ])
    ], className="mb-4"),


    # Skills/Tools Section
    html.H3("Skills and Tools", className="mt-4 mb-3"),
    dbc.ListGroup([
        dbc.ListGroupItem("Quantum Chemistry (Gaussian)"),
        dbc.ListGroupItem("Molecular Dynamics Simulation (GROMACS)"),
        dbc.ListGroupItem("Machine Learning (TensorFlow, scikit-learn)"),
        dbc.ListGroupItem("Topology Automation (LigParGen, Polyply)"),
        dbc.ListGroupItem("Data Analysis and Visualization (Python, Pandas, Matplotlib)"),
        dbc.ListGroupItem("Thermodynamic Property Calculation (SAFT-γ Mie Equation of State)"),
        dbc.ListGroupItem("Molecular Visualization (VMD)"),
    ], className="mb-4"),
], fluid=True)
