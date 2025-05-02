# 2024_IA_INTEGRATION
2024 IA
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
