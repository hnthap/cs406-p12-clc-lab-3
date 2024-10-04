import sys

import cv2
import streamlit as st

from utils.prepare import prepare_image
from utils.sharpen import sharpen_image


def main():
    title = 'Image Sharpener'
    icon = '✨'
    supported_types = ['jpg', 'png', 'jpeg']

    st.set_page_config(title, icon, 'centered')
    st.header(icon + ' ' + title)
    image_file = st.file_uploader('Upload an image', supported_types)

    st.subheader('Gaussian Blur')
    with st.container(border=True):
        enabled_blur = st.checkbox('Enable Gaussian blur', value=True)
        [col_1, col_2, col_3] = st.columns([1, 1, 1], gap='small',
                                           vertical_alignment='center')
    with col_1:
        kernel_size = st.select_slider('Kernel size', range(3, 18, 2),
                                        value=9)
    with col_2:
        sigma_x = st.slider('$\sigma_{x}$', 0., 10., value=2.)
    with col_3:
        sigma_y = st.slider('$\sigma_{y}$', 0., 10., value=2.)

    if image_file is None:
        image_file = 'assets/examples/moon.jpg'

    image = prepare_image(image_file)
    if enabled_blur:
        blurred = cv2.GaussianBlur(src=image, ksize=(kernel_size, kernel_size),
                                   sigmaX=sigma_x, sigmaY=sigma_y)
    else:
        blurred = image
    sharpened = sharpen_image(blurred)

    st.subheader('Results')
    [col_1, col_2, col_3] = st.columns([1, 1, 1], gap='small', 
                                       vertical_alignment='center')
    with col_1: 
        st.text('Original')
        st.image(image, use_column_width=True)
    with col_2: 
        if enabled_blur:
            st.text('Blurred')
            st.image(blurred, use_column_width=True)
    with col_3: 
        st.text('Sharpened')
        st.image(sharpened, use_column_width=True)


if __name__ == '__main__':
    sys.exit(main())
