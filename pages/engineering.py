import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/engineering", name="Engineering")

layout = dbc.Container([

    # Research Overview Card
    dbc.Row(
        dbc.Col(
            html.Div([
                html.H2("Engineering Projects", className="mb-3"),
                dcc.Markdown('''
                    My work combines high-performance computing, molecular simulations and machine learning to develop innovative solutions for pressing sustainability challenges. I use advanced simulation techniques and data-driven approaches to predict material properties and enable rational design of polymers for circular economy applications.

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
                        html.B("Ultrasonic Spray Deposition of Drug-Eluting"),
                        html.Br(),
                        html.B("Polymer Coatings for Coronary Stents"),
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
                        src="assets/images/gse-biomedical-project.png",
                        className="mb-3",
                        style={
                            "width": "90%", 
                            "borderRadius": "8px", 
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto"}
                    ),
                    dcc.Markdown('''
                        Simulated and analyzed a library of 10 polyethylene-like materials featuring cleavable bonds for circular polymer design. Benchmarked against polyethylene thermodynamic, transport and crystallization properties.

                        **Key tools:** Optical Microscopy, FTIR and UV-Vis Spectroscopy, Ultrasonic Spray Deposition.
                                            ''')
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
                        html.B("Circular-by-Design Polymers"),
                        html.Br(),
                        html.B("for Sustainable Plastics"),
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

                        **Publication:**  
                        Ley-Flores et al. (2025) *[In-Review]* [arXiv preprint arXiv:2404.09341](https://doi.org/10.48550/arXiv.2404.09341).

                        **Poster:**  
                        Best Poster Award, [Center for Plastics Innovation (CPI) Annual Meeting 2023](https://cpi.udel.edu/).
                                            '''),
                    dbc.Button(
                        "Explore the data",
                        href="/project2",
                        color="primary",
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
                        html.B("Non-Conjugated Redox-Active Polymers"),
                        html.Br(),
                        html.B("for All-Organic Batteries"),
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
                        Yang, Y., Ma, T., Studer, G., **Ley-Flores, M.**, et al (2025) *[Submitted]*

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
    ]),
    
    # Skills Section
    html.H3("Technical Expertise", className="mt-5 mb-4"),
    dbc.Row([
        dbc.Col(
            dbc.ListGroup([
                dbc.ListGroupItem("Raspberry Pi"),
                dbc.ListGroupItem("C/C++ (Arduino IDE)"),
                dbc.ListGroupItem("--"),
            ], flush=True),
            md=4
        ),
        dbc.Col(
            dbc.ListGroup([
                dbc.ListGroupItem("SolidWorks"),
                dbc.ListGroupItem("3D Printing"),
                dbc.ListGroupItem("--"),
            ], flush=True),
            md=4
        ),
        dbc.Col(
            dbc.ListGroup([
                dbc.ListGroupItem("Industrial Automation"),
                dbc.ListGroupItem("PLC Programming"),
                dbc.ListGroupItem("--"),
            ], flush=True),
            md=4
        ),
    ], className="mb-5")

], fluid=True)
