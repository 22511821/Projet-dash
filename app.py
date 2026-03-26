import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

from pages import page1
from pages import page1_cb
from pages import page2_cb

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

from pages import page1
from pages import page1_cb
from pages import page2
from pages import page2_cb
from pages import page3       

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

page1_cb.register_callbacks(app)
page2_cb.register_callbacks(app)

app.layout = html.Div([

    dcc.Location(id="url", refresh=False),

    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
            dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
            dbc.NavItem(dbc.NavLink("Page 3", href="/page3")),  # ajout
        ],
        brand="Application Avocado",
        color="primary",
        dark=True
    ),

    html.Div(id="contenu-page")

])

@app.callback(
    Output("contenu-page", "children"),
    Input("url", "pathname")
)
def afficher_page(pathname):
    if pathname == "/page2":
        return page2.layout
    if pathname == "/page3":
        return page3.layout    # ajout
    return page1.layout

if __name__ == "__main__":
    app.run(debug=True)
from pages import page2_cb    

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

# Enregistrement des callbacks
page1_cb.register_callbacks(app)
page2_cb.register_callbacks(app)   

app.layout = html.Div([

    dcc.Location(id="url", refresh=False),

    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
            dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
        ],
        brand="Application Avocado",
        color="primary",
        dark=True
    ),

    html.Div(id="contenu-page")

])

@app.callback(
    Output("contenu-page", "children"),
    Input("url", "pathname")
)
def afficher_page(pathname):
    if pathname == "/page2":
        return page2.layout
    return page1.layout

if __name__ == "__main__":
    app.run(debug=True)