# app.py - Fichier principal (Commit 1 : layout page 1 uniquement)

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

# Import de la page 1 uniquement
from pages import page1

# Création de l'application Dash
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

# Layout principal
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="contenu-page")
])

# Callback de navigation (simplifié pour commit 1)
@app.callback(
    Output("contenu-page", "children"),
    Input("url", "pathname")
)
def afficher_page(pathname):
    return page1.layout

# Lancement
if __name__ == "__main__":
    app.run(debug=True)