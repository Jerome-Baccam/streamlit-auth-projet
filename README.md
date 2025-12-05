# streamlit-auth-projet

# 🔒 Application d'Authentification Streamlit (Chat Album)

Bienvenue sur l'application de démonstration construite avec Streamlit, implémentant une gestion d'authentification basée sur un fichier CSV.

## 🎯 Fonctionnalités Clés

* **Authentification :** Page de connexion obligatoire avant l'accès au contenu.
* **Gestion des Utilisateurs :** Les identifiants (Username et Password) sont lus à partir du fichier `users.csv`.
* **Navigation Protégée :** Menu dynamique dans la barre latérale après connexion.
* **Album Photo :** Affichage des images dans une grille de 3 colonnes (`st.columns(3)`).

## 🚀 Démarrage Rapide (Local)

Pour lancer l'application sur votre machine locale :

### 1. Prérequis

Assurez-vous d'avoir Python installé.

### 2. Installation des Dépendances

Installez les bibliothèques requises en utilisant le fichier `requirements.txt` :

```bash
pip install -r requirements.txt
