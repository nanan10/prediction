import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

data1 = pd.read_csv('ml1_data.csv', sep=';', encoding='ISO-8859-1')
data2 = pd.DataFrame(data1)

def app():
    partie1, partie2, partie3 = st.columns(3)

    def user_Input():
        with partie1:
            Prime_net = st.number_input('Prime net ', min_value=1, max_value=1000000000, value=82225000, step=1)
            janvier = st.number_input('janvier ', min_value=1, max_value=1000000000, value=3095753, step=1)
            fevrier = st.number_input('fevrier ', min_value=1, max_value=1000000000, value=2232455, step=1)
            mars = st.number_input('mars ', min_value=1, max_value=1000000000, value=2934014, step=1)

        with partie2:
            avril = st.number_input('Avril ', min_value=1, max_value=1000000000, value=2369418, step=1)
            mai = st.number_input('mai ', min_value=1, max_value=1000000000, value=1737997, step=1)
            juin = st.number_input('juin ', min_value=1, max_value=1000000000, value=2548072, step=1)

        with partie3:
            juillet = st.number_input('juillet ', min_value=1, max_value=1000000000, value=1848907, step=1)
            aout = st.number_input('aout ', min_value=1, max_value=1000000000, value=2501309, step=1)
            septembre = st.number_input('septembre ', min_value=1, max_value=1000000000, value=2149814, step=1)

        data = {

            'Prime_net': Prime_net,
            'janvier': janvier,
            'fevrier': fevrier,
            'mars': mars,
            'avril': avril,
            'mai': mai,
            'juin': juin,
            'juillet': juillet,
            'aout': aout,
            'septembre': septembre
        }
        data_parametres = pd.DataFrame(data, index=[1])
        return data_parametres

    y = data2.Target
    X = data2[['PrimeNet', 'janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    grid = {"C": np.logspace(-3, 3, 7), "penalty": ["l1", "l2"]}
    model = LogisticRegression()
    logreg_cv = GridSearchCV(model, grid, cv=10)
    logreg_cv.fit(X_train, y_train)
    model2 = LogisticRegression(C=0.001, penalty="l2")
    model2.fit(X_test, y_test)
    st.write('''
                #### Prediction 
                   ''')
    df = user_Input()
    st.write(df)
    prediction = model2.predict(df)
    st.write(prediction)

