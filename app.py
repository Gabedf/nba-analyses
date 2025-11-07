# app.py
import streamlit as st

from pages.geral import geral_page
from pages.player import player_page

pages = [st.Page(geral_page, title='Geral Page', icon=":material/home:"),
         st.Page(player_page, title='Player Stats', icon=':material/bar_chart:'),
        ]
page = st.navigation(pages, position='top')

if page:
    page.run()