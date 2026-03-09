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
 