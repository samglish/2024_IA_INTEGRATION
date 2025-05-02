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
