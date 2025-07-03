import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/research", name="Research")

layout = dbc.Container([

    # Research Overview Card
    dbc.Row(
        dbc.Col(
            html.Div([
                html.H2("Research Overview", className="mb-3"),
                dcc.Markdown('''
                    From tackling the global plastics crisis to enabling next-generation energy storage, my research is driven by the urgent need for sustainable materials solutions. 
                    By integrating high-performance computing, molecular simulations, and machine learning, I aim to accelerate the discovery and design of advanced polymers that address real-world environmental challenges. 
                    My work focuses on predicting material properties and developing circular-by-design strategies to close the loop on plastic waste, engineer high-performance polymer blends, and create innovative materials for all-organic batteries.

                    **Key areas of focus include:**

                    - Polymer blends and diffusion modeling
                    - Circular-by-design polymers for sustainable plastics
                    - Polymer-based electrodes for all-organic batteries
                ''', className="text-left mb-3"),
            ], className="text-left"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "24px", "border-radius": "12px", "margin-bottom": "12px"}
    ),
    
    # Row 1 of Projects
    dbc.Row([

        # Project 1
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),
                        html.B("Numerical Simulation of"),
                        html.Br(),
                        html.B("Circular-by-Design Polymers"),
                    ],
                    className="text-center",
                    style={
                        "fontSize": "1.1rem", 
                        "backgroundColor": "#142850", 
                        "color": "white", 
                        "borderRadius": "12px 12px 0 0"}
                ),
                dbc.CardBody([
                    html.Img(
                        src="assets/images/PE-like.png",
                        className="mb-3",
                        style={"width": "98%", "borderRadius": "8px"}
                    ),
                    dcc.Markdown('''
                        Simulated and analyzed a library of 10 polyethylene-like materials featuring cleavable bonds for circular polymer design. Benchmarked against polyethylene thermodynamic, transport and crystallization properties.

                        **Key tools:** GROMACS, GROMOS ATB, Polyply, Python.

                        **Publication:**  Ley-Flores et al. (2025) *[In-Review]* [arXiv preprint arXiv:2404.09341](https://doi.org/10.48550/arXiv.2404.09341).

                        **Poster:**  
                        Best Poster Award, [Center for Plastics Innovation (CPI) Annual Meeting 2023](https://cpi.udel.edu/).
                                            '''),
                    dbc.Button(
                        "Explore the data",
                        href="/circular-polymers",
                        color="primary",
                        className="mt-3"
                    )
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),

        # Project 2
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),
                        html.B("Polyethylene Blends Diffusion Modeling"),
                        html.Br(),
                        html.B("at Extreme Conditions"),
                    ],
                    className="text-center",
                    style={
                        "fontSize": "1.1rem", 
                        "backgroundColor": "#142850", 
                        "color": "white", 
                        "borderRadius": "12px 12px 0 0"}
                ),
                dbc.CardBody([
                    html.Img(
                        src="assets/images/binary_blend.png",
                        className="mb-3",
                        style={"width": "100%", "borderRadius": "8px"}
                    ),
                    dcc.Markdown('''
                        Developed a model to predict diffusion coefficients based on temperature, pressure, oligomer length and blend concentration.

                        **Key tools:** GROMACS, GROMOS ATB, Python, TensorFlow.

                        **Publication:**  Ley-Flores et al. (2025) *[In-Review]* [arXiv preprint arXiv:2404.09676](https://doi.org/10.48550/arXiv.2404.09676).  
                                 
                        **Poster:**  
                        Best Poster Presentation, [MindBytes Conference for High Performance Computing 2023](https://legacy.mindbytes.rcc.uchicago.edu/2023/).
                                            '''),
                    dbc.Button(
                        "Applet Coming Soon",
                        color="secondary",
                        className="mt-3"
                    )
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),

        # Project 3
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),
                        html.B("Thermodynamic Properties of Polymer Blends"),
                        html.Br(),
                        html.B("Under Catalytic Recycling Conditions"),
                    ],
                    className="text-center",
                    style={
                        "fontSize": "1.1rem", 
                        "backgroundColor": "#142850", 
                        "color": "white", 
                        "borderRadius": "12px 12px 0 0"}
                ),
                dbc.CardBody([
                    html.Img(
                        src="assets/images/PE_SAFT_density.gif",
                        className="mb-3",
                        style={"width": "100%", "borderRadius": "8px"}
                    ),
                    dcc.Markdown('''
                        Developed a model to predict diffusion coefficients based on temperature, pressure, oligomer length and blend concentration.

                        **Key tools:** SAFT-γ Mie EoS, Clapeyron, Python.

                        **Publication:**  Kots et al. (2025) Impact of small-alkane solvents on polyolefin hydrogenolysis over ruthenium catalyst. *Submitted*.
                                 
                                            '''),
                    dbc.Button(
                        "Applet Coming Soon",
                        color="secondary",
                        className="mt-3"
                    )
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),
    ]),

    # Row 2 of Projects
    dbc.Row([

        # Project 4
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),
                        html.B("Design of Phenothiazine-based"),
                        html.Br(),
                        html.B("Polymers for All-Organic Cathodes"),
                    ],
                    className="text-center",
                    style={
                        "fontSize": "1.1rem", 
                        "backgroundColor": "#142850", 
                        "color": "white", 
                        "borderRadius": "12px 12px 0 0"}
                ),
                dbc.CardBody([
                    html.Img(
                        src="assets/videos/redox_polymer.gif",
                        className="mb-3",
                        style={
                            "width": "63.5%", 
                            "borderRadius": "8px", 
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto"}
                    ),
                    dcc.Markdown('''
                        Simulated and benchmarked a library of 6 phenothiazine-based polymers for its potential as cathode materials for all-organic batteries.

                        **Key tools:** Gaussian, GROMACS, LigParGen, Polyply, MDAnalysis.

                        **Publication:**  
                        Yang, Y., Ma, T., Studer, G., **Ley-Flores, M.**, et al (2025) (*In Preparation*)

                        **Oral Contribution:**  
                        Best Oral Presentation, [Organic Battery Days 2025](https://www.obd2025.com.au/).
                                            '''),
                    dbc.Button(
                        "Applet Coming Soon",
                        color="secondary",
                        className="mt-3"
                    )
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),

        # Undergrad Thesis
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),
                        html.B("Synthesis and Characterization of"),
                        html.Br(),
                        html.B("Amphiphilic Molecules Based on L-Cysteine"),
                    ],
                    className="text-center",
                    style={
                        "fontSize": "1.1rem", 
                        "backgroundColor": "#142850", 
                        "color": "white", 
                        "borderRadius": "12px 12px 0 0"}
                ),
                dbc.CardBody([
                    html.Img(
                        src="assets/images/thesis_undergrad.png",
                        className="mb-3",
                        style={
                            "width": "81%", 
                            "borderRadius": "8px", 
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto"},
                    ),
                    dcc.Markdown('''
                        Developed a model to predict diffusion coefficients based on temperature, pressure, oligomer length and blend concentration.

                        **Key tools:** FTIR, UV-Vis and Raman Spectroscopy, Nuclear Magnetic Resonance, Dynamic Light Scattering.

                        **Publication:**  
                        Vizcarra-Pacheco, M., **Ley-Flores, M.**, Matrecitos-Burruel, A. M., López-Esparza, R., Fernández-Quiroz, D., Lucero-Acuña, A., & Zavala-Rivera, P. (2021). Synthesis and characterization of a bioconjugate based on oleic acid and L-cysteine. *Polymers*, 13(11), 1791. [DOI:10.3390/polym13111791](https://doi.org/10.3390/polym13111791).
                                            ''')
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),
        
    ]),
    
    # Skills Section
    html.H3("Technical Expertise", className="mt-5 mb-4"),
    dbc.Row([
        dbc.Col(
            dbc.ListGroup([
                dbc.ListGroupItem("Quantum Chemistry (Gaussian)"),
                dbc.ListGroupItem("Molecular Dynamics (GROMACS)"),
                dbc.ListGroupItem("Machine Learning (TensorFlow)"),
            ], flush=True),
            md=4
        ),
        dbc.Col(
            dbc.ListGroup([
                dbc.ListGroupItem("Topology Automation (Polyply)"),
                dbc.ListGroupItem("Molecular Visualization (VMD, Blender)"),
                dbc.ListGroupItem("SAFT-γ Mie EoS"),
            ], flush=True),
            md=4
        ),
        dbc.Col(
            dbc.ListGroup([
                dbc.ListGroupItem("High-Performance Computing (PBS, Slurm)"),
                dbc.ListGroupItem("Python Scientific Stack (Numpy, Pandas, Matplotlib)"),
                dbc.ListGroupItem("Version Control (Git)"),
            ], flush=True),
            md=4
        ),
    ], className="mb-5")

], fluid=True)
