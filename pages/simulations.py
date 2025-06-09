import dash  
from dash import dcc, html, Input, Output  
import dash_player  
import plotly.express as px  
import pandas as pd  

dash.register_page(__name__, path='/simulations')  

# Sample data for interactive plot  
df = pd.DataFrame({  
    'Time (ns)': [0, 1, 2, 3],  
    'Energy (kJ/mol)': [100, 85, 70, 65]  
})  

layout = html.Div([  
    html.H2("Liquid Crystal Simulations"),  
    dash_player.DashPlayer(  
        id='simulation-video',  
        url='/assets/videos/my_video.mp4',  
        controls=True,  
        width='80%'  
    ),  
    dcc.Graph(id='energy-plot'),  
    dcc.Slider(0, 3, 1, value=0, id='time-slider')  
])  

@dash.callback(  
    Output('energy-plot', 'figure'),  
    Input('time-slider', 'value')  
)  
def update_plot(selected_time):  
    fig = px.line(df, x='Time (ns)', y='Energy (kJ/mol)',  
                  title="Energy Landscape of LC System")  
    fig.add_vline(x=selected_time, line_dash="dash", line_color="red")  
    return fig  

