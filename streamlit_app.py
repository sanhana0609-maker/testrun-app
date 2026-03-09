import streamlit as st

from utlis.dataprocessing import data
st.title("Testrunapp")
st.write("Duchuy")
  #  "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."

st.divider()
st.subheader("Dữ liệu tội phạm (Raw Data)")
st.dataframe(data)

my_numbers = [1,2,3]
st.divider()
st.line_chart(my_numbers)
 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- CẤU HÌNH TRANG (Phải là lệnh Streamlit đầu tiên) ---
st.set_page_config(page_title="Phân tích Tỷ lệ sinh & CO2", layout="wide")

# --- PHẦN 1: TEST RUN (Phần đầu của bạn) ---
st.title("🚀 Testrunapp")

st.write(
    "Author: **Đức Huy**")

st.divider()

# 3. PHẦN PHÂN TÍCH CHÍNH
st.title("📊 Analysis Correlation: Birth rate, GDP and Annual CO2 Emissions")
st.markdown("""*Quantitive Research Project.*
Data is visualized by Python Streamlit.
""")

# Đường dẫn file (Bạn hãy kiểm tra lại folder finaltest có tồn tại không)
data_path = "finaltest/final_data_combined.csv"

@st.cache_data
def load_data():
    if os.path.exists(data_path):
        return pd.read_csv(data_path)
    return None

df = load_data()

if df is not None:
    st.success("Đã tải dữ liệu thành công!")
    # Tiếp tục các phần vẽ biểu đồ của bạn ở đây...
else:
    st.error(f"Không tìm thấy file tại: {data_path}")