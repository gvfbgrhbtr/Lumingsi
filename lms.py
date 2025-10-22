import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(
   [
      ["龙门花甲",22.817287 , 108.321617],
      ["家卫杀猪粉店", 22.817629, 108.323023],
      ["梁小糖", 22.817194, 108.320974],
      ["瑶家食府", 22.818558, 108.322873],
      ["螺公堂", 22.817441, 108.321735]
   ],
    columns=["店名", "latitude", "longitude"])
df.index.name="序号"
st.subheader("👀各家店所在:red[位置]")
st.map(df)

data = {
    '月份':['01月', '02月', '03月', '04月', '05月', '06月'],
    '龙门花甲':[4.7, 4.8, 4.7, 4.9, 4.8, 4.9],
    '家卫杀猪粉店':[4.5, 4.4, 4.6, 4.7, 4.6, 4.8],
    '梁小糖':[4.3, 4.2, 4.4, 4.5, 4.6, 4.7],
    '瑶家食府':[4.6, 4.7, 4.5, 4.6, 4.4, 4.5],
    '螺公堂':[4.8, 4.8, 4.9, 4.9, 4.8, 4.9],
}
df = pd.DataFrame(data)
st.subheader("⭐各门店月度:red[评分]")
df_chart = df.set_index("月份")
st.bar_chart(df_chart)


data = {
'店名': ['龙门花甲', '家卫杀猪粉店', '梁小糖', '瑶家食府', '螺公堂'],
'人均价格(元)': [30,50,15,70,60], 
}
df = pd.DataFrame(data)
st.subheader("💸各家店的:red[人均价格]")
df_chart = df.set_index("店名")
st.line_chart(df_chart)
data = {
    '时段':['11:30-13:30', '14:00-16:00', '17:30-19:30', '19:00-23:00'],
    '龙门花甲--':[5, 2, 4, 3],
    '家卫杀猪粉店':[2, 1, 3, 5],
    '梁小糖':[2, 4, 3, 4],
    '瑶家食府':[3, 1, 5, 4],
    '螺公堂':[5, 2, 4, 3],
}
df = pd.DataFrame(data)
st.subheader("⏰各家店:red[用餐高峰时段]")
st.area_chart(df, x='时段')
df.set_index('时段', inplace=True)
