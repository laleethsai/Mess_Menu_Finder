import pandas as pd

def load_menu():
    df = pd.read_excel("rag/Menu.xlsx", header=None)

    menu_data = []
    current_date = None

    for i in range(len(df)):
        row = df.iloc[i]

        # Detect date row
        if isinstance(row[0], str) and any(day in row[0] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]):
            current_date = row[0]

        # Extract items
        breakfast = row[1] if len(row) > 1 else None
        lunch = row[3] if len(row) > 3 else None
        dinner = row[4] if len(row) > 4 else None

        if pd.notna(breakfast):
            menu_data.append({
                "Date": current_date,
                "Session": "Breakfast",
                "Items": str(breakfast)
            })

        if pd.notna(lunch):
            menu_data.append({
                "Date": current_date,
                "Session": "Lunch",
                "Items": str(lunch)
            })

        if pd.notna(dinner):
            menu_data.append({
                "Date": current_date,
                "Session": "Dinner",
                "Items": str(dinner)
            })

    return pd.DataFrame(menu_data)


def get_menu(date, session):
    df = load_menu()

    # Extract only numbers from Date
    df["Day"] = df["Date"].str.extract(r'(\d+)')

    result = df[
        (df["Day"] == str(date)) &
        (df["Session"].str.lower() == session.lower())
    ]

    if not result.empty:
        return ", ".join(result["Items"].tolist())

    return "Menu not found"