import pandas
import streamlit
streamlit.text("Hi Kitchen people")
my_fru_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fru_list)
