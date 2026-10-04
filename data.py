import pandas as pd
import streamlit as st

def new_account():
    data=st.file_uploader("Upload a csv file", type=["csv","xlsx","xls"])
    if data is not None:
        if data.name.endswith('.csv'):
            df_new_account=pd.read_csv(data)
        elif data.name.endswith('.xlsx') or data.name.endswith('.xls'):
            df_new_account=pd.read_excel(data)
        print(df_new_account)
        return df_new_account
    else:
        st.warning("Please upload a file to proceed.")