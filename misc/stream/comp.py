import streamlit as st
import streamlit.components.v1 as stc


def main():
    st.title("components")

    stc.html("<p   style='color:red;'> Streamlit is awesome</p>")
    st.markdown("<p   style='color:red;'> Streamlit is awesome</p>",unsafe_allow_html=True)

if __name__=="__main__":
    main()
    