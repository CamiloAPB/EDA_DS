""""
Este archico contendra las funciones para verificar y recuperar el formato datetime de las fechas en la carga de dataframes 
"""


def assing_split(df):

    """
    Esta función asigna las diversos splits entre Spring y Summer

    """

    spring_splits = ["Opening", "Split 1", "Winter"]
    summer_splits = ["Split 2", "Closing"]

    for split in df["split"]:
        if split in spring_splits:
            df["split"][df["split"] == split] = "Spring"
            pass
        elif split in summer_splits:
            df["split"][df["split"] == split] = "Summer"
    
    return df

