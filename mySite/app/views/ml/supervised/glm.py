import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_selection import VarianceThreshold
from numpy import unique
import re

class glm:

    def __init__(self):
        st.markdown("### Start of Data Cleaning",unsafe_allow_html=True)
        df = None
        file = st.file_uploader("Upload Files",['csv','xls'])
        flag= 1
        df,flag = glm.file_selector(file,flag)
        df,flag = glm.data_cleaning(df,flag)
        df,flag = glm.data_imputation(df,flag)
        model,flag = glm.linear_model_selection(flag)

    def data_cleaning(df,flag):
        if flag:
            
            st.markdown(""" ### Removing duplicate rows """)
            st.write("Data Shape",(df.shape[0],df.shape[1]), " before Removal")
            df.drop_duplicates(inplace=True)
            st.write("Data Shape",(df.shape[0],df.shape[1]), " after Removal")

            counts = df.nunique()

            """ Removing features with unique values"""

            st.write("Data Shape",(df.shape[0],df.shape[1]), " before Removal")
            index = [i for i,v in enumerate(counts) if v<=1]
            st.write('the following columns with 0 or 1 unique values can be removed')
            cols = df.iloc[:,index].columns
            st.write(cols)
            df.drop(cols,axis=1,inplace=True)
            st.write("Data Shape",(df.shape[0],df.shape[1]), " After Removal")

            """ Removing features with little variance or no variance"""
            num_cols,cat_cols = glm.cat_num_cols(df) 
            if st.checkbox("data frame with only numerical features"):
                st.write(df[num_cols].head(10))  
                st.write(df[num_cols].shape[0],df[num_cols].shape[1])
            
            if st.checkbox("data frame with only categorical features"):
                st.write(df[cat_cols].head(10))  
                st.write(df[cat_cols].shape[0],df[cat_cols].shape[1])
            
            sel = VarianceThreshold(threshold=0.05)

            def clean(x):
                x = re.sub("[a-zA-Z +%~!@#$%^&*<>()-+=]","",str(x))
                if x == '':
                    x=0
                return float(x)

            if st.checkbox("Want to Change some categorical features to numerical?"):
                features = st.multiselect("Enter the categorical features that can be converted to numerical features",cat_cols)    
                final = []
                if features:
                    for col in features:
                        df[col]=df[col].apply(clean)
                        final.append(col)
                st.write(df.head(10))
         
        return df, 0

    def file_selector(file,flag):
        if flag:
            if file == None:
                st.warning('Please upload File')    
                flag=0
            elif file.type =='text/csv':
                df = pd.DataFrame(pd.read_csv(file))
            elif file.type in ['text/xls','text/xlsx']:
                df = pd.DataFrame(pd.read_excel(file))
            
            if  file !=None:
                row = st.number_input("Select the number of rows to display",min_value=1,max_value=df.shape[0])
                st.dataframe(df.head(row))
            else:
                df =None
                flag = 0

        return df,flag

    def linear_model_selection(flag):
        if flag:
            menu = ['Linear Regression','Logistic Regression']
            choice = st.radio("Pick the model",menu)

            if choice=='Linear Regression':
                st.write('Linear Regression')
            elif choice=='Logistic Regression':
                st.write('Logistic Regression')

            return choice,flag
        
        return '',flag
    
    def data_imputation(df,flag):
        if flag:
            
            st.write('Finding Missing Values...') 

            temp = pd.DataFrame(columns=['i','missing_values','Percent of Total Observations'])
            for n,i in enumerate(df.columns):
            # count number of rows with missing values
                n_miss = df[i].isnull().sum()
                perc = n_miss / df.shape[0] * 100
                temp.loc[n,:] = [i,n_miss,perc]
                
            st.table(temp) 

            st.write("the data type of the converted features will be string")
            n_impute = ['mean','median','mode'] + ['cluster mean','cluster Mode','cluster Median']
            c_impute = ['cluster Based']
            choice = st.radio("select the Imputation methods to apply",n_impute,)

            if choice in n_impute:
                st.write('{} imputation will be applied'.format(choice))



        return df,flag

    def cat_num_cols(df):
        num_cols =[]
        cat_cols =[]
        for col in df.columns:
            if df[col].dtype in ['float64','float32','float16' ,'int64','int32','int16','int8'] : 
                num = len(unique(df.loc[:,col]))
                num_cols.append(col)
            else:
                cat_cols.append(col)
        return num_cols,cat_cols





