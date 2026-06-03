


import streamlit as st
import requests
import pandas as pd

#response = requests.get('https://jsonplaceholder.typicode.com/users')
#users = response.json()

st.set_page_config(page_title="Contact", page_icon="🎒")
st.title("Contact App Using API")
st.write("Click the button to fetch data from the API")
if st.button("Fetch Data"):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    st.success("Data fetched successfully!")
    user_list = []
    for user in users:
        user_data = {
            "ID": user["id"],
            "Name": user["name"],
            "Username": user["username"],
            "Email": user["email"],
            "Phone": user["phone"],
            "City": user["address"]["city"],
            "Company": user["company"]["name"]
        }
        user_list.append(user_data)

    df=pd.DataFrame(user_list)
    st.subheader("User Information")
    st.dataframe(df, use_container_width=True)