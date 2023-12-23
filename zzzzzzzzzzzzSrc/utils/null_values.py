import pandas as pd

def show_nulls(df):

    for i in df:
        a = df[i].isna().sum()
        if a > 0:
            print(f"La cantidad de nulos de la variable {i} es {a}")