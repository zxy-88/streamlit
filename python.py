import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.title('Data Isurvey')
uploaded_file = st.file_uploader('Upload Your File Here')

if uploaded_file:
    st.header('Data Statistics')
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())

    st.header('Data Header')
    st.write(df.head())

    fig,ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'],y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)
 

import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# ตัวอย่างข้อมูลสำหรับการสร้างกราฟ
data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'Revenue': [100, 200, 150, 300, 250]
}
df = pd.DataFrame(data)

# เริ่มต้นใช้ Streamlit
st.title('Charts with Streamlit')

# ใช้ Matplotlib เพื่อสร้างกราฟแท่ง (Bar chart)
st.subheader('Bar Chart with Matplotlib')
fig, ax = plt.subplots()
ax.bar(df['Month'], df['Revenue'])
st.pyplot(fig)

# ใช้ Plotly เพื่อสร้างกราฟแท่ง (Bar chart)
st.subheader('Bar Chart with Plotly')
fig = px.bar(df, x='Month', y='Revenue', title='Revenue by Month')
st.plotly_chart(fig)
#-----------------------------------------------------------------------------------------------------

import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# ตัวอย่างข้อมูลสำหรับการสร้างกราฟ
data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'Revenue': [100, 200, 150, 300, 250]
}
df = pd.DataFrame(data)

# เริ่มต้นใช้ Streamlit
st.title('Charts with Streamlit')

# ใช้ Matplotlib เพื่อสร้างกราฟแท่ง (Bar chart) แนวนอน
st.subheader('Bar Chart with Matplotlib (Horizontal)')

fig, ax = plt.subplots()
ax.barh(df['Month'], df['Revenue'])
st.pyplot(fig)

# ใช้ Plotly เพื่อสร้างกราฟแท่ง (Bar chart)
st.subheader('Bar Chart with Plotly (Vertical)')

fig = px.bar(df, x='Revenue', y='Month', orientation='h', title='Revenue by Month')
st.plotly_chart(fig)

#-----------------------------------------------------------------------------------------------------

# import streamlit as st
# import matplotlib.pyplot as plt
# import plotly.express as px
# import pandas as pd

# # ตัวอย่างข้อมูลสำหรับการสร้างกราฟ
# data = {
#     'Month': ['January', 'February', 'March', 'April', 'May'],
#     'Revenue': [100, 200, 150, 300, 250]
# }
# df = pd.DataFrame(data)

# # เริ่มต้นใช้ Streamlit
# st.title('Charts with Streamlit')

# # ใช้ Matplotlib เพื่อสร้างกราฟแท่ง (Bar chart) แนวนอน
# st.subheader('Bar Chart with Matplotlib (Horizontal)')
# fig, ax = plt.subplots()
# ax.barh(df['Month'], df['Revenue'])
# st.pyplot(fig)

# # ใช้ Plotly เพื่อสร้างกราฟแท่ง (Bar chart)
# st.subheader('Bar Chart with Plotly (Vertical)')
# fig = px.bar(df, x='Month', y='Revenue', title='Revenue by Month')
# st.plotly_chart(fig)

import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# ตัวอย่างข้อมูลสำหรับการสร้างกราฟ
l1 = ['January', 'February', 'March', 'April', 'May']
l2 = [100, 200, 150, 300, 250]

data = {
    'Month': l1,
    'Revenue': l2
}
df = pd.DataFrame(data)

# เริ่มต้นใช้ Streamlit
st.title('Charts with Streamlit')

# ใช้ Matplotlib เพื่อสร้างกราฟแท่ง (Bar chart) แนวนอน
st.subheader('Bar Chart with Matplotlib (Horizontal)')

fig, ax = plt.subplots()
ax.barh(df['Month'], df['Revenue'])
st.pyplot(fig)

# ใช้ Plotly เพื่อสร้างกราฟแท่ง (Bar chart)
st.subheader('Bar Chart with Plotly (Vertical)')

fig = px.bar(df, x='Revenue', y='Month', orientation='h', title='Revenue by Month')
st.plotly_chart(fig)

#-----------

df = pd.read_csv(r'C:\Users\88888888\Desktop\streamlit\kaggle_significant_earthquakes_database.csv')
st.write(df.describe())

st.header('Data Header')
st.write(df.head())

fig,ax = plt.subplots(1,1)
ax.scatter(x=df['Depth'],y=df['Magnitude'])
ax.set_xlabel('Depth')
ax.set_ylabel('Magnitude')

st.pyplot(fig)

fig, ax = plt.subplots()
ax.barh(df['Magnitude'], df['Depth'])

st.pyplot(fig)

fig = px.bar(df, x='Depth', y='Magnitude', orientation='h', title='Revenue by Month')
st.plotly_chart(fig)


