import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Diabetes')

#membagi colum
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('input nilai Pregnancies')

with col2 :
    Glucose = st.text_input ('input nilai Glucose')

with col1 :
    BloodPressure = st.text_input ('input nilai Blood Pressure')

with col2 :
    SkinThickness = st.text_input ('input nilai Skin Thickness')

with col1 :
    Insulin = st.text_input ('input nilai Insulin')

with col2 :
    BMI = st.text_input ('input nilai BMI')

with col1 :
    DiabetesPedigreeFunction = st.text_input ('input nilai Diabetes Pedigree Function')

with col2 :
    Age = st.text_input ('input nilai Age')

# code untuk prediksi
diab_diagnosis = ''

# membuat tombol prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabetes'
    else :
        diab_diagnosis = 'Pasien tidak terkena Diabetes'
        
    st.success(diab_diagnosis)

