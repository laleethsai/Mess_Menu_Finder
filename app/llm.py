import os
import google.generativeai as genai

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set in environment")

genai.configure(api_key=api_key)

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

    try:
        response = model.generate_content(prompt)
        return response.text if response.text else "No response from model"
    except Exception as e:
        return f"Error generating response: {str(e)}"