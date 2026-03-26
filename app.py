import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

from pages import page1
from pages import page1_cb
from pages import page2

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

# Enregistrement des callbacks page 1
page1_cb.register_callbacks(app)

app.layout = html.Div([

    dcc.Location(id="url", refresh=False),

    # Navbar pour naviguer entre les pages
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
            dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
        ],
        brand="Application Avocado",
        color="primary",
        dark=True
    ),

    # Zone d'affichage
    html.Div(id="contenu-page")

])

@app.callback(
    Output("contenu-page", "children"),
    Input("url", "pathname")
)
def afficher_page(pathname):
    if pathname == "/page2":
        return page2.layout
    return page1.layout  # par défaut : page 1

if __name__ == "__main__":
    app.run(debug=True)