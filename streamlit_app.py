import streamlit as st

st.title('🎈 My Project') 

st.write('Welcome to my page!')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

with st.expender('Data')
  st.write('X')
  X_raw = df.drop('species', axis=1)
  st.dataframe(X_raw)

  st.write("y")
  y_raw = df.species
  st.dataframe(y_raw)
