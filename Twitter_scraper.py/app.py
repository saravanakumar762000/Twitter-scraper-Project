import streamlit as st
from fuction import scraping, upload_in_Mongo
import time

st.set_page_config(
    page_title="Twitter Scraper",
    page_icon="😀"
    
    )

st.title('Twitter Scraping')



search_term=st.text_input("Please enter the search term")
since=st.date_input("please enter the start date to search: ")
until=st.date_input("please enter the end date to search: ")
tweets=st.slider("How many Tweets?",0,5000,step=5)

submit=st.button("search")

df= scraping(search_term=search_term, since=since, until=until, number_of_tweets=tweets)

if submit:
    st.write("Display the tweets")
    st.progress(100)
    st.dataframe(df.iloc[0:50])
    st.success(f"{search_term} is successfully scrapped from twitter")

upload=st.button("upload in MongoDB")


if upload:
    upload_in_Mongo(search_term=search_term)
    st.success(f"{search_term} is successfully uploaded")
    
download=st.radio('want to save file as CSV/JSON?',['Yes','No'])
file=st.text_input("Name the file:")

if download=='Yes':
    choice=st.radio("select the file format:",['CSV','JSON'])
    if choice=="CSV":
        st.download_button(
            label="Download data csv",
            data=df.to_csv(),
            file_name=f"{file}.csv",
            mime='text/csv'
            )
        st.success("CSV is downloaded")
    else:
        st.download_button(
            label="Download data as json",
            data=df.to_json(),
            file_name=f"{file}.json",
            mime='application/json'         
            )
        st.success("JSON is downloaded")
    st.subheader("Thanks for using")
  

else:
    st.subheader("Thank You")
            
            
            