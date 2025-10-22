import streamlit as st
import pandas as pd
st.title("  学生小雪数字档案")
st.header("🍭基本信息")
st.write("学生ID：NEO-2023-001")
st.write("注册时间：2023—10—08 08:30:17|精神状态：✅正常")
st.write("当前位置：实训楼3楼|安全等级：高级")
st.subheader("📊技能矩阵")
c1,c2,c3=st.columns(3)
c1.metric(label="C语言",value="95%",delta="2%")
c2.metric(label="Python",value="87%",delta="-1%")
c3.metric(label="Java",value="68%",delta="-10%")

st.subheader("Streamlit课程进度")
st.progress(50,text="Streamlit课程进度")
st.subheader("📝任务日志")
data={
    '日期':["2023-10-01","2023-10-05","2023-10-12"],
    '任务':["学生数值档案","课程管理系统","数据图表展示"],
    '状态':["完成","进行中","未完成"],
    '难度':["⭐⭐","⭐️⭐️⭐️","⭐️⭐️⭐️⭐️"]
    }
st.dataframe(data)
st.subheader("最新代码结果")
str='''
def matrix_breach():
    while True:
        if detect_vulnerability():
            exploit()
            reture"ACCESS GRANTED"
        else:
            stealth_evade()
'''
st.code(str,language=None)
st.caption("》SYSTEM MESSAGE:下一个任务目标已解锁……")
st.caption("》TASK:课程管理系统")
st.caption("》CONTINUE:2025-06-03 15:24:58")
st.caption("》系统状态：在线|健康状态：已加强")


