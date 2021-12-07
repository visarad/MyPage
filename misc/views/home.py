import streamlit as st
import pandas as pd


class Calc:
    def __init__(self):
        st.write('This is a calculator')
        with st.form(key='form1'):
            firstname=st.text_input('Enter Frist Name:')
            Lastname=st.text_input('Enter Last Name:')
            dob = st.date_input("Date of Birth")
            submit_bottom = st.form_submit_button(label='SignUp ')
            if submit_bottom:
                if firstname=="" or Lastname=="":
                    st.error("First or last name Missing")
                else:
                    st.success('Hello {}, You\'re successfully signed up'.format(firstname+' '+Lastname))
        
        form2 = st.form(key="form2")
        job= form2.selectbox("job",['Data Scientist',"Machine Learning Expert",
                            "AI expert","DL Expert"])
        submit_bottom2 = form2.form_submit_button("login")
        
        if submit_bottom2:
             st.success('Hello {}, You\'re successfully signed in as {}'\
                            .format(firstname+' '+Lastname,job))

        with st.form(key='salary'):
            col1,col2 = st.columns([1,2])
            col3,col4 = st.columns([4,3])

            with col1:
                hours = st.number_input("Hours worked")
            with col2:
                amount = st.number_input("Hourly Rate in $")
            with col3:
                h_p_w = st.number_input("Hour per Week")
            with col4:
                st.text('salary')
                submit_salary=st.form_submit_button(label='calculate')

        if submit_salary:
            with st.expander("results"):
                daily = [amount * hours]
                weekly =amount * hours*h_p_w
                if weekly <=0.0 or hours>24:
                    st.error('Wrong Information')
                else:
                    df = pd.DataFrame({'Hourly':amount,
                                    'daily':daily,
                                    'weekly':weekly})
                    st.dataframe(df.T)
                    



        

        
        

