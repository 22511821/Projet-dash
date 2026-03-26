# pages/page1.py - Layout de la page 1
# Page de comparaison des quantités vendues par région

import os
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd

# Chemin absolu vers le CSV
# BASE_DIR remonte de pages/ vers le dossier racine du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, "datas", "avocado.csv"))

# Liste de toutes les régions pour le menu déroulant
all_regions = sorted(df["region"].unique())

# Layout de la page 1
layout = dbc.Container([

    dbc.Card([

        # Header avec le titre
        dbc.CardHeader(
            html.H4("Quantités vendues (Total Volume)", style={"color": "white"}),
            style={"backgroundColor": "#0dcaf0"}
        ),

        # Body avec deux colonnes
        dbc.CardBody([
            dbc.Row([

                # Colonne gauche : graphique des régions fixes
                dbc.Col([
                    dcc.Graph(id="graph-regions-fixes")
                ], width=6),

                # Colonne droite : badge + dropdown + graphique dynamique
                dbc.Col([

                    dbc.Badge(
                        "Sélectionnez une région:",
                        className="mb-2",
                        style={
                            "fontSize": "14px",
                            "padding": "8px 16px",
                            "width": "100%",
                            "display": "block",
                            "textAlign": "center",
                            "backgroundColor": "#6f42c1"
                        }
                    ),

                    dcc.Dropdown(
                        id="dropdown-region-p1",
                        options=[{"label": r, "value": r} for r in all_regions],
                        value=all_regions[0],
                        clearable=False,
                        className="mb-3"
                    ),

                    dcc.Graph(id="graph-region-choisie")

                ], width=6)

            ])
        ])

    ], className="mt-3")

], fluid=True)