import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():

	df = pd.read_csv('USA_Housing.csv')

	st.dataframe(df)


	# using pyplot function:
	#.......................................................................

	fig = plt.figure()
	sns.distplot(df['Price'])
	st.pyplot(fig)


	fig1 = plt.figure()
	cor = df.corr()
	st.dataframe(cor)
	sns.heatmap(cor , annot = True)
	st.pyplot(fig1)



	# using streamlit inbuilt functions
	#.......................................................................

	lang = pd.read_csv('lang_data.csv')
	st.dataframe(lang)

	list = lang.columns.tolist()
	selection = st.multiselect('Select your language', list, default='Python')


	data = lang[selection]
	st.line_chart(data)


main()