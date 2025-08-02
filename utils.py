import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

def generate_cold_email(name, company, product, goal, tone="Professional", length_type="Paragraphs", length_value=3):
    prompt = f"""
You are an expert email copywriter.

Write a cold email with the following details:

Recipient: {name}
Company: {company}
Product/Service Offered: {product}
Objective: {goal}
Tone: {tone}

Requirements:
- The email must have approximately {length_value} {length_type.lower()}
- Be personalized and engaging
- Include a strong call-to-action (e.g., book a call, reply to discuss)
- Do NOT include any extra comments outside the email

Respond only with the email content.
"""

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",  # Free and high-quality
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.7,
        "stop": None
    }

    try:
        response = requests.post("https://api.together.xyz/v1/completions", headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["text"].strip()
    except Exception as e:
        return f"❌ Error generating email:\n\n{e}"
