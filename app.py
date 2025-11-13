# This app was written by Geemini Flass2.5, on Nov 7, 2025.
# It was the response of this prompt:

"""
create a simple streamlit that does the following:
- uses the titanic dataset
- on the sidebar it has a menu of five different exploratory analysis that it can do with the dataset
- whenever one clicks a menu item, we see the analysis on the main page
- the main page should have some widget that allow for some control over the graphs, such as dropdown for choosing values, or something else
Do not write complex code, keep it simple.
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime
from datetime import time

st.header("Hello world")

df = pd.read_csv('st04_data copy.csv')

st.write(df.head())