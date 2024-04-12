import streamlit as st

import add
import register
import show

home_tab, register_tab, add_tab, show_tab = st.tabs(["Home", "Register", "Add", "Show"])

# with homeTab:

with register_tab:
    register.register()
with add_tab:
    add.add()
with show_tab:
    show.show()
