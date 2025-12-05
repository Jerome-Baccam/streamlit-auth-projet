import streamlit as st
import pandas as pd
import os
import time

# --- Configuration Générale ---
# Assurez-vous que le fichier users.csv est dans le même répertoire
FILE_CSV = 'users.csv'
USER_PASS = 'user1pass' # Exemple de mot de passe initial pour le compte 'user1'
ADMIN_PASS = 'adminpass' # Exemple de mot de passe initial pour le compte 'admin'


# --- Fonctions de Chargement des Données (Optionnel : utilisez @st.cache_data pour la performance) ---

# Fonction pour charger les utilisateurs
def load_users():
    """Charge le DataFrame des utilisateurs à partir du CSV."""
    if os.path.exists(FILE_CSV):
        # Lire le fichier CSV
        df = pd.read_csv(FILE_CSV)
        # S'assurer que les colonnes nécessaires existent
        required_cols = ['name', 'password', 'email', 'failed_login_attemps', 'logged_in', 'role']
        if all(col in df.columns for col in required_cols):
            return df
    st.error("Fichier d'utilisateurs non trouvé ou mal formaté. Assurez-vous que users.csv existe.")
    return pd.DataFrame() # Retourne un DataFrame vide en cas d'erreur

# Charger le DataFrame des utilisateurs au démarrage
# ATTENTION : En l'absence de @st.cache_data (selon votre demande), cette ligne se réexécute à chaque interaction !
users_df = load_users()


# --- Fonctions de Gestion de Session et de Pages ---

def initialize_session():
    """Initialise les variables d'état de session nécessaires."""
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    if 'username' not in st.session_state:
        st.session_state['username'] = None
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Accueil' # Page par défaut


def login_user(username, password, df):
    """Vérifie les informations de connexion."""
    user_row = df[df['name'] == username]
    
    if not user_row.empty:
        # Vérification du mot de passe (sans hachage pour la simplicité de l'exercice)
        if user_row['password'].iloc[0] == password:
            st.session_state['authenticated'] = True
            st.session_state['username'] = username
            st.session_state['page'] = 'Accueil'
            st.success(f"Connexion réussie ! Bienvenue {username}.")
            time.sleep(0.5) # Petite pause avant le rechargement
            st.rerun()
        else:
            st.error("Mot de passe incorrect.")
    else:
        st.error("Nom d'utilisateur non trouvé.")

def logout_user():
    """Déconnecte l'utilisateur et retourne à la page de login."""
    st.session_state['authenticated'] = False
    st.session_state['username'] = None
    st.session_state['page'] = 'Accueil' # Redirection vers la page d'accueil (Login)
    st.info("Vous avez été déconnecté.")
    time.sleep(0.5)
    st.rerun()

# --- Définition des Pages Protégées ---

def page_accueil():
    st.title("Bienvenue sur ma page")
    st.write(f"Ceci est la page d'accueil du site pour {st.session_state['username']}.")
    #  # Exemple d'image pour la page d'accueil
    st.image("https://t4.ftcdn.net/jpg/04/07/75/91/360_F_407759139_WQ80XZI3XovzoqB4omith0hjFuu5ctPz.jpg", caption="Accueil") # Image générique

def page_album_chat():
    st.title("BIENVENUE dans l'album de mon chat 😻")
    st.write("Voici quelques-unes des photos de mon chat 😇")
    
    # 2. Les images sont disposées de manière à en avoir 3 sur la même ligne.
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://cdn8.futura-sciences.com/a1920/images/shutterstock_Marben.jpg", caption="Mon souhait")
        
    with col2:
        st.image("https://eproshopping.cloud/media/03397875cfc5e6cd8df8765ccdcce464548c3af5/produit/1158db10363e104ae4438b423bb2b7f69f03c133-lg.jpg", caption="Mon rêve")
        
    with col3:
        st.image("https://lesexplos.com/wp-content/uploads/2024/11/1080x1080_licorne.png", caption="Ce que j'ai")


def login_page():
    """Affiche la page de connexion (Login)."""
    st.title("Login")
    
    # Champs de formulaire
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if username and password:
                login_user(username, password, users_df)
            else:
                st.warning("Les champs Username et Password doivent être remplis.")


# --- Fonction Principale de l'Application ---

def main_app():
    # 4. Le menu dans la barre latérale
    with st.sidebar:
        if st.session_state['authenticated']:
            st.markdown(f"**Bienvenue {st.session_state['username']}**")
            st.subheader("Menu")
            
            # Liens de navigation
            if st.button("🏠 Accueil"):
                st.session_state['page'] = 'Accueil'
            if st.button("🐾 Les photos de mon chat"):
                st.session_state['page'] = 'Album Chat'
            
            st.markdown("---")
            
            # Bouton Déconnexion
            if st.button("Déconnexion"):
                logout_user()
        
        else:
            # Affichage dans la sidebar lorsque non connecté
            st.markdown("Veuillez vous connecter.")


    # --- Affichage du Contenu Principal ---
    
    if not st.session_state['authenticated']:
        # 1. Si non connecté, afficher la page de Login
        login_page()
    else:
        # Si connecté, gérer la navigation
        if st.session_state['page'] == 'Accueil':
            page_accueil()
        elif st.session_state['page'] == 'Album Chat':
            page_album_chat()


# --- Exécution ---
if __name__ == "__main__":
    # Initialisation de l'état de session avant tout
    initialize_session()
    main_app()