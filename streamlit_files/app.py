# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("CSS 2026")
st.write("Day 3")
st.write("My first Streamlit App")
number = st.slider ("pick a number", 1, 100)

st.write(f" you picked {number}")

st.title("Heading 1")

st.markdown("some text that you can write")


# st.write("Hello2")

# st.title("Title heading")

# st.write("Hello, Streamlit!")

# st.header("Number selection")

# number = st.slider("Pick a number", 1, 100)
# st.write(f"You picked: {number}")