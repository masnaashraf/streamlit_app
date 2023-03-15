import streamlit as st
import pandas as pd
from matplotlib import image
import os
import io

st.title(":red[Exploratory Data Analysis]")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "heart2.jpg")


img = image.imread(IMAGE_PATH)

st.image(img)



DATA_PATH = os.path.join(dir_of_interest, "data", "heart_cleaned.csv")
df = pd.read_csv(DATA_PATH)




data_info = st.radio(':blue[Explore the data set using available options:]',
                      ('Head', 'Tail','Sample', 'Columns', 'Shape', 'Info', 'Descriptive Statistics',"Unique column values"),
                      horizontal=True)

if data_info == 'Shape':
    st.subheader("Shape")
    st.write(f"Number of Rows:  {df.shape[0]}")
    st.write(f"Number of Columns:  {df.shape[1]}")
elif data_info == 'Head':
    st.subheader("Top 5 rows")
    st.write(df.head())
elif data_info == 'Tail':
    st.subheader("Bottom 5 rows")
    st.write(df.tail())
elif data_info == 'Sample':
    st.subheader("10 Sample rows")
    st.write(df.sample(10))  
elif data_info == 'Columns':
    st.subheader("List of column names")
    for column in list(df.columns):
        st.write(column)
elif data_info == 'Info':
    st.subheader("Information regarding the data set")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
elif data_info=="Unique column values":
    st.subheader("Number of unique values in each column")
    st.write(df.nunique())

    st.subheader("Unique values of each column")
    for i in df.columns[:]:
        st.subheader("Unique values:")
        st.write(i)
        
        st.write(df[i].unique())

else:
    st.subheader("Statistical Information regarding the data set")
    st.write(df.describe())