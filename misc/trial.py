import streamlit as st
import setStyle

st.set_page_config(layout='wide')
    
menu = ['home','about']

choice = st.sidebar.selectbox('menu',menu)

if choice =='home':

    projects = ['ML',"DL","AI"]
    options = st.sidebar.selectbox('projects',projects)
    st.sidebar.image('imgaes/visu.png')

    if options=='ML':
        st.write("These are ml projects")

    elif options=='DL':
        st.write("These are dl projects")
    else:
        st.write("These are ai projects")


setStyle.style()
''' this is for testing purpose'''


