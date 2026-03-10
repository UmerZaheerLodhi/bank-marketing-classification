import pandas as pd

def load_data(path):
   
    return pd.read_csv(path, sep=';')


def preprocess_data(df):
    
    X = df.drop('y', axis=1)
    y = df['y'].map({'no': 0, 'yes': 1})  # convert target to binary

    X = pd.get_dummies(X, drop_first=True)

    return X, y
