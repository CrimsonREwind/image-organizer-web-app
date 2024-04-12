import streamlit as st

import image
import os


def show():
    organized_user_dir = "./organized_user/"
    image_dir_paths = image.get_sub_directory_paths(organized_user_dir)

    for image_dir_path in image_dir_paths:
        user_name = os.path.basename(image_dir_path)
        expander = st.expander(user_name)
        images = image.get_all_images(image_dir_path)

        for img in images:
            image_path = os.path.join(image_dir_path, img)
            expander.image(image_path)
