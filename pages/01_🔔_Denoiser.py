import numpy as np
import streamlit as st

from utils.denoise import get_denoiser, get_denoiser_names
from utils.noises import get_noise_adder, get_noise_names
from utils.prepare import prepare_image


def main():
    title = 'Image Denoiser'
    icon = '🔔'
    supported_types = ['jpg', 'png', 'jpeg']

    st.set_page_config(title, icon, 'centered')
    st.header(icon + ' ' + title)
    image_file = st.file_uploader('Upload an image', supported_types)

    st.subheader('Noise')

    with st.container(border=True):
        [col_1, col_2, col_3] = st.columns(
            [1, 1, 1], gap='small', vertical_alignment='center'
        )
    with col_1:
        noise_name = st.selectbox('Noise', get_noise_names(), index=1,
                                  placeholder='Enter noise name...')
        add_noise = get_noise_adder(noise_name)
    with col_2:
        seed = st.number_input('Noise seed', np.iinfo(np.int32).min, 
                               np.iinfo(np.int32).max, 0)
    with col_3:
        prob = None
        scale = None
        if noise_name == 'Salt & pepper noise':
            prob = st.slider('Noise probability', 0.0, 0.5, 0.1)
        elif noise_name == 'Gaussian noise':
            scale = int(st.slider('Noise scale', 0, 50, 25, step=1))

    st.subheader('Denoiser')
    with st.container(border=True):
        [col_1, col_2] = st.columns([1, 1], gap='small', 
                                    vertical_alignment='center')
    with col_1:
        denoiser_name = st.selectbox('Denoiser', get_denoiser_names(), index=1,
                                     placeholder='Enter denoiser name...')
        denoise = get_denoiser(denoiser_name)
    with col_2:
        kernel_size = st.select_slider('Denoiser kernel size', range(3, 18, 2), 5)

    if image_file is None:
        image_file = 'assets/examples/warning.jpg'
    if add_noise is None:
        st.error('Please select a noise name.')
        return 1
    if denoise is None:
        st.error('Please select a denoiser name.')
        return 1

    image = prepare_image(image_file)
    noised_image = add_noise(image, prob=prob, scale=scale, seed=seed)
    denoised_image = denoise(noised_image, kernel_size)

    def show(text, image):
        st.text(text)
        st.image(image, use_column_width=True)

    [col_1, col_2, col_3] = st.columns(
        [1, 1, 1], vertical_alignment='center')
    with col_1:
        show('Original', image)
    with col_2:
        show('Noisy', noised_image)
    with col_3:
        show('Noisy image after denoised', denoised_image)


if __name__ == '__main__':
    main()
