import streamlit as st
import pandas as pd
from views import home,about


def main():
    st.title(" 👈 Select the Apps from the sidebar")
    menu = ["Calc",'Other']
    choice = st.sidebar.selectbox("Menu",menu,)
    if choice =='Calc':
        home.Calc()
    elif choice=='Other':
        about.about()























    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                content:' 😀 Made By Visarad 😀 ' ; 
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




if __name__ =='__main__':
    main()