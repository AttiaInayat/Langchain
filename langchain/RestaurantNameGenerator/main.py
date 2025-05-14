import streamlit as st
import langchain_helper 

st.title("Restaurant Name Generator")
cuisine=st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

if cuisine:
    result= langchain_helper.generate_restaurant_name_and_cusines(cuisine)
    st.header(result['restaurant_name'].strip())
    st.write("Cuisines Items: ")
    cuisine_items=result['menu_items'].strip().split(',')

    for item in cuisine_items:
        st.write('-',item)

