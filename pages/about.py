# pages/home.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import dcc
from dash import html



lat = 40.610289
lng = -64.628406
zoom = 2.9
url = "https://www.google.com/maps/d/u/3/embed?mid=1BEhCX-JBNWPNmUOOtv6Aj8OgKL53mRo&ehbc=2E312F&ll={lat},{lng}&z={zoom}"
#url = f"https://www.google.com/maps/d/u/0/embed?mid=13WAtu9_3Y8YKHpec44xtdgtMDmrqs4U&ehbc=2E312&ll={lat},{lng}&z={zoom}"

dash.register_page(__name__, path="/about", name="About Me", index=True)


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
                    dbc.Row([

                        dbc.Col(
                            html.Div([
                                html.Iframe(
                                    src=url,
                                    style={'width': '100%', 'height': '500px', 'border': 'none'}
                                ),
                            ]),
                            width=4
                        ),

                        dbc.Col([
                            html.H4("Education", className="mb-3"),
                            html.Ul([

                                html.Li([
                                        html.B("Ph.D. Molecular Engineering, University of Chicago (2020 - Expected 2025)"),
                                        html.Ul([
                                            html.Li([html.B("Track: "), "Materials for Energy and Sustainability"]),
                                            html.Li([html.B("Thesis: "),"Computational Design of Circular Polymers: From Plastics to Batteries"]),
                                            ])
                                        ]),

                                html.Li([
                                        html.B("B.S. Materials Engineering, Universidad de Sonora, Mexico (2013 - 2018)"),
                                        html.Ul([
                                            html.Li([html.B("Concentration: "),"Polymer Science and Engineering"]),
                                            html.Li([html.B("Thesis: "), "Synthesis and characterization of a bioconjugate based on oleic acid and L-cysteine"]),                                            ])
                                        ]),


                            ]),
                            html.H4("Research Experience", className="mb-2 mt-3"),
                            html.Ul([
                                html.Li([html.B("Visiting Graduate Researcher"), ", KU Leuven, Belgium (Jan 2025 - Present)"]),
                                html.Li([html.B("Graduate Research Assistant"), ", University of Chicago (Jan 2021 - Present)"]),
                                html.Li([html.B("Materials Research Intern"), ", GSE Biomedical (Jan 2018 - Dec 2018)"]),
                                html.Li([html.B("Undergraduate Researcher"), ", Universidad de Sonora (2015 - 2018)"]),
                            ]),
                        ], width=8)
                    ])
                ]),
                className="shadow-sm",
                style={"border-radius": "12px", "margin-bottom": "24px", "line-height": "1.8",}
            ), width=12
        )
    ),


    dbc.Row(
        dbc.Col(
            html.Div([
                html.H4("Skills"),
                html.Ul([
                    html.Li([html.B("Software: "),"GROMACS, LAMMPS, Polyply, Gaussian, Dash, Overleaf (LaTeX)"]),
                    html.Li([html.B("Programming Languages: "),"Python, R, JavaScript"]),
                    html.Li([html.B("Machine Learning: "), "Scikit-learn, TensorFlow, Keras"]),
                    html.Li([html.B("Data Analysis: "),"Pandas, NumPy, Matplotlib, Plotly"]),
                    html.Li([html.B("Languages: "),"Spanish (Native), English (Professional Proficiency), French (Intermediate)"]),
                ]),

            ], className="text-left mt-4"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px", "line-height": "1.8",}
    ),


    dbc.Row(
        dbc.Col(
            html.Div([

                html.H4("Awards and Honors"),
                html.Ul([
                    html.Li(["Best Oral Presentation, ", html.I("Organic Battery Days"),"(2025)"]),
                    html.Li(["SHPE Graduate Award, ", html.I("Society of Hispanic Professional Engineers "), "(2024)"]),
                    html.Li(["Fulbright-García Robles Fellowship ", html.I("COMEXUS "),"(2020 - 2023)"]),
                    html.Li(["Best Poster Presentation, ", html.I("MindBytes Conference "),  "(2023)"]),
                ]),

            ], className="text-left mt-4"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px", "line-height": "1.8",}
    ),

    dbc.Row(
        dbc.Col(
            html.Div([
                html.H4("Presentations"),
                html.H6([html.U("Contributed oral presentations")]),
                html.Ul([
                    html.Li([html.B("Organic Battery Days. "), html.I("Hierarchical Modeling of Redox-Active Polymers for All-Organic Batteries"), ", 2025 (Adelaide, Australia)"]),
                    html.Li([html.B("AIChE Annual Meeting. "), html.I("Thermophysical Properties of Binary Mixtures of Polyethylene and Higher n-Alkanes"),", 2023 (Orlando, U.S.)"]),
                    html.Li([html.B("APS March Meeting. "), html.I("Thermophysical Properties of Short-Chain Branched Polyethylene"), ", 2023 (Las Vegas, U.S.)"]),
                ]),

                
                html.H6([html.U("Contributed poster presentations")]),
                html.Ul([
                    html.Li([html.B("Frontiers of Molecular Engineering. "), html.I("Multiscale Modeling of Phenothiazine-Based Cathodes for All-Organic Batteries"), ", 2025 (Paris, France)"]),
                    html.Li([html.B("Mindbytes Conference for High-Performance Computing. "), html.I("Transport Property Prediction of Polyethylene Blends"),", 2023 (Chicago, U.S.)"]),
                    html.Li([html.B("AIChE Annual Meeting. "), html.I("Harnessing Molecular Simulations and Machine Learning to Predict Macromolecular Properties and Drive Efficient Polymer Recycling"),", 2023 (Orlando, U.S.)"]),

                ]),

            ], className="text-left mt-4"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px", "line-height": "1.8",}
    ),

    dbc.Row(
        dbc.Col(
            html.Div([
                html.H4("Publications"),
                html.Ul([
                    html.Li([html.B("Ley-Flores, M."),", Alessandri, R., Marsden, S., Vettese, I., Rowan, S.J., & de Pablo, J.J. Crystallization of Circular-by-Design Polyethylene-like Materials. [", html.I("In-Preparation"),"]"]),
                    html.Li(["Yang, Y., Ma, T., Studer, G.,", html.B("Ley-Flores, M."),", Alessandri, R., Rowan, S.J., de Pablo, J.J., Esser, B. & Lutkenhaus, J.L. Influence of Anion Solvation on Charge Storage Performance and Mechanism of Poly(phenothiazine) Cathode. [", html.I("Submitted"),"]"]),
                    html.Li([html.B("Ley-Flores, M."),", Chabbi, A., Alessandri, R., Marsden, S., Vettese, I., Rowan, S.J., & de Pablo, J.J. (2024). Numerical Study of Cleavable Bond-Modified Polyethylene for Circular Polymer Design. ", html.I(["arXiv preprint ", html.A("arXiv:2404.09341 ", href="https://doi.org/10.48550/arXiv.2404.09341", target="_blank")]),"[", html.I("In-Review"),"]"]),
                    html.Li([html.B("Ley-Flores, M."),", Alessandri, R., Najmi, S., Valsecchi, M., Jackson, G., Galindo, A., Korley, L.S., Epps, T.H., Vlachos, D., & de Pablo, J.J. (2024). Thermodynamic and Transport Properties of Binary Mixtures of Polyethylene and Higher n-Alkanes from Physics-Informed and Machine-Learned Models. ", html.I(["arXiv preprint ", html.A("arXiv:2404.09676 ", href="https://doi.org/10.48550/arXiv.2404.09676", target="_blank")]),"[", html.I("In-Review"),"]"]),
                    html.Li(["Vizcarra-Pacheco, M., ", html.B("Ley-Flores, M."),", Matrecitos-Burruel, A. M., López-Esparza, R., Fernández-Quiroz, D., Lucero-Acuña, A., & Zavala-Rivera, P. (2021). Synthesis and characterization of a bioconjugate based on oleic acid and L-cysteine. ", html.I("Polymers"), ", 13(11), 1791."]),
                ]),
            ], className="text-left mt-4"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px", "line-height": "1.8",}
    ),

   ], fluid=True)
