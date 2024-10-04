import cv2
import numpy as np
import streamlit as st

from utils.prepare import prepare_image


def main():
    title = 'Edge Detection'
    icon = '📦'
    supported_types = ['jpg', 'png', 'jpeg']
    st.set_page_config(title, icon, 'centered')
    st.header(icon + ' ' + title)

    image_file = st.file_uploader('Upload an image', supported_types)
    if image_file is None:
        image_file = 'assets/examples/arab_girl.jpg'
    image = prepare_image(image_file, 1024)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    st.divider()
    sobel(image, gray)
    st.divider()
    prewitt(image, gray)
    st.divider()
    canny(image, gray)


def sobel(image: np.ndarray, gray: np.ndarray):
    st.subheader('Sobel')
    with st.container(border=True):
        kernel_size = st.select_slider('Kernel size', range(3, 14, 2), value=5)
    sobel_x = cv2.Sobel(gray, -1, 1, 0, ksize=kernel_size)
    sobel_y = cv2.Sobel(gray, -1, 0, 1, ksize=kernel_size)
    sobel = cv2.addWeighted(
        cv2.convertScaleAbs(sobel_x), 0.5,
        cv2.convertScaleAbs(sobel_y), 0.5, 0
    )
    [col_1, col_2] = st.columns([1, 1], gap='small', 
                                vertical_alignment='center')
    with col_1: 
        st.text('Original')
        st.image(image, use_column_width=True)
    with col_2: 
        st.text('Result')
        st.image(sobel, use_column_width=True)


def prewitt(image: np.ndarray, gray: np.ndarray):
    st.subheader('Prewitt')
    prewitt_x_kernel = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]],
                                dtype=np.float32)
    prewitt_y_kernel = np.transpose(prewitt_x_kernel)
    prewitt_x = cv2.filter2D(gray, -1, prewitt_x_kernel)
    prewitt_y = cv2.filter2D(gray, -1, prewitt_y_kernel)
    prewitt = cv2.addWeighted(
        cv2.convertScaleAbs(prewitt_x), 0.5,
        cv2.convertScaleAbs(prewitt_y), 0.5, 0
    )
    [col_1, col_2] = st.columns([1, 1], gap='small', 
                                vertical_alignment='center')
    with col_1: 
        st.text('Original')
        st.image(image, use_column_width=True)
    with col_2: 
        st.text('Result')
        st.image(prewitt, use_column_width=True)


def canny(image: np.ndarray, gray: np.ndarray):
    st.subheader('Canny edges')
    with st.container(border=True):
        [col_1, col_2] = st.columns([1, 1], gap='small',
                                    vertical_alignment='center')
    with col_1:
        lower_threshold = st.slider('Lower threshold', 0, 255, 100)
    with col_2:
        upper_threshold = st.slider('Upper threshold', 0, 255, 200)
    [col_1, col_2] = st.columns([1, 1], gap='small', 
                                vertical_alignment='center')
    with col_1: 
        st.text('Original')
        st.image(image, use_column_width=True)
    with col_2: 
        if upper_threshold < lower_threshold:
            st.warning('Upper threshold must be greater than lower threshold.')
        else:
            canny = cv2.Canny(gray, lower_threshold, upper_threshold)
            st.text('Result')
            st.image(canny, use_column_width=True)


if __name__ == '__main__':
    main()
