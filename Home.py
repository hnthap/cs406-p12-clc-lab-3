import streamlit as st


def main():
    title = 'Image Enhancements'
    st.set_page_config(title, '🥰', 'centered')
    with open('README.md', 'rt') as f:
        content = f.read()
        header, content = content.split('\n', 1)
        st.markdown(header)
        with st.container(border=True):
            st.text('🔰   Select a demo from the sidebar...')
        st.markdown(content)


if __name__ == '__main__':
    main()
