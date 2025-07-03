import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/teaching", name="Teaching")

import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/teaching", name="Teaching")

layout = dbc.Container([

    # Teaching and Mentorship Overview Card
    dbc.Row(
        dbc.Col(
            html.Div([
                html.H2("Teaching and Mentorship", className="mb-3"),
                dcc.Markdown('''
                             
                    Born in Mexico on Teacher’s Day (May 15th), I discovered early that this serendipitous timing would prove prophetic. My father, a dedicated educator and my very first mentor, inspired me from a young age with his passion for teaching and his ability to change lives. Following his example, I have become deeply committed to the idea that education is the most powerful catalyst for positive change in the world—a belief that continues to drive my work as an educator, tutor, and mentor in STEM.
                                                 
                    Throughout my career, I have embraced every opportunity to share knowledge and inspire the next generation of researchers and innovators. My approach combines rigorous academic standards with genuine care for student success, creating an environment where complex concepts become accessible and learning becomes an exciting discovery process.
                    Whether working one-on-one with struggling students or leading advanced research discussions, I bring the same level of enthusiasm and dedication that my father modeled for me. Each teaching interaction is an opportunity to not only transfer knowledge but to spark curiosity, build confidence, and empower students to reach their full potential.
                    
                    **My teaching philosophy centers on making science and engineering both comprehensible and compelling, ensuring that every student—regardless of their starting point—can engage meaningfully with these crucial fields that shape our future.**                                                
                                    ''', className="text-left mb-3"),
            ], className="text-left"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "24px", "border-radius": "12px", "margin-bottom": "12px"}
    ),
    
    # Row of Teaching and Mentorship Experience
    dbc.Row([
        # Teaching Assistant at UChicago
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),
                        html.B("Thermodynamics and Statistical Mechanics"),
                        html.Br(),
                        html.B("Teaching Assistant at UChicago"),
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
                        src="assets/images/uchicago.png",
                        className="mb-3",
                        style={
                            "width": "40%", 
                            "borderRadius": "8px", 
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto"}
                    ),
                    dcc.Markdown('''
                        As a Teaching Assistant for Thermodynamics and Statistical Mechanics at the University of Chicago, I led discussion sections, designed problem sets, and provided one-on-one support to undergraduate and graduate students.

                        **Key Responsibilities:**
                        - Facilitated weekly discussion sections and office hours
                        - Graded assignments and exams
                        - Provided mentorship and academic support to students
                        - Assisted in developing course materials and resources
                                            ''')
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),
        
        # REU Mentor at UChicago
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),
                        html.B("Research Experiences for Undergraduates (REU)"),
                        html.Br(),
                        html.B("Mentor at UChicago"),
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
                        src="assets/images/REU_mentorship.jpg",
                        className="mb-3",
                        style={
                            "width": "95%", 
                            "borderRadius": "8px", 
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto"}
                    ),
                    dcc.Markdown('''
                        As a mentor for the Research Experiences for Undergraduates (REU) program at the University of Chicago, I guided two students through their research projects, helping them develop essential research, analytical, and communication skills.

                        **Key Achievements:**
                        - Provided hands-on guidance in experimental and computational research
                        - Organized weekly meetings to discuss progress and challenges
                        - Supported students in preparing presentations and reports
                        - Helped students develop professional and academic skills
                    ''')
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),

        # Tecmilenio Curricular Instructor
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),
                        html.B("Curricular Instructor for"),
                        html.Br(),
                        html.B("Mathematical Models at Universidad Tecmilenio"),
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
                        src="assets/images/tecmi-logo-cuadrado.png",
                        className="mb-3",
                        style={
                            "width": "60%", 
                            "borderRadius": "8px", 
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto"}
                    ),
                    dcc.Markdown('''
                        As the curricular instructor for Mathematical Models at Universidad Tecmilenio, I designed and delivered a course focused on mathematical modeling for high school students.

                        **Key Responsibilities:**
                        - Developed course curriculum and materials
                        - Delivered lectures and interactive sessions
                        - Guided students through hands-on modeling projects
                        - Provided individualized support and feedback
                                            ''')
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),
    ]),

], fluid=True)
