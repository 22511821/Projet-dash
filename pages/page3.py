import os
import dash_bootstrap_components as dbc
from dash import dcc, html


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "expli1.md"), "r", encoding="utf-8") as f:
    contenu1 = f.read()

with open(os.path.join(BASE_DIR, "expli2.md"), "r", encoding="utf-8") as f:
    contenu2 = f.read()

with open(os.path.join(BASE_DIR, "expli3.md"), "r", encoding="utf-8") as f:
    contenu3 = f.read()


layout = dbc.Container([

    dbc.Card([

        dbc.CardHeader(
            html.H4("Présentation de Dash", style={"color": "white"}),
            style={"backgroundColor": "#0dcaf0"}
        ),

        dbc.CardBody([
            dbc.Tabs([
                dbc.Tab(dcc.Markdown(contenu1), label="Accueil",  tab_id="tab-1"),
                dbc.Tab(dcc.Markdown(contenu2), label="Layout",   tab_id="tab-2"),
                dbc.Tab(dcc.Markdown(contenu3), label="CallBack", tab_id="tab-3"),
            ], active_tab="tab-1")
        ])

    ], className="mt-3")

], fluid=True)