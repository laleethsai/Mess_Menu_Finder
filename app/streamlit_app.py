import streamlit as st
from data_loader import get_menu
from llm import get_nutrition

st.title("🍽️ Keerthana's Menu Analyzer")

date = st.selectbox("Select Date", list(range(1, 31)))
session = st.selectbox("Session", ["Breakfast", "Lunch", "Dinner"])

if st.button("Get Menu"):

    # ✅ menu is defined here
    menu = get_menu(date, session)

    st.subheader("📋 Menu")

    if menu != "Menu not found":
        items = list(set(menu.split(",")))

        for item in items:
            st.write("•", item.strip())

        st.subheader("🥗 Nutrition Analysis")

        with st.spinner("Analyzing..."):
            nutrition = get_nutrition(menu)

        st.write(nutrition)

    else:
        st.write(menu)