import os


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

os.makedirs("static/images/", exist_ok=True)

def generate_graphs():
    #cargamos los datos
    file_path ="train.csv"
    data = pd.read_csv(file_path)

    #limpieza inicial de nuestros dataframe
    data_cleaned = data.copy()
    data_cleaned["Age"].fillna(data_cleaned["Age"].median(), inplace=True)
    data_cleaned["Embarked"].fillna(data_cleaned["Embarked"].mode()[0], inplace=True)

    #Grafico 1: Distribucion de supervivencia
    plt.figure(figsize=(8,
                        6))
    sns.countplot(data=data_cleaned, x="Survived")
    plt.title("Distribucion de supervivencia")
    plt.xlabel("Sobrevivio (1=si, 0 = No")
    plt.ylabel("cantidad")
    plt.tight_layout()
    plt.savefig("static/images/survived_distribution.png")
    plt.close()

    #Grafico 2 Distribucion de edad por supervivencias
    plt.figure(figsize=(8,6))
    sns.histplot(data=data_cleaned, x="Age", hue="Survived",kde=True, bins=20)
    plt.title("Distribucion de edad por supervivencia")
    plt.xlabel("Edad")
    plt.ylabel("cantidad")
    plt.tight_layout()
    plt.savefig("static/images/age_distribution.png")
    plt.close()

    plt.figure(figsize=(8,6))
    sns.scatterplot(x="Age", y="Fare", hue="Survived", data=data_cleaned, marker="o")
    plt.title("Relacion entre tarifas y edad")
    plt.xlabel("edad")
    plt.ylabel("Tarifa")
    plt.legend(title="Supervivencia", loc="upper right")
    plt.tight_layout()
    plt.savefig("static/images/age_scatter.png")
    plt.close()