import io

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from obj2html import obj2html
import time


# download img
def load_image(img_bytes):
    img = Image.open(io.BytesIO(img_bytes.getvalue()))
    img = img.convert('RGB')
    return img


# make obj file -> return the path
def make_obj(img) -> str:
    # sent img to neural network
    time.sleep(2)
    return 'knight.obj'


def main():

    st.title("3D Reconstruction")
    image_bytes = st.sidebar.file_uploader("Choose Image",
                                           type=["png", "jpg", "jpeg"])

    if image_bytes is not None:
        # To View Uploaded Image
        img_name = image_bytes.name.split(".")[0]
        img = load_image(image_bytes)
        st.sidebar.image(img)

        # 3d reconstruction method
        obj_file_path = make_obj(img)

        # make window with interactive 3d model
        html_string = obj2html(obj_file_path, html_elements_only=True)
        components.html(html_string)

        # download obj file
        with open(obj_file_path) as f:
            st.download_button('Download obj file', f,
                               file_name=img_name + '.obj')



if __name__ == "__main__":
    main()