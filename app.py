import streamlit as st
from multiapp import MultiApp
from apps import home, analyse, modelisation,predire # import your app modules here

app = MultiApp()
st.title('')
st.markdown("""
    # Data Predict for depense

    Application de  prévision des dépenses annuelle 
    Cette application permet de vérifier si un employé 
    consomme plus de 75 % de sa prime annuelle pendant les 9 premiers mois 

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Analyse des Données", analyse.app)
app.add_app("Modelisation", modelisation.app)
app.add_app("Prédiction", predire.app)
# The main app
app.run()
