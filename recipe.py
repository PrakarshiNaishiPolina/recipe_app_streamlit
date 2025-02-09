import streamlit as st
import pandas as pd
st.set_page_config(page_title="Recipe Book", page_icon="🍜")

# Load dataset
@st.cache_data


def load_data():
    return pd.read_csv("recipes.csv")

df = load_data()

st.title("🍽️ Recipe Book & Food Database")

# Search by ingredient
ingredient = st.text_input("Search by Ingredient", "") 

if ingredient:
    results = df[df['Ingredients'].str.contains(ingredient, case=False, na=False)]
    if not results.empty:
        st.write(results[['Recipe', 'Calories', 'Proteins', 'Fat']])
    else:
        st.warning("No recipes found with this ingredient.")

# Show a random recipe
if st.button("🍳 Generate Random Recipe"):
  
    random_recipe = df.sample(1)
    st.subheader(random_recipe["Recipe"].values[0])
    st.write(f"**Ingredients:** {random_recipe['Ingredients'].values[0]}")
    st.write(f"**Calories:** {random_recipe['Calories'].values[0]} kcal")
    st.write(f"**Proteins:** {random_recipe['Proteins'].values[0]} g")
    st.write(f"**Fat:** {random_recipe['Fat'].values[0]} g")


st.markdown(
    """
    <style>
        /* Title Styling */
        .stApp h1 {
            color: #d35400;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }

        /* Text Input Styling */
        .stTextInput > div > div > input {
            border: 2px solid #d35400;
            border-radius: 10px;
            padding: 10px;
        }

        /* Search Results Table */
        .stDataFrame {
            border: 2px solid #d35400;
            border-radius: 10px;
            overflow: hidden;
        }

        /* Button Styling */
        div.stButton > button {
            background-color: #e67e22;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            transition: 0.3s;
        }

        div.stButton > button:hover {
            background-color: #d35400;
        }

        /* Random Recipe Styling */
        .recipe-title {
            color: #c0392b;
            font-size: 28px;
            font-weight: bold;
            text-align: center;
        }

        .recipe-details {
            background-color: #f5f5f5;
            padding: 15px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
