import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Cấu hình trang Streamlit
st.set_page_config(page_title="Phân tích Tỷ lệ sinh & CO2", layout="wide")

st.title("📊 Analysis Correlation: Birth rate, GDP and Annual CO2 Emissions")
st.markdown("""
Quantitive Research.
Data is visualized by Python Streamlit.
""")

# Đường dẫn file (Sử dụng đường dẫn tương đối để linh hoạt)
data_path = "finaltest/final_data_combined.csv"

@st.cache_data
def load_data():
    if os.path.exists(data_path):
        return pd.read_csv(data_path)
    return None

df = load_data()

if df is not None:
    # --- Sidebar: Bộ lọc ---
    st.sidebar.header("Data Filter")
    list_countries = sorted(df['Entity'].unique())
    selected_country = st.sidebar.selectbox("Choose the country to watch closely:", list_countries)

    # --- Layout chính ---
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("1. Phân bổ mật độ: Thực tế vs Dự báo")
        # Giải quyết vấn đề chồng chéo bằng Hexbin
        fig, ax = plt.subplots(figsize=(8, 6))
        hb = ax.hexbin(df['Birth.rate'], df['predicted_birth'], gridsize=30, cmap='mako', mincnt=1)
        ax.plot([df['Birth.rate'].min(), df['Birth.rate'].max()], 
                [df['Birth.rate'].min(), df['Birth.rate'].max()], 
                'r--', lw=2, label="Perfect Prediction")
        fig.colorbar(hb, ax=ax, label='Number of observation')
        ax.set_xlabel("Practical Birth rate")
        ax.set_ylabel("Prediction Birth rate")
        st.pyplot(fig)

    with col2:
        st.subheader(f"2. Chỉ số tại {selected_country}")
        country_data = df[df['Entity'] == selected_country]
        st.metric("Số lượng bản ghi", len(country_data))
        st.metric("Birth Rate trung bình", f"{country_data['Birth.rate'].mean():.2f}")
        
        # Biểu đồ nhỏ cho quốc gia được chọn
        fig2, ax2 = plt.subplots()
        sns.lineplot(data=country_data, x='Year', y='Birth.rate', ax=ax2, marker='o')
        st.pyplot(fig2)

else:
    st.error("Không tìm thấy file 'final_data_combined.csv'. Hãy kiểm tra lại thư mục làm việc!")
