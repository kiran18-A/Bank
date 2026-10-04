from flask import app
import streamlit as st

Home = st.Page("page/home.py", title="Home")
File_upload = st.Page("page/file_upload_data.py", title="Upload_Data")
New_account = st.Page("page/new_account.py", title="New_Account")
pg = st.navigation([Home,New_account,File_upload])
pg.run()