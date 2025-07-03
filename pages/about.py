# pages/home.py
import dash
import random
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import dcc
from dash import html


# List of quotes to rotate
QUOTES = [
    "“Science and everyday life cannot and should not be separated.” – Rosalind Franklin",
    "“Research is to see what everybody else has seen, and to think what nobody else has thought.” – Albert Szent-Györgyi",
    "“You have to go wholeheartedly into anything in order to achieve anything worth having.” – Frank Lloyd Wright",
    "“I know the price of success: dedication, hard work, and an unremitting devotion to the things you want to see happen.” – Frank Lloyd Wright",
    "“The depth of your commitment determines the breadth of your impact.” – William F. Halsey",
    "“Innovation is the ability to see change as an opportunity—not a threat.” – Steve Jobs",
    "“Desire is the key to motivation, but it’s determination and commitment to an unrelenting pursuit of your goal—a commitment to excellence—that will enable you to attain the success you seek.” – Mario Andretti",
    "“Success is not final, failure is not fatal: It is the courage to continue that counts.” – Winston S. Churchill",
    "“The only way to do great work is to love what you do.” – Steve Jobs",
    "“We are what we repeatedly do. Excellence, then, is not an act, but a habit.” – Aristotle ",
    "“I do the very best I know how, the very best I can, and I mean to keep on doing so until the end.” — Abraham Lincoln",
    "“My meaning simply is, that whatever I have tried to do in life, I have tried with all my heart to do well; that whatever I have devoted myself to, I have devoted myself to completely; that in great aims and in small, I have always been thoroughly in earnest.” — David Copperfield (Charles Dickens)",
    #"“Wherever you go, go with all your heart.” – Confucius",
]


lat = 40.610289
lng = -64.628406
zoom = 2.9
url = "https://www.google.com/maps/d/u/3/embed?mid=1BEhCX-JBNWPNmUOOtv6Aj8OgKL53mRo&ehbc=2E312F&ll={lat},{lng}&z={zoom}"
#url = f"https://www.google.com/maps/d/u/0/embed?mid=13WAtu9_3Y8YKHpec44xtdgtMDmrqs4U&ehbc=2E312&ll={lat},{lng}&z={zoom}"

dash.register_page(__name__, path="/", name="About Me", index=True)


def serve_layout():
    # Pick a random quote for each page load
    quote = random.choice(QUOTES)

    return dbc.Container([

    # About Me Card
    dbc.Row(
        dbc.Col(
            html.Div([
                html.H2("About Me", className="mb-3"),
                dcc.Markdown('''
                    I am a computational materials scientist and STEM educator passionate about harnessing high-performance computing, molecular modeling, and machine learning to solve urgent sustainability challenges. 
                    My research centers on the rational design of advanced polymers for circular economy applications, from sustainable plastics to next-generation battery materials.
                        
                    Beyond the lab, I am dedicated to inclusive education, mentorship, and outreach—designing hands-on workshops, developing learner-centered curricula, and leading initiatives that foster diversity and collaboration in STEM. 
                    As a leader and advocate, I have organized international outreach events, mentored emerging researchers, and championed digital innovation in scientific communities.
                    Driven by curiosity and a commitment to real-world impact, I strive to empower the next generation of scientists and engineers to create a more sustainable and equitable future.

                                    ''', className="text-left"),
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
                                    style={'width': '100%', 'height': '400px', 'border': 'none'}
                                ),
                            ]),
                            md=5, sm=12,
                        ),
                        dbc.Col(
                            dcc.Markdown('''
                                #### Education
                                - **Ph.D. Molecular Engineering, University of Chicago (2020 - Expected 2025)**
                                    - *Track:* Materials for Energy and Sustainability
                                    - *Thesis:* Computational Design of Circular Polymers: From Plastics to Batteries     
                                - **B.S. Materials Engineering, Universidad de Sonora, Mexico (2013 - 2018)**
                                    - *Concentration:* Polymer Science and Engineering
                                    - *Thesis:* Synthesis and characterization of a bioconjugate based on oleic acid and L-cysteine

                                #### Research Experience

                                - **Visiting Graduate Researcher**, KU Leuven, Belgium (Jan 2025 - Present)
                                - **Graduate Research Assistant**, University of Chicago (Jan 2021 - Present)
                                - **R&D Intern**, GSE Biomedical (Jan 2018 - Dec 2018)
                                - **Undergraduate Researcher**, Universidad de Sonora (2015 - 2018)
                            '''),
                            md=7, sm=12,
                        )
                    ])
                ]),
                className="custom-card",
                style={"border-radius": "12px", "margin-bottom": "24px", "line-height": "1.8"}
            ), width=12
        )
    ),

    # Technical Skills
    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Markdown('''
                    #### Technical Skills
                    - **Software:** SolidWorks, GROMACS, Clapeyron, Polyply, Dash, Overleaf (LaTeX)
                    - **Programming Languages:** Python, C/C++ (Arduino IDE), JavaScript
                    - **Industrial Automation and Prototyping:** Arduino, Raspberry Pi, PLC, 3D Printing
                    - **Material Characterization:** FTIR and UV-Vis Spectroscopy, Optical Microscopy
                    - **Machine Learning:** Scikit-learn, TensorFlow, Keras
                    - **Data Analysis:** Pandas, NumPy, Matplotlib, Plotly
                    - **Visualization:** Plotly, VMD, Blender
                    - **High Performance Computing:** PBS, Slurm, MPI parallelization, automated workflow development
                ''', className="text-left mt-4"),
            ], className="text-left mt-4"),
            width=12,
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px", "line-height": "1.8"}
    ),

    # Awards and Honors
    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Markdown('''
                    #### Awards and Honors
                    - **Richard Tillman Award for Embodiment of Excellence in Diversity and Inclusion**, *University of Chicago* (Chicago, U.S., 2025)
                    - **Best Oral Presentation**, *Organic Battery Days* (Adelaide, Australia, 2025)
                    - **SHPE Graduate Award**, *Society of Hispanic Professional Engineers* (Chicago, U.S., 2024)
                    - **Best Poster Presentation (Category: Data Science)**, *MindBytes Conference* (Chicago, U.S., 2023)
                    - **Best Poster Award**, *Center for Plastics Innovation (CPI) Annual Meeting* (Delaware, U.S., 2023)
                    - **Fulbright-García Robles Fellowship**, *COMEXUS* (2020 - 2023)
                    - **Engineering Academic Excellence National Award**, *Mexican National Association of Engineering Schools* (Mexico, 2019)
                    - **Student Trajectory Award**, *Universidad de Sonora* (Hermosillo, Mexico, 2018)
                ''', className="text-left mt-4"),
            ], className="text-left mt-4"),
            width=12,
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px", "line-height": "1.8"}
    ),

    # Presentations
    dbc.Row(
        dbc.Col(
            html.Div([
               # html.H4("Presentations"),
               # html.H6([html.U("Contributed oral presentations")]),
                dcc.Markdown('''
                    #### Presentations
                    ##### Contributed Oral Presentations
                    - **Organic Battery Days.** *Hierarchical Modeling of Redox-Active Polymers for All-Organic Batteries*, 2025 (Adelaide, Australia)
                    - **AIChE Annual Meeting.** *Thermophysical Properties of Binary Mixtures of Polyethylene and Higher n-Alkanes*, 2023 (Orlando, U.S.)
                    - **APS March Meeting.** *Thermophysical Properties of Short-Chain Branched Polyethylene*, 2023 (Las Vegas, U.S.)
                             
                    ##### Contributed Poster Presentations
                    - **Frontiers of Molecular Systems Engineering Applied to Societal Problems International Workshop.** *Multiscale Modeling of Phenothiazine-Based Polymers for All-Organic Cathodes*, 2025 (Paris, France)
                    - **Mindbytes Conference for High-Performance Computing.** *Transport Property Prediction of Polyethylene Blends*, 2023 (Chicago, U.S.)
                    - **AIChE Annual Meeting.** *Harnessing Molecular Simulations and Machine Learning to Predict Macromolecular Properties and Drive Efficient Polymer Recycling*, 2023 (Orlando, U.S.)
                                    '''),
            ], className="text-left mt-4"),
            width=12,
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px", "line-height": "1.8"}
    ),

    # Publications
    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Markdown('''
                    #### Publications
                    - Yang, Y., Ma, T., Studer, G., **Ley-Flores, M.**, Alessandri, R., Rowan, S.J., de Pablo, J.J., Esser, B. & Lutkenhaus, J.L. Influence of Anion Solvation on Charge Storage Performance and Mechanism of Poly(phenothiazine) Cathode. (*In Preparation*)
                    - **Ley-Flores, M.**, Chabbi, A., Alessandri, R., Marsden, S., Vettese, I., Rowan, S.J., & de Pablo, J.J. Numerical Study of Cleavable Bond-Modified Polyethylene for Circular Polymer Design. [*arXiv preprint*](https://doi.org/10.48550/arXiv.2404.09341) (*In-Review*)
                    - **Ley-Flores, M.**, Alessandri, R., Najmi, S., Valsecchi, M., Jackson, G., Galindo, A., Korley, L.S., Epps, T.H., Vlachos, D., & de Pablo, J.J. Thermodynamic and Transport Properties of Binary Mixtures of Polyethylene and Higher n-Alkanes from Physics-Informed and Machine-Learned Models. [*arXiv preprint*](https://doi.org/10.48550/arXiv.2404.09676) (*In-Review*)
                    - Vizcarra-Pacheco, M., **Ley-Flores, M.**, Matrecitos-Burruel, A. M., López-Esparza, R., Fernández-Quiroz, D., Lucero-Acuña, A., & Zavala-Rivera, P. (2021). Synthesis and characterization of a bioconjugate based on oleic acid and L-cysteine. *Polymers*, 13(11), 1791.
                                    ''', className="text-left mt-4"),
            ], className="text-left mt-4"),
            width=12,
        ),
        style={"background-color": "#f8f9fa", "padding": "20px", "border-radius": "10px", "margin-bottom": "20px", "line-height": "1.8"}
    ),

], fluid=True)

# Use the function as the layout so it's re-evaluated on each page load
layout = serve_layout