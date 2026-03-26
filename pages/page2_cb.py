# Callbacks de la page 2

import os
from dash import Input, Output
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, "datas", "avocado.csv"))


COLONNES_CACHEES = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
colonnes_affichees = [col for col in df.columns if col not in COLONNES_CACHEES]


def register_callbacks(app):

    @app.callback(
        Output("tableau-p2", "data"),
        Output("badge-lignes", "children"),
        Input("dropdown-region-p2", "value"),
        Input("radio-type-p2", "value")
    )
    def update_tableau(region, type_avocat):


        df_filtre = df[df["region"] == region]

        if type_avocat != "Tous":
            df_filtre = df_filtre[df_filtre["type"] == type_avocat]

        nb_lignes = len(df_filtre)

        return df_filtre[colonnes_affichees].to_dict("records"), f"Lignes: {nb_lignes}"