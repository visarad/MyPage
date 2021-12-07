from numpy.core.fromnumeric import size
import streamlit as st

def main():

    st.title("StreamLit App")
    st.subheader('Hello User')

    menu = ['Home','Projects','About']
    choice = st.sidebar.selectbox("Menu",menu)
    st.sidebar.image('visu.png')

    
    
    if choice =='Home':
        st.subheader('Home')
   
    elif choice =='Projects':
        st.subheader('Please select any of the Projects to Check')
        projects = ["NLP","Computer Vision",'Face detection']
        selection = st.selectbox('Projects',projects)

        if selection == 'NLP':
            st.subheader('NLP')
            with st.form(key='nlpForm'):
                raw_text = st.text_area("Enter Test:")
                submit = st.form_submit_button('Analyze')
        
        elif selection == 'Computer Vision':
            st.subheader('Computer Vision')
            with st.form(key='nlpForm'):
                file = st.file_uploader(label="upload")
                submit = st.form_submit_button('submit')
                
            
    
    else:
        st.subheader('About')


if __name__ == '__main__':
    main()



    
