import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/leadership", name="Leadership")

layout = dbc.Container([

    # Research Overview Card
    dbc.Row(
        dbc.Col(
            html.Div([
                html.H2("Leadership Roles and Contributions", className="mb-3"),
                dcc.Markdown('''

                    Stepping into leadership has been one of the most transformative experiences of my career. 
                    Each role has strengthened my confidence, honed my decision-making skills, and expanded my capacity to effect positive change in both research and outreach. 
                    I lead by putting my teammates’ growth and well-being first, welcoming their ideas and fostering a sense of shared ownership. 
                    Coupled with a highly organized, analytical, and detail-oriented approach, I ensure that our projects are inclusive, impactful and well-structured.
                                    
                    I believe that leadership in STEM matters now more than ever. 
                    We need researchers at the forefront—shaping policies, guiding institutions, and advocating solutions grounded in evidence and rigorous inquiry. 
                    When scientists step into decision-making roles, we bring a commitment to data-driven approaches, a respect for diverse perspectives, and the courage to challenge assumptions. 
                    I am convinced that anyone willing to speak up and listen can cultivate the skills to lead with empathy and vision—and that together, we can build a future where innovation and equity go hand in hand.

                ''', className="text-left mb-3"),
            ], className="text-left"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "24px", "border-radius": "12px", "margin-bottom": "12px"}
    ),
    
    # Row 1 of Leadership Roles
    dbc.Row([
        # President SHPE
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),  # Bootstrap Icons
                        html.B("Elected President of the"),
                        html.Br(),
                        html.B("Society of Hispanic Professional Engineers (SHPE)"),
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
                        src="assets/images/SHPE Logo.webp",
                        className="mb-3",
                        style={"width": "87%", "borderRadius": "8px", "padding": "1rem", "align": "center"}
                    ),
                    dcc.Markdown('''
                        As the 2024 elected president of the SHPE chapter at the University of Chicago, I led initiatives to promote STEM careers among Hispanic students, organized workshops, and facilitated networking opportunities with industry professionals.

                        My leadership focused on increasing membership, fostering a sense of community, and providing resources for academic and professional development.

                        **Key Achievements:**

                        - Organized workshops and networking events to promote STEM careers among Hispanic students.
                        - Led a team of 8 members to increase membership by 200% over the first quarter.
                        - Led a team of student and professional chapters to host the first Chicagoland Día de Ciencias event at the University of Chicago.

                        **Award:**  
                        SHPE Graduate Scholarship (2024) for outstanding leadership and academic excellence.

                        Learn more about SHPE at [SHPE](https://www.shpe.org/).
                            '''),
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),
        
        # DOE BES Early Career Network Representative
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),  # Bootstrap Icons
                        html.B("DOE BES Early Career Representative"),
                        html.Br(),
                        html.B("for the Center for Plastics Innovations (CPI)"),
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
                        src="assets/images/DOE-Office of Science.webp",
                        className="mb-3",
                        style={"width": "95%", "borderRadius": "8px", "padding": "1rem", "align": "center"}
                    ),
                    dcc.Markdown('''
                        As the 2022-2024 Early Career Representative for the Department of Energy's (DOE) Basic Energy Sciences (BES) program, I served as a liaison between early career researchers and the CPI, advocating for the needs and interests of junior scientists.

                        My role involved organizing workshops, facilitating communication between early career researchers and senior scientists, and promoting diversity and inclusion within the CPI community.

                        **Key Achievements:**

                        - Organized professional development workshops for junior scientists of the BES Energy Frontier Research Centers.
                        - Advocated for the needs and interests of junior scientists within the CPI.
                        - Contributed to the development of initiatives to support underrepresented groups in STEM.

                        Learn more about the Early Career Network Program at [DOE Basic Energy Sciences](https://www.energyfrontier.us/bes-ecn).
                    ''')
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),

        # Notion Campus Leader
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),  # Bootstrap Icons
                        html.B("Notion Campus Leader"),
                        html.Br(),
                        html.B("at the University of Chicago"),
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
                        src="assets/images/notion_logo.png",
                        className="mb-3",
                        style={
                            "width": "80%", 
                            "borderRadius": "8px", 
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto"}
                    ),
                    dcc.Markdown('''
                        As the selected 2023-2024 student leader in Notion’s Campus Leaders Program, I led strategic initiatives to enhance productivity and collaboration across the University of Chicago community.
        
                        My role developing and executing outreach strategies, designing educational resources, and building sustainable project management practices that supported both academic and extracurricular activities.
                        
                        **Key Achievements:**

                        - Organized project management workshops to introduce Notion to students and postdoctoral researchers.
                        - Created resources and templates to help users maximize their productivity with Notion.
                        - Fostered a community of Notion users on campus through events and online platforms.
                        - Collaborated with other campus leaders to promote cross-functional use of Notion.

                        Learn more about the Notion Campus Leader Program at [Notion](https://notion.notion.site/Notion-Campus-Leaders-Program-5817b00cbaa244bca9e0e498804cbab4).
                            ''')
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),

    ]),

    # Row 2 of Leadership Roles
    dbc.Row([
        # MRSEC GSPAB
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),  # Bootstrap Icons
                        html.B("MRSEC Graduate Student"),
                        html.Br(),
                        html.B("and Postdoc Advisory Board (GSPAB)"),
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
                        src="assets/images/mrsec.png",
                        className="mb-3",
                        style={"width": "87%", "borderRadius": "8px", "padding": "1rem", "align": "center"}
                    ),
                    dcc.Markdown('''
                        As a member of the MRSEC GSPAB...

                        **Key Achievements:**

                        - Co-organized the CAMPS Research Conference
                        - Co-organized the MRSEC Outreach Day

                        Learn more about MRSEC at [MRSEC](https://www.shpe.org/).
                            ''')
                ])
            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),
        
        # PME EDI Committee
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    [
                        html.I(className="bi bi-flask me-2"),  # Bootstrap Icons
                        html.B("PME EDI Committee"),
                        html.Br(),
                        html.B("Graduate Student Representative"),
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
                        src="assets/images/SHPE Logo.webp",
                        className="mb-3",
                        style={"width": "87%", "borderRadius": "8px", "padding": "1rem", "align": "center"}
                    ),
                    dcc.Markdown('''
                            As a member of the PME EDI Committee...

                            **Key Achievements:**

                            - Co-organized LGBTQ+ Pride Month events in 2022, 2023, and 2024.
                            - Co-organized the Hispanic Heritage Month events in 2023 and 2024.
                            - Co-organized the PME Women's Spring Luncheon in 2021

                            Learn more about MRSEC at [MRSEC](https://www.shpe.org/).
                                ''')
                ])

            ], color="light", outline=True, className="custom-card"),
            md=4, className="mb-4"
        ),

    ]),

], fluid=True)
