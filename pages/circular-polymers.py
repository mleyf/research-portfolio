import dash
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import os
import dash_bio as dashbio
from dash_bio.utils import PdbParser, create_mol3d_style
import pandas as pd
import base64

# Register this page
dash.register_page(
    __name__,
    path='/circular-polymers',
    name='Circular-by-Design Polymers',
    title='Circular-by-Design Polymers'
)

# Load properties data
df = pd.read_csv('assets/data/polymer_properties_full.csv')

# Layout
layout = dbc.Container(fluid=True, children=[

    # Header
    dbc.Row(
        dbc.Col(
            html.Div([
                html.H2("Circular-by-Design Polymers for Sustainable Plastics", className="text-center mb-3"),
                dcc.Markdown('''
                        In this applet you can obtain the melt properties and crystalline properties of the different PE-like materials studied.
                        
                        If you are using this data, please cite: 
                            '''),
            ]),
            width=12
        ),
        style={
            "backgroundColor": "#f8f9fa",
            "padding": "24px",
            "borderRadius": "12px",
            "marginBottom": "12px"
        }
    ),

    # Melt-State Visualization and Properties
    dbc.Card(className="mb-5", children=[
        dbc.CardHeader(html.H3("Melt-State Visualization & Properties"), style={"backgroundColor":"#142850","color":"white"}),
        dbc.CardBody([
            dbc.Row([

                # Single Molecule Viewer
                dbc.Col(dbc.Card([
                    dbc.CardHeader(html.H5("Single Molecule"), style={"backgroundColor":"#142850","color":"white"}),
                    dbc.CardBody(html.Div(id='single-molecule-viewer', style={}))
                ]), width=5),

                # Controls & Melt Properties
                dbc.Col(dbc.Card([
                    dbc.CardHeader(html.H5("Melt Properties"), style={"backgroundColor":"#142850","color":"white"}),
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col(dcc.Dropdown(
                                id='polymer-dropdown',
                                options=[{'label': p, 'value': p} for p in df['polymer'].unique()],
                                value=df['polymer'].unique()[0],
                                clearable=False
                            ), width=4),
                            dbc.Col(dcc.Dropdown(
                                id='length-dropdown',
                                options=[{'label': f"{l} units", 'value': l} for l in df['chain_length'].unique()],
                                value=df['chain_length'].unique()[0],
                                clearable=False
                            ), width=4),
                            dbc.Col(dcc.Dropdown(
                                id='temperature-dropdown',
                                options=[{'label': f"{t} K", 'value': t} for t in df['temperature'].unique()],
                                value=df['temperature'].unique()[0],
                                clearable=False
                            ), width=4),
                        ], className="mb-4"),

                        # First row of properties
                        dbc.Row([
                            dbc.Col(html.Div([
                                html.H6("Density"), 
                                html.P(id='density-value'), 
                                html.Small("g/cm³")
                            ]), width=4),
                            dbc.Col(html.Div([
                                html.H6("Diffusion"), 
                                html.P(id='diffusion-value'), 
                                html.Small("cm²/s")
                            ]), width=4),
                            dbc.Col(html.Div([
                                html.H6("Heat of Vap."), 
                                html.P(id='vaporization-value'), 
                                html.Small("kJ/mol")
                            ]), width=4),
                        ]),
                        html.Br(),
                        # Second row of properties
                        dbc.Row([
                            dbc.Col(html.Div([
                                html.H6("Radius of Gyration"), 
                                html.P(id='radius-gyration-value'), 
                                html.Small("nm")
                            ]), width=4),
                            dbc.Col(html.Div([
                                html.H6("End-to-end Distance"), 
                                html.P(id='end-to-end-value'), 
                                html.Small("nm")
                            ]), width=4),
                            dbc.Col(html.Div([
                                html.H6("Viscosity"), 
                                html.P(id='viscosity-value'), 
                                html.Small("cP")
                            ]), width=4),
                        ]),
                    ])
                ]), width=7),

            ])
        ])
    ]),

    # Solid-State Section 
    dbc.Card(className="mb-5", children=[
        dbc.CardHeader(html.H3("Solid-State Properties & Visualization"), style={"backgroundColor":"#142850","color":"white"}),
        dbc.CardBody([

            # Crystal Polymer Selector
            dbc.Row(dbc.Col(dcc.Dropdown(
                id='polymer-crystal-dropdown',
                options=[{'label': p, 'value': p} for p in df['polymer'].unique()],
                value=df['polymer'].unique()[0],
                clearable=False
            ), width=6), className="mb-4"),

            # Frame Control and Crystal Viewer Row - FIXED
            dbc.Row([
                # Frame slider and image display
                dbc.Col([
                    html.Div([
                        html.H6("Animation Frame Control", className="mb-2"),
                        dcc.Slider(
                            id='frame-slider',
                            min=0,
                            max=304,
                            step=1,
                            value=0,
                            marks={i: str(i) for i in range(0, 305, 50)},
                            tooltip={"placement": "bottom", "always_visible": True}
                        )
                    ], className="mb-3"),
                    html.Img(
                        id='crystal-frame-image',
                        src="",
                        style={"width": "100%", "borderRadius": "8px", "height": "300px", "objectFit": "contain"}
                    )
                ], width=6),
                
                # Crystal PDB Viewer
                dbc.Col([
                    html.Div(id='crystal-viewer', style={"height":"350px"})
                ], width=6),
                
            ], className="mb-4"),

            # Crystal Properties
            dbc.Row([
                dbc.Col(html.Div([html.H6("Cryst. Temp."), html.P(id='cryst-temp'), html.Small("K")]), width=4),
                dbc.Col(html.Div([html.H6("Latent Heat"), html.P(id='cryst-heat'), html.Small("kJ/mol")]), width=4),
                dbc.Col(html.Div([html.H6("Aligned %"), html.P(id='cryst-fraction'), html.Small("%")]), width=4),
            ])

        ])
    ]),

])

###### Callback Section
# Callback for updating slider max when polymer changes
@callback(
    Output('frame-slider', 'max'),
    Input('polymer-crystal-dropdown', 'value')
)
def update_slider_max(poly_crystal):
    frame_folder = f"assets/frames/{poly_crystal.lower()}_crystal"
    if os.path.exists(frame_folder):
        frame_files = sorted([f for f in os.listdir(frame_folder) if f.endswith(('.png', '.jpg', '.jpeg'))])
        max_frames = len(frame_files) - 1 if frame_files else 0
        return max_frames
    return 0


# Callback for updating frame image
@callback(
    Output('crystal-frame-image', 'src'),
    [Input('polymer-crystal-dropdown', 'value'),
     Input('frame-slider', 'value')]
)
def update_frame_image(poly_crystal, frame_number):
    frame_folder = f"assets/frames/{poly_crystal.lower()}_crystal"
    
    if os.path.exists(frame_folder):
        frame_files = sorted([
            f for f in os.listdir(frame_folder) 
            if f.endswith(('.png', '.jpg', '.jpeg'))
        ])
        
        if frame_files and 0 <= frame_number < len(frame_files):
            frame_path = os.path.join(frame_folder, frame_files[frame_number])
            
            # Encode image to base64
            with open(frame_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode()
                return f"data:image/png;base64,{encoded_image}"
    
    return ""


# Helper function to format values with errors
def format_value_with_error(value, error=None):
    """Format a value with its uncertainty using ± symbol"""
    if error is not None and not pd.isna(error):
        # Determine number of significant digits based on error magnitude
        if error != 0:
            error_magnitude = int(-np.log10(abs(error)))
            if error_magnitude < 0:
                decimals = 0
            else:
                decimals = error_magnitude + 1
        else:
            decimals = 3
        
        # Format with appropriate precision
        formatted_value = f"{value:.{decimals}f}"
        formatted_error = f"{error:.{decimals}f}"
        return f"{formatted_value} (± {formatted_error})"
    else:
        return f"{value:.3f}"


# Main callback with added outputs for new properties
@callback(
    [
        Output('single-molecule-viewer','children'),
        Output('density-value','children'),
        Output('diffusion-value','children'),
        Output('vaporization-value','children'),
        Output('radius-gyration-value','children'),
        Output('end-to-end-value','children'),
        Output('viscosity-value','children'),
        Output('cryst-temp','children'),
        Output('cryst-heat','children'),
        Output('cryst-fraction','children'),
        Output('crystal-viewer','children'),
    ],
    [
        Input('polymer-dropdown','value'),
        Input('length-dropdown','value'),
        Input('temperature-dropdown','value'),
        Input('polymer-crystal-dropdown','value'),
    ]
)
def update_main_content(polymer, length, temp, poly_crystal):
    # Your existing melt-state logic
    melt_row = df[
        (df['polymer']==polymer)&
        (df['chain_length']==length)&
        (df['temperature']==temp)
    ].iloc[0]

    # Parse PDBs for melt-state
    single_data = PdbParser(f"assets/pdb_files/{polymer.lower()}_length{length}.pdb").mol3d_data()

    # Create styles and viewers
    style_single = create_mol3d_style(single_data['atoms'], visualization_type='sphere', color_element='atom')

    # Element-to-color mapping
    element_colors = {'C':'#059DC0','O':'#FF0D0D','N':'#3050F8','H':'#FFFFFF', 'S':'#FFFF00','P':'#909090'}
    element_sizes = {'C':0.77*1.4,'O':0.73*1.4,'N':0.75*1.4,'H':0.32*1.4, 'S':1.11*1.4,'P':0.77*1.4}

    # Override color & radius per atom
    for style, atom in zip(style_single, single_data['atoms']):
        name = atom['name']
        elem = name[0]
        style['color'] = element_colors.get(elem, '#808080')
        style['radius'] = element_sizes.get(elem, 1.2)

    single_view = dashbio.Molecule3dViewer(modelData=single_data, styles=style_single, backgroundColor='white')

    # Melt-state properties with error handling
    # Density
    density_val = melt_row['density [kg/m3]']
    density_err = melt_row.get('density_err [kg/m3]', None)  # Assuming error column exists
    dens = format_value_with_error(density_val, density_err)
    
    # Diffusion
    diff_val = melt_row['diff [cm2/s]']
    diff_err = melt_row.get('diff_err [cm2/s]', None)  # You mentioned this exists
    if diff_err is not None and not pd.isna(diff_err):
        diff = f"{diff_val:.2e} (± {diff_err:.2e})"
    else:
        diff = f"{diff_val:.2e}"
    
    # Heat of vaporization
    vap_val = melt_row['H_vap [kJ]']
    vap_err = melt_row.get('H_vap_err [kJ]', None)  # Assuming error column exists
    vap = format_value_with_error(vap_val, vap_err)
    
    # Radius of gyration
    rg_val = melt_row.get('radius_of_gyration [nm]', 0)  # Adjust column name as needed
    rg_err = melt_row.get('radius_of_gyration_err [nm]', None)
    rg = format_value_with_error(rg_val, rg_err) if not pd.isna(rg_val) else "N/A"
    
    # End-to-end distance
    ete_val = melt_row.get('r_ee [nm]', 0)  # Adjust column name as needed
    ete_err = melt_row.get('end_to_end_distance_err [nm]', None)
    ete = format_value_with_error(ete_val, ete_err) if not pd.isna(ete_val) else "N/A"
    
    # Viscosity (if available)
    visc_val = melt_row.get('viscosity [cP]', 0)  # Adjust column name as needed
    visc_err = melt_row.get('viscosity_err [cP]', None)
    visc = format_value_with_error(visc_val, visc_err) if not pd.isna(visc_val) else "N/A"

    # Solid-state PDB viewer
    cryst_data = PdbParser(f"assets/pdb_files/{poly_crystal.lower()}_length80_system.pdb").mol3d_data()
    cryst_style = create_mol3d_style(cryst_data['atoms'], visualization_type='sphere', color_element='atom')
    
    for style, atom in zip(cryst_style, cryst_data['atoms']):
        name = atom['name']
        elem = name[0]
        style['color'] = element_colors.get(elem, '#808080')
        style['radius'] = 1.2
    
    cryst_view = dashbio.Molecule3dViewer(modelData=cryst_data, styles=cryst_style, backgroundColor='white')

    # Solid-state properties
    cryst_row = df[df['polymer']==poly_crystal].iloc[0]
    ctemp = f"{cryst_row['crystallization_temp']:.1f}"
    cheap = f"{cryst_row['latent_heat_crystallization']:.2f}"
    cfrac = f"{cryst_row['aligned_fraction']:.1%}"

    return single_view, dens, diff, vap, rg, ete, visc, ctemp, cheap, cfrac, cryst_view
