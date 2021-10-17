import streamlit as st
import pandas as pd


import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier


def app():
    data1 = pd.read_csv('ml1_data.csv', sep=';', encoding='ISO-8859-1')
    data2 = pd.DataFrame(data1)
    st.write('''
              ## Modélisation 
            ''')
    st.write('''
                  ###### Approche logistique
                ''')
    y = data2.Target
    X = data2[['PrimeNet', 'janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    st.text('En Apprentissage')
    grid = {"C": np.logspace(-3, 3, 7), "penalty": ["l1", "l2"]}
    model = LogisticRegression()
    logreg_cv = GridSearchCV(model, grid, cv=10)
    logreg_cv.fit(X_train, y_train)
    st.write('''les meilleurs paramètre sont : ''', logreg_cv.best_params_)
    st.write('''le meilleur score est : ''', logreg_cv.best_score_)
    model2 = LogisticRegression(C=0.001, penalty="l2")
    model2.fit(X_test, y_test)
    st.text("En test ")
    st.write('''le score en test est : ''', model2.score(X_test, y_test))

    st.write('''
                  ###### Approche KNN
                ''')
    st.text('En Apprentissage')
    model3 = KNeighborsClassifier()
    param_grid = {'n_neighbors': np.arange(1, 20),
                  'metric': ['euclidean', 'manhattan']}
    grid = GridSearchCV(model3, param_grid, cv=10)
    grid.fit(X_train, y_train)
    st.write('''les meilleurs paramètre sont : ''', grid.best_params_)
    st.write('''le meilleur score est : ''', grid.best_score_)
    model4 = KNeighborsClassifier(n_neighbors=5, metric="manhattan")
    model4.fit(X_test, y_test)
    st.text("En test ")
    st.write('''le score en test est : ''', model4.score(X_test, y_test))
    st.write('''
                  #### Conclusion 
                ''')
    st.write(''' Après l'évaluation de nos différents models la régression logistisque 
                     la meilleur avec un score de métrique Accuray en test qui atteint les 90 %
                     pour notre prédiction nous utiliserons la logistique pour prédire la classe 
                     auquel appartient un nouvel individu .
        ''')


