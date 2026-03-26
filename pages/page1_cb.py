# page1_cb.py - Callbacks de la page 1

import os
from dash import Input, Output
import plotly.express as px
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, "datas", "avocado.csv"))

REGIONS_FIXES = ["MidSouth", "Northeast", "SouthCentral", "Southeast", "TotalUS", "West"]


def register_callbacks(app):

    # Graphique gauche : les régions fixes qui sont toujours affiché
    @app.callback(
        Output("graph-regions-fixes", "figure"),
        Input("dropdown-region-p1", "value")
    )
    def update_graph_fixes(_):
        df_fixes = df[df["region"].isin(REGIONS_FIXES)]
        fig = px.line(
            df_fixes,
            x="Date", y="Total Volume", color="region",
            title="Quantités vendues - Régions principales",
            labels={"Total Volume": "Volume total"}
        )
        return fig

    # Graphique droit : Selon la  région choisie dans le dropdown
    @app.callback(
        Output("graph-region-choisie", "figure"),
        Input("dropdown-region-p1", "value")
    )
    def update_graph_region(region):
        df_region = df[df["region"] == region]
        fig = px.line(
            df_region,
            x="Date", y="Total Volume",
            title=f"Quantités vendues - {region}",
            labels={"Total Volume": "Volume total"}
        )
        return fig