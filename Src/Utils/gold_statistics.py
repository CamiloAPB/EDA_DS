def get_team_goldstats(df):

    """
    Esta función calcula las estadísticas de oro por equipo y las añade como nuevas columnas al DataFrame
    """

    gold_stats = df[df.columns[df.columns.str.contains("gold")]]

    #lado azul

    blue_gold_stats = gold_stats[gold_stats.columns[gold_stats.columns.str.contains("blue")]]

    #total
    df["blue_totalgold"] = blue_gold_stats[blue_gold_stats.columns[blue_gold_stats.columns.str.contains("total")]].sum(axis=1)

    #earned
    df["blue_earnedgold"] = blue_gold_stats[blue_gold_stats.columns[blue_gold_stats.columns.str.contains("earned")]].sum(axis=1)

    #spent
    df["blue_spentgold"] = blue_gold_stats[blue_gold_stats.columns[blue_gold_stats.columns.str.contains("spent")]].sum(axis=1)

    #at10
    df["blue_goldat10"] = blue_gold_stats[blue_gold_stats.columns[blue_gold_stats.columns.str.contains("at10")]].sum(axis=1)


    #at15
    df["blue_goldat15"] = blue_gold_stats[blue_gold_stats.columns[blue_gold_stats.columns.str.contains("at15")]].sum(axis=1)

    #lado rojo

    red_gold_stats = gold_stats[gold_stats.columns[gold_stats.columns.str.contains("red")]]

    #total
    df["red_totalgold"] = red_gold_stats[red_gold_stats.columns[red_gold_stats.columns.str.contains("total")]].sum(axis=1)

    #earned
    df["red_earnedgold"] = red_gold_stats[red_gold_stats.columns[red_gold_stats.columns.str.contains("earned")]].sum(axis=1)

    #spent
    df["red_spentgold"] = red_gold_stats[red_gold_stats.columns[red_gold_stats.columns.str.contains("spent")]].sum(axis=1)

    #at10
    df["red_goldat10"] = red_gold_stats[red_gold_stats.columns[red_gold_stats.columns.str.contains("at10")]].sum(axis=1)


    #at15
    df["red_goldat15"] = red_gold_stats[red_gold_stats.columns[red_gold_stats.columns.str.contains("at15")]].sum(axis=1)

    return df

def get_gold_diff(df):

    """
    Calcula la diferencia de las diferentes estadísticas de oro y las añade como columnas al DataFrame
    """

    #diferencia total
    df["blue_totalgold_diff"] = df["blue_totalgold"] - df["red_totalgold"]
    df["red_totalgold_diff"] = df["blue_totalgold_diff"]*-1

    #diferencia de oro ganado
    df["blue_earnedgold_diff"] = df["blue_earnedgold"] - df["red_earnedgold"]
    df["red_earnedgold_diff"] = df["blue_earnedgold_diff"]*-1

    #diferencia de oro gastado
    df["blue_spentgold_diff"] = df["blue_spentgold"] - df["red_spentgold"]
    df["red_spentgold_diff"] = df["blue_spentgold_diff"]*-1

    #diferencia de oro a minuto 10
    df["blue_gold_diffat10"] = df["blue_goldat10"] - df["red_goldat10"]
    df["red_gold_diffat10"] = df["blue_gold_diffat10"]*-1

    #diferencia de oro a minuto 15
    df["blue_gold_diffat15"] = df["blue_goldat15"] - df["red_goldat15"]
    df["red_gold_diffat15"] = df["blue_gold_diffat15"]*-1

    return df

