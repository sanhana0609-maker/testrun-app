import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- CẤU HÌNH TRANG (Phải là lệnh Streamlit đầu tiên) ---
st.set_page_config(page_title="Phân tích Tỷ lệ sinh & CO2", layout="wide")

# --- PHẦN 1: TEST RUN (Phần đầu của bạn) ---
st.title("🚀 Testrunapp")
st.write("Author: **Đức Huy**")

# Giả sử bạn có module xử lý tội phạm, nếu không dùng hãy comment lại
# from utlis.dataprocessing import data 
# st.subheader("Dữ liệu tội phạm (Raw Data)")
# st.dataframe(data)

st.divider()

# --- PHẦN 2: PHÂN TÍCH CHÍNH ---
st.title("📊 Analysis Correlation: Birth rate, GDP and Annual CO2 Emissions")

# Đường dẫn file (Đảm bảo file nằm trong thư mục finaltest/)
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
        # Hexbin giúp tách các điểm bị chồng chéo (Overplotting)
        fig, ax = plt.subplots(figsize=(8, 6))
        hb = ax.hexbin(df['Birth.rate'], df['predicted_birth'], gridsize=30, cmap='mako', mincnt=1)
        
        # Vẽ đường dự báo hoàn hảo
        ax.plot([df['Birth.rate'].min(), df['Birth.rate'].max()], 
                [df['Birth.rate'].min(), df['Birth.rate'].max()], 
                'r--', lw=2, label="Perfect Prediction")
        
        fig.colorbar(hb, ax=ax, label='Number of observations')
        ax.set_xlabel("Practical Birth Rate")
        ax.set_ylabel("Predicted Birth Rate")
        st.pyplot(fig)

    with col2:
        st.subheader(f"2. Chỉ số tại {selected_country}")
        country_data = df[df['Entity'] == selected_country]
        
        # Hiển thị Metrics
        st.metric("Số lượng bản ghi", len(country_data))
        st.metric("Birth Rate trung bình", f"{country_data['Birth.rate'].mean():.2f}")
        
        # Biểu đồ xu hướng quốc gia
        st.write("**Xu hướng tỷ lệ sinh:**")
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        sns.lineplot(data=country_data, x='Year', y='Birth.rate', ax=ax2, marker='o', color='teal')
        plt.xticks(rotation=45)
        st.pyplot(fig2)

else:
    st.error(f"❌ Không tìm thấy file tại đường dẫn: {data_path}")
    st.info("Mẹo: Hãy đảm bảo bạn đã tạo thư mục 'finaltest' và copy file CSV vào đó.")