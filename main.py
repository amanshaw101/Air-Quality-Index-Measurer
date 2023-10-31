'''python -m streamlit run main.py'''
import streamlit as st
import pickle as pkl
import sklearn
import numpy as np
import pydeck as pdk
import plotly.express as px

model = pkl.load(open('model.pkl', 'rb'))
df1 = pkl.load(open('df2.pkl', 'rb'))

st.set_page_config(page_title="APP PROJECT",
                   page_icon=":cloud:",
                   layout="centered")
st.sidebar.title("Please Enter the City name")
option = st.sidebar.selectbox('', ('LUCKNOW', 'MUMBAI', 'DELHI', 'KOLKATA', 'CHENNAI'))


if option == 'LUCKNOW':
    a = 26.8467
    b = 80.9462
elif option == 'MUMBAI':
    a = 19.0760
    b = 72.8777
elif option == 'DELHI':
    a = 28.7041
    b = 77.1025
elif option == 'KOLKATA':
    a = 22.5726
    b = 88.3639
elif option == 'CHENNAI':
    a = 13.0827
    b = 80.2707

st.title('Enter The Values')

PM2_5 = st.number_input('PM2.5')
PM10 = st.number_input('PM10')
NO2 = st.number_input('NO2')
CO = st.number_input('CO')
SO2 = st.number_input('SO2')
O3 = st.number_input('O3')

if st.button('CHECK AQI'):
    query = np.array([PM2_5, PM10, NO2, CO, SO2, O3])
    query = query.reshape(1, 6)
    ans = model.predict(query)
    st.title(*ans)

    if (ans > 0 and ans <= 50):
        st.subheader("GOOD")
    elif (ans > 50 and ans <= 100):
        st.subheader("SATISFACTORY")
    elif (ans > 100 and ans <= 250):
        st.subheader("MODERATELY POLLUTED")
    elif (ans > 250 and ans <= 300):
        st.subheader("POOR")
    elif (ans > 300 and ans <= 400):
        st.subheader("VERY POOR")
    else:
        st.subheader("Severe")

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude= a,
            longitude= b,
            zoom=11,
            pitch=50,
        )))

