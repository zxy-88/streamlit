import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import xml.etree.ElementTree as ET

df = pd.read_csv(r'/Users/macmini/Desktop/streamlit/จบงาน.csv')

df = df[['พนักงานตรวจสอบ','ใช้เซอร์เวย์นอก','ประเภทเคลม(ว.4/นัดหมาย)','วันที่/เวลารับงาน','วันที่/เวลาส่งรายงาน']]

df = df.loc[ (df['ใช้เซอร์เวย์นอก']=='ไม่ใช้') & (df['ประเภทเคลม(ว.4/นัดหมาย)']=='เคลมสด')  ]

df = df.dropna()

'''
เงื่อนไข
    1. คอลัมน์ พนักงานตรวจสอบ เคลมสด ไม่ใช้เซอร์เวย์นอก วันที่/เวลารับงาน วันที่/เวลาส่งรายงาน
    2. ลบคอลัมน์ Unnamed: 0
'''

df.reset_index(inplace=True,drop = True)

st.dataframe(df.set_index(df.columns[0])) # ไม่โชว์คอลัมน์ index ใน streamlit
st.dataframe(df) # ไม่โชว์คอลัมน์ index ใน streamlit



