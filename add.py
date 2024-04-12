import time

import streamlit as st

import image
from db import Database


def add():
    options = ["Camera", "Upload"]
    initial_selection = options.index("Upload")
    method = st.radio("Method", options, index=initial_selection, key = initial_selection)
    if method == "Camera":
        picture = st.camera_input("picture", key="loginPic", label_visibility='hidden')
    if method == "Upload":
        picture = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"], key = "uploadPic")
    button = st.button("Add")

    if button and picture:
        unknown_user_dir = "./unknown_user/"
        unknown_user_name = "unknown_user"
        image.save_image(picture, unknown_user_dir, unknown_user_name)

        is_match, user_id = image.compare_faces_in_directory("./known_user/", unknown_user_dir)

        if is_match:
            db = Database()
            st.write(user_id)
            user_detail = db.get_user_detail(user_id)
            image.save_image(picture, "./organized_user/" + user_detail.name + "/", user_detail.name + str(time.time_ns()))
            st.write(user_detail)
        else:
            st.error("No Match Found")

        image.delete_image(unknown_user_dir + unknown_user_name)#a
