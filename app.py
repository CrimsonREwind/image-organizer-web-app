import streamlit as st
import clear
import add
import register
import show
import home
import os



home_tab, register_tab, add_tab, show_tab, clear_tab = st.tabs(["Home", "Register", "Add", "Show","Clear"])



with home_tab:
    home.home()
with register_tab:
    register.register()
with add_tab:
    add.add()
with show_tab:
    show.show()
with clear_tab:
    clear.clear()
