import streamlit as st
import views.dl
import views.ml.supervised.glm as glm
import views.ml.unsupervised.clustering as cluster 



class Projects:

    def __init__(self):

        items = ['select','Machine Learning',"Deep Learning"]
        choice= st.sidebar.selectbox("projects",items)
        if choice !='select':
            st.markdown('### You have chosen {} Projects'.format(choice))
        else:
            for i in range(4):
                st.markdown("##  ")
            st.markdown('### 👈	 Please select type of Learning from the list')

        if choice == 'Machine Learning':    
            idea = ['Select','Supervised','Unsupervised']
            choice= st.sidebar.selectbox("Learning Type",idea)
            if choice !='Select':
                st.markdown('### You have chosen {} Learning'.format(choice))
                st.empty()
            else:
                for i in range(5):
                    st.markdown("##  ")
                st.markdown('### 👈	 Please select type of Models from the list')

            if choice =="Supervised":
                glm.glm()
            if choice =='Unsupervised':
                cluster.Cluster()

        elif choice == 'Deep Learning':
            pass

