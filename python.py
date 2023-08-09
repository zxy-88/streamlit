import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import xml.etree.ElementTree as ET

st.set_page_config(page_title=None,layout='wide')

# -------------------- Upload File -------------------- #
st.title('Data Isurvey')

uploaded_file = st.file_uploader("เลือกไฟล์")

if uploaded_file is not None:

    root = ET.parse(uploaded_file)

    namespace = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}

    rows = root.findall("./ss:Worksheet/ss:Table/ss:Row", namespace)

    ap_ = []
    for c_row ,v_row in enumerate(rows):
        data_elements = v_row.findall("ss:Cell/ss:Data", namespace)
        # print(data_elements)

        for c_de,v_de in enumerate(data_elements):
            data_text = v_de.text
            ap_.append(data_text)

    ap_.pop(0)  # ลบ 'Report enquiry :Startdate 2023-07-20 to 2023-07-20 Export time [2023-07-21 12:46:28]'
    rows = root.findall("./ss:Worksheet/ss:Table/ss:Row", namespace)
    namespace = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}
    rows = root.findall("./ss:Worksheet/ss:Table/ss:Row/ss:Cell/ss:Data", namespace)
    sl = [ap_[i:i+44] for i in range(0, len(ap_), 44)]
    column = sl[0] # ตั้งชื่อ คอลัมน์
    sl.pop(0) # ลบหัวแถวออก
    df = pd.DataFrame(sl,columns=column) # สร้าง Dataframe

    # df = df[['เลขเคลม','เลขรับแจ้ง','เลขเซอเวย์','อำเภอที่เกิดเหตุ','จังหวัดที่เกิดเหตุ','อำเภอที่ออกตรวจสอบ','จังหวัดที่ออกตรวจสอบ','พนักงานตรวจสอบ','เหตุผลการจ่ายงาน','ใช้เซอร์เวย์นอก',
    # 'ประเภทเคลม(ว.4/นัดหมาย)','ใน/นอก(เวลางาน)','นอกพื้นที่','วันที่/เวลารับแจ้ง','วันที่/เวลาจ่ายงาน','วันที่/เวลารับงาน','วันที่/เวลาถึง ว.22','วันที่/เวลาเสร็จงาน ว.14','วันที่/เวลาส่งรายงาน','ผู้รับแจ้ง','ผู้จ่ายงาน','ผู้ตรวจสอบงาน','วันที่/เวลาตรวจสอบ','สถานะงาน']]


    # df = df.loc[df['สถานะงาน']=='จบงาน']

    st.write(df)

# -------------------- Download Button -------------------- #
    st.title('Download excel')
    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)

    st.download_button(
        label="Download Data",
        data=csv,
        file_name='จบงาน.csv',
        mime='text/csv',
    )

st.title('Streamlit')
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Random':np.random.randn(20),
    'Periods':pd.date_range("1/1/2000", periods=20)
}

df = pd.DataFrame(data)
st.bar_chart(df,x='Periods',y='Random',use_container_width=True)


st.title('Pandas')
#---------------------------------------------------------------------------------
import pandas as pd
import streamlit as st

# Cache the dataframe so it's only loaded once
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)

df3 = pd.DataFrame(np.random.randn(1000, 2), columns=["B", "C"]).cumsum()

df3["A"] = pd.Series(list(range(len(df))))

df3.plot(x="A", y="B")

st.line_chart(df3)


st.title('Plotly')
import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
# fig.show()
st.plotly_chart(fig,use_container_width=True)

