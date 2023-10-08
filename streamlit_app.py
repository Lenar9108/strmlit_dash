import streamlit as st
import pandas as pd



df = pd.read_csv('rents_test.csv', sep=',', encoding='utf-8')

st.header('CarSharing X 🚕')

st.write()
st.write()
st.write('Ежедневная выручка по регионам')
df_revenue = df[['rent_date', 'country_name','rent_cost_per_day']].groupby(['rent_date', 'country_name']).sum().reset_index().copy()
df_revenue = df_revenue.rename(columns={'rent_date':'Дата', 'country_name':'Страна','rent_cost_per_day':'Дневная выручка'})

options = st.multiselect(
    'Выберите страну',
    df_revenue['Страна'].unique(),
    df_revenue['Страна'].unique()[:5])

# st.write('Вы укзали:', options)
df_revenue = df_revenue[df_revenue['Страна'].isin(options)]

st.line_chart(df_revenue, x="Дата", y="Дневная выручка", color="Страна")
