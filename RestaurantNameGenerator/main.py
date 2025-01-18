import streamlit as st
from utility import generate_restaurant_name_and_items
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Pakistani", "Italian", "Mexican", "Arabic", "American"))

if cuisine:
    response=generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip().strip('"'))
    menu_items = response['menu_items'].strip().strip('"').split(",")
    st.write("**Menu Items**\n")
    for item in menu_items:
        st.write("-", item)
