import streamlit as st

st.write(st.user.email)

st.write(st.user)

x = st.slider("X:", 0, 100, 5)
st.write(x**2)
