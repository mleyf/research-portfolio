from dash import Dash, html

app = Dash(__name__)
server = app.server  # Required for Render

app.layout = html.Div("Hello World")

if __name__ == "__main__":
    app.run_server(debug=True)


