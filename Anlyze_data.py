import pandas as pd

def analyze_data():
    file_path ="train.csv"
    data = pd.read_csv(file_path)

    #Limpieza de datos de nuestrp dataframe
    data_cleaned = data.copy()
    data_cleaned["Age"].fillna(data_cleaned["Age"].median(), inplace=True)
    data_cleaned["Embarked"].fillna(data_cleaned["Embarked"].mode()[0], inplace=True)

    #calcular la tasa de supervivencia
    survival_rate =round(data_cleaned["Survived"].mean() * 100,2)

    class_distribution = (
        data_cleaned["Pclass"]
        .value_counts(normalize=True)
        .mul(100)#multiplicar por 100
        .round(2) #redondear
        .to_dict() #convertir a diccionario
    )
    return survival_rate, class_distribution