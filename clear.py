import os
import streamlit as st
import encdec
import shutil


def clear():
    passowrd = st.text_input("Enter a password", type="password")
    clearbtn = st.button("clear")
    known = os.path.join(os.path.dirname(os.path.abspath(__file__)), "known_user")
    unknown = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unknown_user")
    organized = os.path.join(os.path.dirname(os.path.abspath(__file__)), "organized_user")
    db = os.path.join(os.path.dirname(os.path.abspath(__file__)), "db.sqlite")
    if clearbtn and passowrd == encdec.encdec():
        try:
            if os.path.exists(known):
                shutil.rmtree(known)
                os.makedirs(known)
            if os.path.exists(unknown):
                shutil.rmtree(unknown)
                os.makedirs(unknown)
            if os.path.exists(organized):
                shutil.rmtree(organized)
                os.makedirs(organized)
            if os.path.exists(db):
                os.remove(db)
            st.success("Cleared")
        except Exception as e:
            st.error(e)
    if clearbtn and passowrd != encdec.encdec():
        st.error("Password entered is incorrect")


