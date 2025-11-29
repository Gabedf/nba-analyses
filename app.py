# app.py
import streamlit as st
st.set_page_config(page_title="NBA Project", page_icon="🏀", layout="wide")

from pages.geral import geral_page
from pages.player import player_page

pages = [
         st.Page(player_page, title='Player Stats', icon=':material/bar_chart:'),
        ]
page = st.navigation(pages, position='top')

if page:
    page.run()