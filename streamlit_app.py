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
#streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#display the table on the page
streamlit.dataframe(my_fruit_list)
