import streamlit as st 


names = ['Karthik', 'Thallam']

code = """

for item in names:

	print(item)


	"""


st.code(code, language = 'python')

