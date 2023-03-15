
import streamlit as st




st.title(":red[Heart Disease Diagnostic Data Description]")




st.markdown(
    """
    
    ## Heart Disease Diagnostic
    This dataset contains details of the age,BP,cholestrol and about having heart disease or not.Using the attributes in the dataset we can predict heart diseae risk for an individual and identify the risk factors.
    ### Problem Statement:
    Health is real wealth in the pandemic time we all realized the brute effects of covid-19 on all irrespective of any status. You are required to analyze this health and medical data for better future preparation.
    
    
    - From the database extract various information such as Heart disease rates, Heart disease by gender, by age.
    - You can even compare attributes of the data set to extract necessary information.
    - Make necessary dashboard with the best you can extract from the data.
    - Use various visualization and features and make the best dashboard.
    - Find key metrics and factors and show the meaningful relationships between attributes.
    
    
    
    
    ## Dataset Information:
    This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. In particular,   the Cleveland database is the only one that has been used by ML researchers to this date. The "goal" field refers to the presence of heart disease in the patient. It is integer valued from 0 (no presence) to 4. Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0).
    
    The names and social security numbers of the patients were recently removed from the database, replaced with dummy values.
    
    One file has been "processed", that one containing the Cleveland database. All four unprocessed files also exist in this directory.
    
    To see Test Costs (donated by Peter Turney), please see the folder "Costs"
    
    ### Attribute Information:
    
    - Age: The person's age in years
    - Sex: The person's sex (1 = male, 0 = female)
    Variant
    - Chest Pain Level: The chest pain experienced (Value 1: Stable Value 2: Unstable Value 3: Microvascular Value 4: Variant)
    - Resting Blood Pressure: The person's resting blood pressure (mm Hg on admission to the hospital)
    - Cholestrol: The person's cholesterol measurement in mg/dl
    - Fasting Blood Sugar : The person's fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)
    - Resting ECG: Resting electrocardiographic measurement (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria)
    - Max Heart Rate: The person's maximum heart rate achieved
    - Excercise Induced Angina: Exercise induced angina (1 = yes; 0 = no)
    - Depression: ST depression induced by exercise relative to rest
    - slopeC: the slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping)
    - Major Vessels: The number of major vessels (0-3)
    - Thalassemia Level: A blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)
    - Heart Disease: Heart disease (0 = no, 1 = yes)
    
"""
)