import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

cars= pd.read_csv('./vehicles_us.csv')

exclude_classic= st.checkbox("Exclude classic vehicles", value=False)
if exclude_classic:
    cars=cars[cars['model_year']>2000]

exclude_new= st.checkbox("Exclude new vehicles", value=False)
if exclude_new:
    cars=cars[cars['model_year']<=2018]

exclude_fair= st.checkbox('Exclude fair vehicles', value=False)
if exclude_fair:
    cars=cars[cars['condition']!='fair']


days_listed= cars.value_counts(subset=["condition", "days_listed"]).to_frame().reset_index()

st.header('How many days a vehicle has been listed for')
st.plotly_chart(px.line(cars.days_listed.value_counts().sort_index(), labels=dict(
  days_listed="Days Listed",
  value="Count")))

condition=cars.condition

st.header('Length on market vs quality of car')
st.plotly_chart(px.scatter(condition, labels=dict(
  count="Number of vehicles",
  value="Quality",
  index="Number of days"
  )))

st.header('Length of time of market')
st.plotly_chart(px.histogram(cars.days_listed, labels=dict(
    y ='Days',
    value='Number of vehicles'
)))



