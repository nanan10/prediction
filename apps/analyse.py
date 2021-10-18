import streamlit as st
import pandas as pd

data1 = pd.read_csv('ml1_data.csv', sep=';', encoding='ISO-8859-1')
data2 = pd.DataFrame(data1)
def app():
    st.title("Analysons les données")
    st.write(data2.head())
    data2.shape
    st.write('''Notre jeu de donnée est constitué de huit cent quatre-vingt (880) observations et onze variables 
                parmi les variables :
               la Target correspond à variable expliquer et les autres sont les variables explicatives .''')
    data3 = data2.copy()
    st.write('''
       ###### Idendification des valeurs manquantes
       ''')

    st.write(data2.isna().sum())
    st.write('''Toute les valeurs sont présentes dans notre jeu de donnée et sont correcte ''')

    st.write(''' Pour cette Analyse nous allons utilisé toute les variables puisqu'elles
                    ont été correctement renseigner et sont utiles pour faire notre prévision
                     ''')

    st.write('''##### Variables Explicatives''')

    p1, p2, p3 = st.columns(3)

    with p1:
        st.write(''' Prime net :   variable Quantitatif représentant la prime annuelle ''')
        st.write('''Janvier : Variable Quantitative représentant les dépenses du mois Janvier''')
        st.write('''Fevrier : Variable Quantitative représentant les dépenses du mois  Fevrier''')
        st.write('''Mars : Variable Quantitative représentant les dépenses du mois Mars''')

    with p2:
        st.write('''Avril : Variable Quantitative représentant les dépenses du mois Avril ''')
        st.write('''Mai : Variable Quantitative représentant les dépenses du mois Mai ''')
        st.write('''Juin : Variable Quantitative représentant les dépenses du mois Juin ''')

    with p3:
        st.write('''** Juillet ** : Variable Quantitative représentant les dépenses du mois Juillet''')
        st.write('''Aout : Variable Quantitative représentant les dépenses du mois Aout ''')
        st.write('''Septembre : Variable Quantitative représentant les dépenses du mois Septembre ''')

    st.write('''
         ###### Analysons notre Target
       ''')
    st.write(data2['Target'].value_counts(normalize=True))
    st.write('''
       On remarque qu'il y a 52,16 % des employés dépensés 75 % de leur prime Annuelle 
        ''')


