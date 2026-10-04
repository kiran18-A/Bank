import streamlit as st
import pandas as pd

st.title("New Account Creation")
type=st.selectbox("Number of New accounts",['Single','Multiple'])
if type=='single':
    first_name=st.text_input("Enter your first name:")
    last_name=st.text_input("Enter your last name:")
    email=st.text_input("Enter your email:")
    aadhaar_number=st.number_input("Aadhaar number")
    phone_number=st.number_input("Phone number")
    city=st.text_input("City")
    account_type=st.selectbox("Select account type",["Savings","Current"])
    balance=st.number_input("Desposit amount")
    Date_of_birth=st.date_input("Date of birth")
    status=st.selectbox("Status",['Active','Inactive'])
elif type=='Multiple':
    if "account_data" not in st.session_state:
        st.session_state.account_data = None
    uploaded_file = st.file_uploader(
    "Upload Bank Account CSV",
    type=["csv"]
    )
    if uploaded_file is not None:
        st.session_state.account_data = pd.read_csv(uploaded_file)
        st.success("Data uploaded successfully!")

    if st.session_state.account_data is not None:
        df = st.session_state.account_data
        unique=[]
        columns = df.columns.tolist()
        for column in columns:
            value=st.checkbox(column, key=column, value=False)
            if value:
                unique.append(column)
        if st.button("Process the data"):
            st.write("Before processing")
            st.write("Total accounts:", len(df))
            st.write("Total columns:", len(df.columns))
            st.write("Processing the data...")
            for column in unique:
                df = df.drop_duplicates(subset=[column], keep='first')
            st.write("After processing")
            st.write("Total accounts:", len(df))
            st.write("Total columns:", len(df.columns))