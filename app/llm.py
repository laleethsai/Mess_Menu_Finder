import google.generativeai as genai

# 🔑 paste your API key here
genai.configure(api_key="AIzaSyDXvpu-FimT01decoNT1f4OuyOskU4ZaiE")

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