import streamlit

streamlit.title('My family Designer shop PJ')
streamlit.header('Mens design')
streamlit.text('👕 Top')
streamlit.text('👖 Bottom')
streamlit.text('👓 Accessories')
streamlit.header('Womens design')
streamlit.text('👗 Dress')
streamlit.text('👙 Bikini')
streamlit.text('👜 Handbag')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
