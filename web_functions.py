import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import streamlit as st

def load_data():
    #menambahkan dataset
    df = pd.read_csv("indeks-standar-pencemar-udara-di-spku-dataset.csv")
    #menghapus semua spasi dari nama kolom
    df.columns = list(map(lambda a: a.lstrip(), df.columns))
    #menghapus nilai yang tidak berguna
    df.drop(["tanggal"],axis=1,inplace=True)
    df.drop(["stasiun"],axis=1,inplace=True)
    pd.set_option("display.max_columns", None)
    df = df[df.pm10 != "---"]
    df = df[df.so2 != "---"]
    df = df[df.o3 != "---"]
    df = df[df.co != "---"]
    df = df[df.no2 != "---"]
    df = df[df.critical != "---"]
    df = df[df.categori != "---"]
    df.dropna(subset = ["critical"], inplace=True)
    df.dropna(subset = ["max"], inplace=True)
    df= df[df['max'] != 0]
    X = df[['pm10', 'so2', 'co', 'o3','no2' ]]
    y = df['categori']
    
    return df, X,y

def train_model(X,y,z):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=z, random_state=123)
    # membuat model Decision Tree
    tree_model = DecisionTreeClassifier()

    # melakukan pelatihan model terhadap data
    tree_model = tree_model.fit(X_train, y_train)
    

    y_pred = tree_model.predict(X_test)

    acc_secore = round(accuracy_score(y_pred, y_test), 3)
    
    data = X_test
    data1= y_test

    # data = pd.concat([data,data1])
    return tree_model,acc_secore,data,data1
    

def predict(x,y,z,features):
    tree_model,acc_score,data,data1 = train_model(x,y,z)
    
    predict = tree_model.predict(np.array(features).reshape(1,-1))
    
    return predict,acc_score

    
    
