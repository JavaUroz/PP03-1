from types import MappingProxyType
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset('mpg')
registros = len(mpg)
atributos = mpg.shape
tipos = mpg.dtypes.astype(str)
estadistico = mpg.describe()
categorias = mpg.species.unique()
g = sns.pairplot(mpg, hue='species')

def show_explore_page():
    st.title("Explorador de la fuente de  datos")
    st.subheader("Vista general del dataset")
    col1, col2 = st.columns(2)
    col1.metric("Registros", registros)
    col2.metric("Atributos", atributos[1]-1)

    st.subheader("Estructura de datos del dataset")
    st.write(tipos)

    st.subheader("Valores de la variable categórica")
    st.dataframe(categorias)

    st.subheader("Resumen estadístico")
    st.dataframe(estadistico)

    st.subheader("Vista detallada de los registros")
    st.dataframe(mpg)

    st.write("""#### Relaciones entre atributos""")

    st.pyplot(g)


show_explore_page()
