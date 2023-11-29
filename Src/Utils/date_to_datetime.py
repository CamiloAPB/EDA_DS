""""
Este archico contendra las funciones para verificar y recuperar el formato datetime de las fechas en la carga de dataframes 
"""
import pandas as pd
from datetime import datetime

def to_datetime(df):

    """
    Esta función convierte la columna del DataFrame pasada como argumento y convierte el tipo de sus datos a tipo datetime
    """
    df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)

    return df

