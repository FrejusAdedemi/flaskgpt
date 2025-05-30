# 🧠 FlaskGPT

Une mini app de chat en Python avec Flask + OpenAI (GPT-3.5)  
💬 Interface simple + streaming de réponses via l’API OpenAI


## ⚙️ Technologies utilisées

- Python 3.10+
- Flask
- OpenAI API (`openai>=1.0.0`)
- python-dotenv
- Tailwind CSS (via CDN)
- Render (pour le déploiement)
  
🚀 [Voir la démo en ligne](https://flaskgpt-1dku.onrender.com)


---

## 🧪 Lancer en local

### 1. Cloner le projet

```bash
git clone https://github.com/ton-utilisateur/flaskgpt.git
cd flaskgpt

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate  # sur Mac/Linux
.venv\Scripts\activate     # sur Windows

### 3. Installer les dépendances

```bash
pip install -r requirements.txt

### 4. Ajouter ta clé OpenAI
Crée un fichier .env à la racine :

```env
OPENAI_API_KEY=sk-xxxxxx...

### 5. Lancer l'app

```bash
python app.py
Puis ouvrir http://localhost:5000 dans ton navigateur.





