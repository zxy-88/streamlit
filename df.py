import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import xml.etree.ElementTree as ET

dfx = pd.read_csv('จบงาน.csv')

dfx = dfx.dropna()

dfx = dfx[['พนักงานตรวจสอบ','เลขเคลม','ใช้เซอร์เวย์นอก','ประเภทเคลม(ว.4/นัดหมาย)','วันที่/เวลารับงาน','วันที่/เวลาส่งรายงาน']]

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


indexs = pd.DataFrame(count,columns=['ลำดับ'])

df =  pd.concat([indexs,dfx],axis=1)

st.dataframe(df.set_index(df.columns[0]))

st.title('Timeline')

fig = px.timeline(df,x_start=df['วันที่/เวลารับงาน'],x_end=df['วันที่/เวลาส่งรายงาน'],y=df['เลขเคลม'])
fig.update_yaxes(autorange='reversed')
st.plotly_chart(fig)

# df = pd.DataFrame([
#     dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
#     dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
#     dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30'),
#     dict(Task="Job D", Start='2009-01-01', Finish='2009-02-28'),
#     dict(Task="Job E", Start='2009-03-05', Finish='2009-04-15'),
#     dict(Task="Job F", Start='2009-02-20', Finish='2009-05-30')
# ])

# fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
# fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
# st.plotly_chart(fig)

