import streamlit as st
import pandas as pd
import os
from matplotlib import image
import plotly.express as px


st.title(":red[Heart Disease Diagnostic Visualization]")


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "heart2.jpg")



DATA_PATH = os.path.join(dir_of_interest, "data", "heart_cleaned.csv")
df = pd.read_csv(DATA_PATH)

data_info = st.radio(':blue[Click to view the Visualization of the Dataset]:',
                      ('Age Group', 'Sex', 'Chest Pain Level','Excercise Induced Angina', 'SlopeC', 'Thalassemia Level'),
                      horizontal=True)


if data_info == 'Age Group':
    st.markdown(" ## Ages Group")

    col1, col2 = st.columns(2)
    fig_1 = px.pie(df, names='Age Group', hole=0.5, title='Age Pie Chart')
    col1.plotly_chart(fig_1)
    
    
    fig_1 = px.histogram(df, x='Age Group',color="Heart Disease" , title='Age Group vs Heart Disease Histogram Chart')
    col1.plotly_chart(fig_1)

elif data_info == 'Sex':
    st.markdown(" ## Gender")

    col1, col2 = st.columns(2)
    fig_1 = px.pie(df, names='Sex', hole=0.5, title='Gender Pie Chart')
    col1.plotly_chart(fig_1)
    
    
    fig_1 = px.histogram(df, x='Sex',color="Heart Disease" , title='Gender vs Heart Disease Histogram Chart')
    col1.plotly_chart(fig_1)


elif data_info == 'Chest Pain Level':
    st.markdown("## Chest Pain Experienced")

    col1, col2 = st.columns(2)

    fig_1 = px.histogram(df, x='Chest Pain Level', title='Chest Pain Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='Chest Pain Level', color='Sex', title='Chest Pain vs Gender Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='Chest Pain Level', color='Age Group', title='Chest Pain vs Age Group Histogram Chart')
    col1.plotly_chart(fig_1)

    fig_1 = px.histogram(df, x='Chest Pain Level',color="Heart Disease" , title='Gender vs Heart Disease Histogram Chart')
    col1.plotly_chart(fig_1)


elif data_info == 'Excercise Induced Angina':
    st.markdown("## Exercise Induced Angina")
    
    col1, col2 = st.columns(2)
    
    fig_1 = px.pie(df, names='Excercise Induced Angina', hole=0.5, title='Exercise Induced Angina Pie Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='Excercise Induced Angina', color='Sex', title='Exercise Induced Angina vs Gender Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='Excercise Induced Angina', color='Age Group', title='Exercise Induced Angina vs Age Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='Excercise Induced Angina',color="Heart Disease" , title='Excercise Induced Angina vs Heart Disease Histogram Chart')
    col1.plotly_chart(fig_1)
   

elif data_info == 'SlopeC':
    st.markdown("## The Slope of the Peak Exercise ST Segment")
    
    col1, col2 = st.columns(2)
    
    fig_1 = px.pie(df, names='SlopeC', hole=0.5,  title='Slope Pie Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='SlopeC', color='Sex', title='Slope vs Gender Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='SlopeC', color='Age Group', title='Slope vs Age Histogram Chart')
    col1.plotly_chart(fig_1)



   
elif data_info == 'Thalassemia Level':
    st.markdown("## A Blood Disorder called Thalassemia")
    
    col1, col2 = st.columns(2)
    
    fig_1 = px.pie(df, names='Thalassemia Level', hole=0.5,  title='Thalassemia Pie Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='Thalassemia Level', color='Sex',  title='Thalassemia vs Gender Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='Thalassemia Level', color='Age Group',  title='Thalassemia vs Ages Histogram Chart')
    col1.plotly_chart(fig_1)

    fig_1 = px.histogram(df, x='Thalassemia Level',color="Heart Disease" , title='Thalassemia Level vs Heart Disease Histogram Chart')
    col1.plotly_chart(fig_1)



