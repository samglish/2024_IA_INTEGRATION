## IA_INTEGRATION
```python
import openai

# 🔑 Remplace ceci par ta propre clé API
openai.api_key = "sk-...ta_clé..."

# 💬 Envoi d’un message simple au modèle
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Tu es un assistant intelligent spécialisé en cybersécurité."},
        {"role": "user", "content": "Donne-moi une définition simple de l’attaque zero-day."}
    ],
    temperature=0.7,
    max_tokens=150
)

# 🖨️ Affichage de la réponse
print("Réponse de GPT-3.5-turbo :")
print(response['choices'][0]['message']['content'])
```
## Version avec input
```python
import openai

# 🔑 Clé API OpenAI
openai.api_key = "sk-...ta_clé..."

# 💬 Demander un message à l'utilisateur
question = input("Pose ta question à GPT-3.5-turbo : ")

# 🧠 Envoi à l'API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Tu es un assistant intelligent spécialisé en cybersécurité."},
        {"role": "user", "content": question}
    ],
    temperature=0.7,
    max_tokens=150
)

# 📢 Affichage de la réponse
print("\nRéponse de GPT-3.5-turbo :")
print(response['choices'][0]['message']['content'])

```
## Interface
Une fenêtre avec :
* une zone de saisie pour la question,
* un bouton "Envoyer",
* une zone de texte pour afficher la réponse.

```python
import openai
import tkinter as tk
from tkinter import scrolledtext

# 🔐 Clé API OpenAI
openai.api_key = "sk-...ta_clé..."

# 🧠 Fonction d'appel API
def envoyer_question():
    question = champ_question.get()
    if not question.strip():
        return

    zone_reponse.insert(tk.END, "Tu : " + question + "\n", "user")
    champ_question.delete(0, tk.END)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant intelligent."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=300
        )
        reponse = response['choices'][0]['message']['content']
        zone_reponse.insert(tk.END, "GPT : " + reponse + "\n\n", "bot")
    except Exception as e:
        zone_reponse.insert(tk.END, "Erreur : " + str(e) + "\n", "error")

# 🪟 Création de l’interface
fenetre = tk.Tk()
fenetre.title("Assistant GPT-3.5-turbo")

champ_question = tk.Entry(fenetre, width=70)
champ_question.pack(padx=10, pady=10)

btn_envoyer = tk.Button(fenetre, text="Envoyer", command=envoyer_question)
btn_envoyer.pack(pady=5)

zone_reponse = scrolledtext.ScrolledText(fenetre, wrap=tk.WORD, width=80, height=20)
zone_reponse.pack(padx=10, pady=10)
zone_reponse.tag_config("user", foreground="blue")
zone_reponse.tag_config("bot", foreground="green")
zone_reponse.tag_config("error", foreground="red")

fenetre.mainloop()
```
### Instructions :
1. Installe openai si ce n’est pas fait :
```bash
pip install openai
```
2. Remplace "sk-...ta_clé..." par ta vraie clé API OpenAI.
3. Lance le script :
```bash
python ton_fichier.py
```
4. Pose des questions via l'interface ! 😄
