import streamlit as st
import pandas as pd
from sklearn.naive_bayes import GaussianNB
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


DATA_PATH = os.path.join(dir_of_interest, "data", "heart_numerical.csv")

st.title(":red[Heart Disease Predictor]")

df= pd.read_csv(DATA_PATH)

# creating function to convert numerical to categorical data

df.rename(columns={'Chest Pain Level':'Chest_Pain_Level', 'Resting Blood Pressure':'Resting_Blood_Pressure','Fasting Blood Sugar':"Fasting_Blood_Sugar"
                   , 'Resting ECG':"Resting_ECG", 'Max Heart Rate':"Max_Heart_Rate",
       'Excercise Induced Angina':"Excercise_Induced_Angina", 'Major Vessels':"Major_Vessels",
       'Thalassemia Level':"Thalassemia_Level"},inplace=True)


st.write(":blue[Provide values and predict your chance of heart disease]")

st.header("User input:")

def user_input():
    Age= st.number_input('Enter your Age',min_value=0)

    Sex = st.radio("Select your sex",('Male','Female'))
    #1=Male , 0=Female
    if Sex == "Male":
        sex_val=1
        
    elif Sex == "Female":
        sex_val=0
    
    Chest_Pain_Level=st.radio("Select  Chest Pain Level ",('Stable Value','Unstable Value' ,'Microvascular Value','Variant'))
    #1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic
    if Chest_Pain_Level=="Stable Value":
        cpl_val=1
    elif Sex=="Unstable Value":
        cpl_val=2
    elif Sex=="Microvascular Value":
        cpl_val=3
    elif Sex=="Variant":
        cpl_val=4

    Resting_Blood_Pressure= st.number_input('Enter Resting Blood Pressure value',min_value=0)

    Cholestrol=st.number_input('Enter Cholestrol Level',min_value=0)

    Fasting_Blood_Sugar = st.radio("select person's fasting blood sugar ",('Greater than 120 mg/dl', ' Less than 120 mg/dl'))
    # 1 = true; 0 = false
    if Fasting_Blood_Sugar=="Greater than 120 mg/dl":
        bs_val=1
    elif Fasting_Blood_Sugar=="Less than 120 mg/dl":
        bs_val=0

    Resting_ECG=st.radio("Select Resting electrocardiographic measurement", ('Normal', 'Having ST-T wave abnormality','Showing probable or definite left ventricular hypertrophy by Estes\' criteria'))
    #0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria

    if Resting_ECG=="Normal":
        ecg_val=0
    elif Resting_ECG=="Having ST-T wave abnormality":
        ecg_val=1
    elif Resting_ECG=="Showing probable or definite left ventricular hypertrophy by Estes\' criteria":
        ecg_val=2
    

    Max_Heart_Rate=Cholestrol=st.number_input('Enter ax_Heart_Rate value',min_value=0)

    Excercise_Induced_Angina= st.radio('Exercise induced angina',('Yes','No'))
    #Exercise induced angina (1 = yes; 0 = no)

    if Excercise_Induced_Angina=="Yes":
        angina_val=1
    elif Excercise_Induced_Angina=="No":
        angina_val=0

    Depression=st.number_input('Enter drepression value in range(\o.o to 10.0\)',min_value=0.0,max_value=10.0)

    SlopeC= st.radio('Select the slope of the peak exercise ST segment',('Upsloping','Flat','Downsloping'))
    #Value 1: upsloping, Value 2: flat, Value 3: downsloping

    if SlopeC=="Upsloping":
        slope_val=1
    elif SlopeC=="Flat":
        slope_val=2
    elif SlopeC=="Downsloping":
        slope_val=3

   
    Major_Vessels=st.radio("Select the number of major vessels \(0-3\)",('0','1','2','3'))
    vessel_val=int( Major_Vessels)
    
    Thalassemia_Level=st.radio("Select the level of thalassemia disoder",('Normal','Fixed defect','Reversable defect'))
    # (3 = normal; 6 = fixed defect; 7 = reversable defect)
    if Thalassemia_Level=="Normal":
        t_val=3
    elif Thalassemia_Level=="Reversable defect":
        t_val=7
    elif Thalassemia_Level=="Fixed defect":
        t_val=6
    



    data={"Age": Age,
          "Sex":sex_val,
          "Chest_Pain_Level":cpl_val,
          "Resting_Blood_Pressure":Resting_Blood_Pressure,
          "Cholestrol":Cholestrol,
          "Fasting_Blood_Sugar":bs_val,
          "Resting_ECG":ecg_val,
          "Max_Heart_Rate":Max_Heart_Rate,
          "Excercise_Induced_Angina":angina_val,
          "Depression":Depression,
          "SlopeC":slope_val,
          "Major_Vessels":vessel_val,
          "Thalassemia_Level":t_val
          }
    features=pd.DataFrame(data,index=[0])
    return features
df_userinput=user_input()




X=df.iloc[:,:-1]
Y=df.iloc[:,-1]
classifierNB = GaussianNB()
classifierNB.fit(X, Y)
y_res=classifierNB.predict(df_userinput)
r=y_res[0]
if r==1:
    st.subheader("HEART DISEASE DETECTED")
elif r==0:
    st.subheader("HEART DISEASE NOT DETECTED")

