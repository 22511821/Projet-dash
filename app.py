# app.py - Commit 2 : ajout des callbacks page 1

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

from pages import page1
from pages import page1_cb  # importation des callbacks

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

# Enregistrement des callbacks de p1
page1_cb.register_callbacks(app)

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="contenu-page")
])

@app.callback(
    Output("contenu-page", "children"),
    Input("url", "pathname")
)
def afficher_page(pathname):
    return page1.layout

if __name__ == "__main__":
    app.run(debug=True)