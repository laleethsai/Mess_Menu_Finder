import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def get_nutrition(menu_items):
    prompt = f"""
    You are a nutrition expert.

    Menu:
    {menu_items}

    Provide:
    - Calories
    - Protein
    - Carbs
    - Fat
    - Short explanation
    """

    response = model.generate_content(prompt)

    return response.text