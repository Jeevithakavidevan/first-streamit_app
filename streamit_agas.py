import pandas
import streamlit
streamlit.text("Hi Kitchen people")
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.dataframe(fruits_to_show)
