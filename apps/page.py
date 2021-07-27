import streamlit as st
from data_sources import source


def show():
    st.write("Hello!")
    st.write(source.get_data())