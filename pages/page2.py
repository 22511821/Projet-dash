# Page 2.py
# Cette page permet de filtrer les données affichées dans le tableau en fonction de la région et une liste d’options permettant un filtrage du type d’avocat.

import os
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, "datas", "avocado.csv"))

# L'ensembeles des régions
all_regions = sorted(df["region"].unique())

# Colonnes à ne pas afficher car elles n'ont pas de noms explicites.
COLONNES_CACHEES = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
colonnes_affichees = [col for col in df.columns if col not in COLONNES_CACHEES]

# Layout de la page
layout = dbc.Container([

    html.Div([

        # Ligne des filtres
        dbc.Row([

            # Dropdown région
            dbc.Col([
                html.Label("Sélectionner une région:", className="fw-bold"),
                dcc.Dropdown(
                    id="dropdown-region-p2",
                    options=[{"label": r, "value": r} for r in all_regions],
                    value=all_regions[0],
                    clearable=False
                )
            ], xs=12, md=6),  # empilé sur petits écrans

            # Radio buttons type
            dbc.Col([
                html.Label("Sélectionner un type:", className="fw-bold"),
                dbc.RadioItems(
                    id="radio-type-p2",
                    options=[
                        {"label": " Tous",         "value": "Tous"},
                        {"label": " conventional", "value": "conventional"},
                        {"label": " organic",      "value": "organic"}
                    ],
                    value="Tous",
                    inline=True
                )
            ], xs=12, md=6),

        ], className="mb-2 mt-3 p-3 border rounded bg-light"),

        # Badge nombre de lignes (aligné à droite)
        dbc.Row([
            dbc.Col(
                dbc.Badge(
                    id="badge-lignes",
                    color="primary",
                    style={"fontSize": "13px", "padding": "6px 12px",
                           "backgroundColor": "#6f42c1"}
                ),
                className="d-flex justify-content-end mb-2"
            )
        ]),

        # Tableau
        dbc.Row([
            dbc.Col(
                dash_table.DataTable(
                    id="tableau-p2",
                    columns=[{"name": col, "id": col} for col in colonnes_affichees],
                    data=df[colonnes_affichees].to_dict("records"),
                    sort_action="native",   # tri sur les colonnes
                    page_size=10,
                    style_table={"overflowX": "auto"},
                    style_header={
                        "backgroundColor": "#343a40",
                        "color": "white",
                        "fontWeight": "bold",
                        "textAlign": "left"
                    },
                    style_cell={
                        "textAlign": "left",
                        "padding": "8px",
                        "fontSize": "13px"
                    },
                    style_data_conditional=[
                        {"if": {"row_index": "odd"}, "backgroundColor": "#f8f9fa"}
                    ]
                )
            )
        ])

    ], className="mt-3")

], fluid=True)