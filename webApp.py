import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Upload CSV!")

uploaded_file = st.file_uploader("Choose a csv file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

  # # Add some matplotlib code !
  # fig, ax = plt.subplots()
  # df.hist(
  #   bins=8,
  #   column="imageName",
  #   grid=False,
  #   figsize=(8, 8),
  #   color="#86bf91",
  #   zorder=2,
  #   rwidth=0.9,
  #   ax=ax,
  # )
  # st.write(fig)
