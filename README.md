Voici le contenu complet du `README.md` prêt à copier-coller ou enregistrer dans ton projet :

---

````markdown
# 🧠 FlaskGPT

Une mini app de chat en Python avec Flask + OpenAI (GPT-3.5)  
💬 Interface simple + streaming de réponses via l’API OpenAI

---

## 🚀 Aperçu

![screenshot](static/img/demo.png) <!-- Tu peux remplacer ce chemin par une image réelle ou le supprimer -->

---

## ⚙️ Technologies utilisées

- Python 3.10+
- Flask
- OpenAI API (`openai>=1.0.0`)
- python-dotenv
- Tailwind CSS (via CDN)
- Render (pour le déploiement)

---

## 🧪 Lancer en local

### 1. Cloner le projet

```bash
git clone https://github.com/ton-utilisateur/flaskgpt.git
cd flaskgpt
````

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS / Linux
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Ajouter ta clé OpenAI

Crée un fichier `.env` à la racine du projet et ajoute :

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Lancer le serveur Flask

```bash
python app.py
```

Puis ouvre [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ☁️ Déploiement sur Render

1. **Push ton repo sur GitHub**
2. **Créer un Web Service sur [Render](https://render.com)** :

   * Type : Web Service
   * Repo : `flaskgpt`
   * Build Command : `pip install -r requirements.txt`
   * Start Command : `python app.py`
   * Runtime : Python 3.x
3. **Ajouter la variable d’environnement** :

   * `OPENAI_API_KEY=ta_clé`

Render va builder et lancer ton app automatiquement. Tu obtiendras une URL comme :
`https://flaskgpt.onrender.com`

---

## 📦 Exemple de `requirements.txt`

```txt
Flask
python-dotenv
openai>=1.0.0
```

---

## 🛡️ Sécurité

* ✅ `.env` est ignoré par Git (voir `.gitignore`)
* 🔒 Ne partage jamais ta clé `OPENAI_API_KEY`
* ✅ Pour Render, configure les variables dans le Dashboard

---

## ✨ À propos

Développé avec 💻 et ☕ par [@ton-pseudo](https://github.com/ton-utilisateur)

---

## 📄 Licence

Ce projet est distribué sous licence [MIT](LICENSE)

```

---

Tu veux que je te génère le fichier prêt à être enregistré (`README.md`) ou que je t’ajoute une version WIM style (plus cool et pop) ?
```
