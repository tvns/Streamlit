import streamlit as st 
import pandas as pd


df = pd.read_csv('USA_Housing.csv')


# Method1
#.........


st.dataframe(df.head())

st.dataframe(df.head(), width=1500, height=1000)

st.dataframe(df.style.highlight_max(axis=0))




# Method2
#.........

st.table(df.head(10))   #It will give static table



# Method3
#.........

st.write(df.head(20))


