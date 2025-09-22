import streamlit as st
import pandas as pd
import numpy as np

def get_title():
    """Retourne le titre de l'application."""
    return "Analyse de Données Interactive"

def main():
    """Fonction principale pour exécuter l'application Streamlit."""
    st.title(get_title())

    # --- Barre Latérale pour les Contrôles ---
    st.sidebar.header("Paramètres")
    nombre_points = st.sidebar.slider(
        'Sélectionnez le nombre de points de données',
        min_value=10, max_value=200, value=50, step=10
    )

    # --- Contenu Principal ---
    st.header("Données et Graphique Générés")
    st.write(f"Génération d'un graphique avec **{nombre_points}** points de données aléatoires.")

    # Génération de données factices
    data = pd.DataFrame({
        'x': range(nombre_points),
        'y': np.random.randn(nombre_points).cumsum()
    })

    # Affichage du DataFrame
    if st.checkbox("Afficher les données brutes"):
        st.write(data)

    # Affichage du graphique
    st.line_chart(data.set_index('x'))

    st.info("Modifiez le curseur dans la barre latérale pour voir le graphique se mettre à jour en temps réel.")

if __name__ == "__main__":
    main()