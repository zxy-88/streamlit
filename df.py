import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import xml.etree.ElementTree as ET

dfx = pd.read_csv(r'/Users/macmini/Desktop/streamlit/จบงาน.csv')

dfx = dfx.dropna()

dfx = dfx[['พนักงานตรวจสอบ','ใช้เซอร์เวย์นอก','ประเภทเคลม(ว.4/นัดหมาย)','วันที่/เวลารับงาน','วันที่/เวลาส่งรายงาน']]

dfx = dfx.loc[ (dfx['ใช้เซอร์เวย์นอก']=='ไม่ใช้') & (dfx['ประเภทเคลม(ว.4/นัดหมาย)']=='เคลมสด')  ]



'''
เงื่อนไข
    1. คอลัมน์ พนักงานตรวจสอบ เคลมสด ไม่ใช้เซอร์เวย์นอก วันที่/เวลารับงาน วันที่/เวลาส่งรายงาน
    2. ลบคอลัมน์ Unnamed: 0
'''

dfx.reset_index(inplace=True,drop = True)

# st.dataframe(dfx.set_index(dfx.columns[0])) # ไม่โชว์คอลัมน์ index ใน streamlit
# st.dataframe(dfx) # ไม่โชว์คอลัมน์ index ใน streamlit

count = []
for i in range(len((dfx['ใช้เซอร์เวย์นอก']))):
    ans = i+1
    count.append(ans)
    print(ans)

indexs = pd.DataFrame(count,columns=['ลำดับ'])

df =  pd.concat([indexs,dfx],axis=1)

st.dataframe(df.set_index(df.columns[0]))
