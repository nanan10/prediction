import streamlit as st

def app():
    st.write('''
    ### Problème 
    
 Ces donnees presentent les depenses de plusieurs individus sur 9 mois, la prime versee et la target 
(1 si les depenses de l'annee sont superieures a 75% de la prime et 0 sinon). Le but en fait est de prendre des mesures en avance
(des a partir du 9eme mois) si la target est egale a 1.
Donc le probleme sera de :
- Construire un bon modele de classification (supervise)

IMPORTANT ==> Ce qui ne sera pas tolorer pour l'entreprise serait de dire que les depenses ne depasseront pas alors qu'elles vont depasser la prime.
Donc faites bcp attention a la methode et au modele a choisir selon le context.

    
    ''')
