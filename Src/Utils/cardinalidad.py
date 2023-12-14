import pandas as pd
import numpy as np


def cardinalidad(df):

    columnas = df.columns

    unicos = df.nunique()

    card_100 = [(df[i].nunique()/len(df))*100 for i in df]

    card = [(df[x].nunique()/len(df)) for x in df]

    cardinality = pd.DataFrame({"Columna":columnas, "Total de únicos":unicos, "Cardinalidad":card, 
                                "Cardinalidad (%)":card_100}).set_index("Columna")
    
    return cardinality