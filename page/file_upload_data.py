import streamlit as st
import pandas as pd

st.title("Upload New Account Data")

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

    if st.button("Process the data"):
        st.write("Processing the data...")
        df = st.session_state.account_data
        st.write("Total accounts:", len(df))
        st.write("Total columns:", len(df.columns))