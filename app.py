import streamlit as st
# from google.oauth2 import service_account
# from gsheetsdb import connect

# # Create a connection object.
# credentials = service_account.Credentials.from_service_account_info(
#     st.secrets["gcp_service_account"],
#     scopes=[
#         "https://www.googleapis.com/auth/spreadsheets",
#     ],
# )
# conn = connect(credentials=credentials)

# # Perform SQL query on the Google Sheet.
# # Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def run_query(query):
#     rows = conn.execute(query, headers=1)
#     rows = rows.fetchall()
#     return rows

# sheet_url = st.secrets["private_gsheets_url"]
# rows = run_query(f'SELECT * FROM "{sheet_url}"')
# st.header("SMTE 6/11 Homework List")
# Name = st.sidebar.selectbox(
#     "ชื่อ-นามสกุล",
#     ("Email", "Home phone", "Mobile phone")
# )
# # Print results.
# subjects_all = ["สุขศึกษา"]
# for subject in subjects_all:
#     subjects = run_query(f'SELECT {subject} FROM "{sheet_url}"')
#     if subjects 
#     st.markdown(f"{subject.subject}")
#     for row in rows:
#         st.markdown(f"{row.วันที่}: {row.งาน} กำหนดส่ง:{row.ภายในเวลา} หมายเหตุ:{row.หมายเหตุ} ")
st.header("New Update Coming Soon...")