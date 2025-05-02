import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px 
import pickle
with open("model.pickle","rb") as m:
    model = pickle.load(m)

wage = pd.read_csv('tallerivansamuel.csv')

st.title("Taller Ivan Samuel prediccion")

tab1, tab2, tab3 = st.tabs(['Tab 1','Tab 2', 'Tab 3'])

with tab1:

    fig, ax = plt.subplots(1,6 ,  figsize=(10,4))

    tab_freq = wage['mujer'].value_counts().sort_index()
    ax[0].bar(tab_freq.index, tab_freq.values)

    tab_freq = wage['mujer'].value_counts().sort_index()
    ax[1].bar(tab_freq.index,tab_freq.values)


    ax[2].hist(wage['años_de_experiencia_expotencial'], bins =30)


    ax[3].hist(wage['años_empleador'], bins =30)

    ax[4].hist(wage['años_de_educacion'], bins =30)


    ax[5].hist(wage['ingresos_por_hora'], bins =30)




    st.pyplot(fig)


with tab2:

    fig, ax = plt.subplots(1, 5, figsize=(10,4))
    ax[0].scatter(wage['años_de_educacion'],wage['ingresos_por_hora'])

    ax[1].scatter(wage['años_de_experiencia_expotencial'],wage['ingresos_por_hora'])

    ax[2].scatter(wage['años_empleador'],wage['ingresos_por_hora'])

    
    ax[3].scatter(wage['mujer'],wage['ingresos_por_hora'])
    ax[4].scatter(wage['casados'],wage['ingresos_por_hora'])





    








    st.pyplot(fig)

with tab3:

    años_de_educacion = st.slider("Años de educacion",0,20)
    años_de_experiencia_expotencial = st.slider("Años de experiencia potencial",0,40)
    años_empleador = st.slider("Años en la empresa actual",0,50)
    mujer = st.selectbox('Sexo',['Femenino','Masculino'])
    if mujer == 'Femenino' :
        mujer = 1
    else:
        mujer = 0
        

        
    casados = st.selectbox('Estado civil',['Casado','Soltero'])
    if casados == 'Casado' :
        casados = 1
    else:
        casados = 0
        
    if st.button("Predecir"):

        pred = model.predict(np.array([[años_de_educacion,
                                     años_de_experiencia_expotencial,
                                     años_empleador,
                                     mujer,
                                     casados]]))
        st.write(pred[0])
