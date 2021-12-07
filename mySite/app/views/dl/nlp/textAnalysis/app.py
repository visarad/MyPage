import streamlit as st

def main():

    st.title('NLP App with Text Analysis')
    menu = ['Home','NLP (Files)','About']
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == 'Home':
        st.subheader("Analyse Text")
        raw_text = st.text_area("Enter Text Here......")
        if st.button("Analyse"):
            with st.expander('Raw Text'):
                st.write(raw_text)
        no_of_most_common = st.sidebar.number_input("Most Common Token",5,15)
        st.write(no_of_most_common)

    elif choice =='NLP (Files)':
        st.subheader('NLP Task') 
    else:
        st.subheader('About') 



if __name__ =='__main__':
    main()
        