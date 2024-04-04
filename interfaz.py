import streamlit as st
import pickle
from utilidades import vectorize
import joblib
from sklearn.preprocessing import FunctionTransformer
def clean_vectorize(text):
    vector = vectorize(text)
    vector = vector.reshape(-1,300)
    return vector
transformer = FunctionTransformer(clean_vectorize)
# Cargar el modelo entrenado desde el archivo Pickle (.pkl)
@st.cache(allow_output_mutation=True)


# Función para realizar la predicción
def predict_cancer(symptoms):
    prediction = modelo.predict([symptoms])
    return prediction[0]
st.title('Cancer Prediction')
st.write('Drop here your article to predict the type of cancer')

file = st.file_uploader("Upload file", type=["txt"])

if file is not None:
    codificaciones_a_probar = ["utf-8", "latin-1", "utf-16"]
    for codificacion in codificaciones_a_probar:
        try:
            file.seek(0)
            contenido = file.read().decode(codificacion)
            st.write(f"Archivo decodificado exitosamente con codificación: {codificacion}")
            break  # Salir del bucle si la decodificación fue exitosa
        except UnicodeDecodeError:
            print(f"No se pudo decodificar con la codificación: {codificacion}")
    contenido = ' '.join(contenido.split('\n'))
    modelo = joblib.load('grid.pkl')
    st.subheader("File Content:")
    st.text_area("Text", contenido, height=300)
    if st.button('Do prediction'):
        prediction = modelo.predict(contenido)    

        st.subheader("Resultado de la predicción:")
        st.write(f"El tipo de cáncer predicho es: {prediction}")