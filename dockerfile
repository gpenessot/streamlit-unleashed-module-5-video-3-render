# STAGE 1: Builder - Installe les dépendances dans un environnement temporaire
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
# L'option --user est importante pour l'installation sans être root
RUN pip install --user --no-cache-dir --no-warn-script-location -r requirements.txt

# STAGE 2: Runtime - L'image finale, légère et sécurisée
FROM python:3.12-slim
WORKDIR /app

# Crée un utilisateur non-root pour la sécurité. C'est une pratique essentielle.
RUN useradd -ms /bin/bash streamlituser

# Copie UNIQUEMENT les dépendances installées depuis le stage "builder"
COPY --from=builder /root/.local /home/streamlituser/.local

# Copie le code de l'application
COPY app.py .

# Donne la propriété du répertoire à notre nouvel utilisateur
RUN chown -R streamlituser:streamlituser /app /home/streamlituser

# Change d'utilisateur pour ne plus être root
USER streamlituser

# Ajoute le chemin des packages au PATH de l'environnement
ENV PATH="/home/streamlituser/.local/bin:${PATH}"

# Expose le port par défaut de Streamlit
EXPOSE 8501

# Commande pour lancer l'application en écoutant sur toutes les interfaces
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]