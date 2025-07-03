import dash
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/values", name="Values")

layout = dbc.Container([

    # Overview Card
    dbc.Row(
        dbc.Col(
            html.Div([
                html.H2("Personal Philosophy", className="mb-3"),
                dcc.Markdown('''
                    **Commitment to Equity, Diversity and Inclusion**  
                    Matt Tirrell was the first one to introduce me to the idea that...

                    **Commitment to Sustainability and Environment**  
                    We can all contribute to sustainability... My research with the CPI, the SDG2030

                    **Commitment to FAIR Data and Open Science**  
                    The applets in my website, my github repository...

                    **Dedication to Education and Mentorship**  
                    The tutorials I have developed, the workshop in Clubes de Ciencia, my mentorship in REU—see more in the Teaching section.

                    **Commitment to Community Engagement and Social Responsibility**  
                    Acknowledging my privilege means to acknowledge the social responsibility to make the world a fairer place.

                    **Global Perspective and Cultural Awareness**  
                    As a Fulbrighter, I genuinely believe in mutual understanding between countries as a way to create a better world for everyone.

                    **Commitment to Excellence and Quality**  
                    You have to go wholeheartedly into anything in order to achieve anything worth having.

                    **Leadership and Initiative**  
                    See the Leadership section.
                                    ''', className="text-left"),
            ], className="text-left"),
            width=12
        ),
        style={"background-color": "#f8f9fa", "padding": "24px", "border-radius": "12px", "margin-bottom": "12px"}
    ),
    

], fluid=True)
