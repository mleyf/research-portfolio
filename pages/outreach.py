import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/outreach", name="Outreach")

layout = dbc.Container([

    # Overview Card
    dbc.Row(
        dbc.Col(
            html.Div([
                html.H2("Outreach and Volunteering", className="mb-3"),
                dcc.Markdown('''
                    My commitment to outreach is deeply rooted in the belief that **STEM should be accessible, welcoming, and inspiring for everyone**—especially those from communities that have historically been underrepresented in science and engineering.
                    As a woman in STEM, I have experienced firsthand the challenges that come with navigating spaces where role models and mentors can be scarce. 
                    I am passionate about designing and leading initiatives that not only demystify STEM, but also make it genuinely exciting and approachable. 
                    By reaching out to students who may not have access to mentors or role models in these fields, I strive to bridge gaps of social injustice and open doors that might otherwise remain closed. 
                    
                    **I believe that increasing diversity in STEM is not just a matter of equity—it is essential for innovation.** When we bring together people with different backgrounds and perspectives, we gain new insights and creative solutions to the world’s most pressing challenges. 
                    Through my outreach and volunteering efforts, I am dedicated to building a more inclusive STEM community where every aspiring scientist and engineer feels empowered to contribute and succeed.                    
                ''', className="text-left mb-3"),
            ], className="text-left"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "24px", "border-radius": "12px", "margin-bottom": "12px"}
    ),
    
    # Row of Outreach Experiences
    dbc.Row([
        # Clubes de Ciencia
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),
                        html.B("Co-Instructor at"),
                        html.Br(),
                        html.B("Clubes de Ciencia Mexico"),
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
                        src="assets/images/clubes_de_ciencia_recuerdito.jpg",
                        className="mb-3",
                        style={
                            "width": "92%", 
                            "borderRadius": "8px", 
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto"}
                    ),
                    dcc.Markdown('''
                        As a co-instructor at Clubes de Ciencia Mexico, I played a key role in mentoring students and leading hands-on workshops focused on STEM topics.

                        **Key Achievements:**
                        - Organized workshops and networking events to promote STEM careers among Hispanic students.
                        - Led a team of 8 members to increase workshop participation.
                        - Helped students develop practical skills and confidence in science and engineering.

                        Learn more about our workshop at [Clubes de Ciencia MX](https://minimoocs.clubesdeciencia.mx/courses/learning-machine-polimeros/).
                                            ''')
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),
        
        # Día de Ciencias
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),
                        html.B("Organizer of SHPE Chicagoland"),
                        html.Br(),
                        html.B("Día de Ciencias"),
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
                        src="assets/images/dia_de_ciencias_leader-2-2.jpg",
                        className="mb-3",
                        style={
                            "width": "92%", 
                            "borderRadius": "8px", 
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto"}
                    ),
                    dcc.Markdown('''
                        As the organizer of SHPE Chicagoland Día de Ciencias, I coordinated outreach events to inspire young students from underrepresented communities to pursue careers in STEM.

                        **Key Achievements:**
                        - Organized professional development workshops for students and early career researchers.
                        - Advocated for accessibility and inclusion in STEM outreach programs.
                        - Contributed to the development of initiatives to support underrepresented groups.

                        Read more about the impact of this event in [this article](https://pme.uchicago.edu/news/dia-de-ciencias-spurs-passion-stem) from the University of Chicago.
                                            ''')
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),

        # South Side Science Festival
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),
                        html.B("Science Promoter at"),
                        html.Br(),
                        html.B("South Side Science Festival"),
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
                        src="assets/images/SSSF_1-2.jpg",
                        className="mb-3",
                        style={
                            "width": "92%", 
                            "borderRadius": "8px", 
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto"}
                    ),
                    dcc.Markdown('''
                        As a science promoter at the South Side Science Festival, I engaged with the local community by organizing interactive science demonstrations and educational activities.

                        **Key Achievements:**
                        - Developed and delivered hands-on science workshops for children and families.
                        - Collaborated with local schools and organizations to maximize outreach impact.
                        - Inspired curiosity and enthusiasm for science in the local community.
                                            ''')
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),
    ]),
], fluid=True)
