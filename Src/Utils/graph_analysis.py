import matplotlib.pyplot as plt
import seaborn as sns


def side_wins_univariate(df):

    """
    Esta función devuelve las gráficas de barras que muestran el conteo de victorias y derrotas de cada lado
    """

    results = df[["blue_result", "red_result"]]
    blue_wins = results["blue_result"][results["blue_result"] == 1].count()
    red_wins = results["red_result"][results["red_result"] == 1].count()

    # Creamos el plot
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # Plot del subplot del lado azul
    sns.countplot(results, x = "blue_result", palette = "Blues", ax=axes[0])

    axes[0].set_title("Blue side victories")

    axes[0].set_xlabel("Blue result")
    axes[0].set_xticks([0,1], ["Loss", "Win"])
    axes[0].set_ylabel("Amount of win/loss")
    
    axes[0].annotate(xy=(0,red_wins), text=red_wins, xytext=(0,red_wins/2))
    axes[0].annotate(xy=(1,blue_wins), text=blue_wins, xytext=(1,blue_wins/2))


    # Plot del subplot del lado rojo
    sns.countplot(results, x = "red_result", palette= 'Reds', ax=axes[1])
    
    plt.title("Red side victories")
    
    plt.xlabel("Red result")
    plt.ylabel("Amount of win/loss")
    plt.xticks([0,1], ["Loss", "Win"])
    
    plt.annotate(xy=(1,red_wins), text=red_wins, xytext=(1,red_wins/2))
    plt.annotate(xy=(0,blue_wins), text=blue_wins, xytext=(0,blue_wins/2))
    
    # Ajuste del subplot
    plt.tight_layout()

    # Graficamos
    plt.show()