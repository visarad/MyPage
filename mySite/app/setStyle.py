import streamlit as st

class style:

    def __init__(self):


        hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                footer:after {
                    content:' 😀 Made By Visarad 😀';
                    visibility: visible;
                    display: block;
                    position: relative;
                    #background-color: red;
                    padding: 5px;
                    top: 2px;
                }
                </style>
                """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

