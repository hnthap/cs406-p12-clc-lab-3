import sys

import streamlit as st


def main():
    title = 'Image Enhancements'
    # pages = [
    #     '01_🔔_Denoiser',
    #     '02_✨_Sharpener',
    #     '03_📦_Edge_Detection',
    # ]
    st.set_page_config(title, '🥰', 'centered')
    with open('README.md', 'rt') as f:
        content = f.read()
        header, content = content.split('\n', 1)
        st.markdown(header)
        with st.container(border=True):
            st.text('''
🔰   Select a demo from the sidebar...
''')
        st.markdown(content)


if __name__ == '__main__':
    sys.exit(main())
