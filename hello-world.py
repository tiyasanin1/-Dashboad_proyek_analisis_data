import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import datetime


st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

st.header('Pengembangan Dashboard')
st.subheader('Pengembangan Dashboard')
st.caption('Copyright (c) 2023')

code="""def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.text('Halo, calon praktisi data masa depan.')


st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r})\right)
""")

df=pd.DataFrame({
    'c1':[1,2,3,4],
    'c2':[10,20,30,40],
})
st.table(data=df)

st.metric(label='Temperature', value='28 °C', delta='1.2 °C')

st.json({
    'c1':[1,2,3,4],
    'c2':[10,20,30,40],
})



name=st.text_input(label='Nama lengkap', value='')
st.write('Nama:', name) 

text=st.text_area('Feedback')
st.write('Feedback: ', text)

number=st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

date=st.date_input(label='Tanggal lahir', min_value=datetime.date(1900,1,1))
st.write('Tanggal lahir:', date)

with st.container():
    st.write('Inside the container')
    x=np.random.normal(15, 5, 250)
    fig, ax= plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig)
with st.expander('see explanation'):
    st.write(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    )


st.title('Belajar Analisis Data')
tab1, tab2, tab3= st.tabs(['Tab 1','Tab 2','Tab 3'])

with tab1:
    st.header('Tab 1')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with tab2:
    st.header('Tab 2')
    st.image('https://static.streamlit.io/examples/dog.jpg')
with tab3:
    st.header('Tab 3')
    st.image('https://static.streamlit.io/examples/owl.jpg')


