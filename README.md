# Gestion de Bibliothèque - API Sample

Ce projet est une application de gestion de bibliothèque développée avec **Flask** et **APIFairy**. Il permet de gérer des auteurs, des livres et des emprunts via une interface REST documentée automatiquement.

## 🛠 Stack Technique
- **Backend :** Flask
- **Documentation API :** APIFairy (Swagger/OpenAPI)
- **Base de données :** PostgreSQL
- **ORM :** Flask-SQLAlchemy
- **Validation/Sérialisation :** Marshmallow

## Installation et Configuration

### 1. Cloner le dépôt
```bash
git clone [https://github.com/MarcelleT01/library_project.git](https://github.com/MarcelleT01/library_project.git)
cd library_project

2. Configuration de l'environnement virtuel
L'environnement a été configuré sous Windows. Pour l'activer :

venv\Scripts\activate


3. Installation des dépendances
Les bibliothèques nécessaires incluent Flask, les extensions SQLAlchemy/Marshmallow, APIFairy pour la documentation, et le driver PostgreSQL :


pip install flask flask-sqlalchemy flask-marshmallow apifairy marshmallow-sqlalchemy psycopg2-binary

4. Configuration de la base de données
L'application est configurée pour se connecter à une instance locale de PostgreSQL :

Base de données : library_db

Utilisateur : postgres

Mot de passe : 

Note : Assurez-vous que la base de données library_db est créée dans votre instance PostgreSQL avant de lancer l'application.

 Lancement de l'application
Pour démarrer le serveur de développement :

Bash

python app.py
Le serveur sera disponible sur : http://127.0.0.1:5000

 Démonstration (Interface Swagger)
Conformément aux directives, l'API est auto-documentée. Vous pouvez tester tous les points d'entrée (Endpoints) directement via l'interface interactive :

Accès Swagger : http://127.0.0.1:5000/docs

 Workflow Git
Le projet respecte les standards de versioning :

Branche main : Code stable pour la production.

Branche develop : Branche utilisée pour l'intégration des fonctionnalités.

Commits : Historique atomique et messages clairs (ex: feat:, docs:, Initialisation:).

