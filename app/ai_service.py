import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_note_summary(content: str) -> str:
    if not GROQ_API_KEY:
        print("DEBUG: Clave de API no configurada.")
        return "Clave de API no configurada."
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {"role": "system", "content": "Eres un asistente útil que resume notas de manera muy concisa y profesional en una sola frase."},
            {"role": "user", "content": f"Resume brevemente el siguiente texto: {content}"}
        ],
        "max_tokens": 300
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f"DEBUG: Código de respuesta Groq -> {response.status_code}")
        print(f"DEBUG: Cuerpo de respuesta Groq -> {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        else:
            return "Resumen no disponible temporalmente."
    except Exception as e:
        print(f"DEBUG: Excepción capturada -> {e}")
        return "Resumen no disponible temporalmente."