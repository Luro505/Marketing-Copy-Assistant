""" Module for generating marketing assets using LLMs """

import os
import json
import requests

# Environment variables
API_KEY = os.environ.get('API_KEY')
BASE_URL = os.environ.get('BASE_URL')

ENDPOINT = f"{BASE_URL}/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

MODEL = "mistralai/mistral-small-3.2-24b-instruct" # Can be changed to other models

# Load product catalog
with open("products.json", "r", encoding="utf-8") as file:
    PRODUCTS = json.load(file)

product = PRODUCTS[0]  # SwiftBrew Pro

PROMPT = f"""Write a single punchy tagline for the following product.

Product: {product["name"]}
Category: {product["category"]}
Description: {product["description"]}

Return ONLY the tagline. No explanation, no quotes."""

PROMPT_LONG = f"""write a long, detailed ad
Product: {product["name"]}
Category: {product["category"]}
Description: {product["description"]}"""

PROMPT_SHORT = f"""write a short ad

Product: {product["name"]}
Category: {product["category"]}
Description: {product["description"]}"""

payload = {
    "model": MODEL,
    "messages": [
        {"role": "user", "content": PROMPT}
    ],
    "temperature": 0.7,
    "max_tokens": 200
}

steps = [0.1, 0.7, 1.5]
length = [20, 60, 80]

for temp, tokens in zip(steps, length):
    payload["temperature"] = temp
    payload["max_tokens"] = tokens
    try:
        response = requests.post(
            url=ENDPOINT,
            headers=HEADERS,
            json=payload,
            timeout=10,)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"].strip()
        print(f"Long prompt (temp: {temp}, tokens: {tokens}):\n{reply}")
    except requests.exceptions.HTTPError as e:
        print(f"Błąd dla pary temp: {temp}, tokens: {tokens} -> Status: {e.response.status_code}")
