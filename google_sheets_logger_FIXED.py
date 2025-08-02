import streamlit as st
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load Google credentials securely from Streamlit secrets
data = json.loads(st.secrets["GOOGLE_CREDENTIALS"])

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(data, scope)
client = gspread.authorize(credentials)

# Example: open spreadsheet
sheet = client.open("Your Sheet Name").sheet1
