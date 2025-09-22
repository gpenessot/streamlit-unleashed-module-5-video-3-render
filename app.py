import streamlit as st
import pandas as pd
import numpy as np

def get_title():
    """Retourne le titre de l'application."""
    return "Analyse de Données Interactive"

def main():
    """Fonction principale pour exécuter l'application Streamlit."""
    st.title(get_title())

    st.write("Générateur de données aléatoires pour démonstration.")

    # Slider pour choisir le nombre de points de données
    nombre_points = st.slider("Nombre de points", 10, 100, 50)

    # Génération des données
    data = pd.DataFrame({
        'x': np.arange(nombre_points),
        'y': np.random.randn(nombre_points).cumsum()
    })

    # Affichage du graphique
    st.line_chart(data)

if __name__ == "__main__":
    main()
    