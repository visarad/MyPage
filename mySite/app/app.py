import streamlit as st
from views.aboutme import aboutMe
from views.home import Home
from views.contactme import contactMe
from views.projects import Projects
import setStyle

def main():

    menu = ['Home','Projects','About Me','Contact Me']

    choice = st.sidebar.selectbox('Menu',menu)

    if choice =="Home":
        Home()
    elif choice =="Projects":
        Projects()
    elif choice =="About Me":
        aboutMe()
    else:
        contactMe()

    setStyle.style()


if __name__=="__main__":
    main()

