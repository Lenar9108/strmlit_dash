import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dash App",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
)

df = pd.read_csv('rents_test.csv', sep=',', encoding='utf-8')
country_list = df['country_name'].unique()

st.header('CarSharing X 🚕')


st.write()
st.write()

with st.sidebar:

    options = st.multiselect(
        'Выберите страну',
        country_list,
        country_list[:2])


    
st.subheader('Ежедневная выручка по регионам')

df_revenue = df[['rent_date', 'country_name','rent_cost_per_day']].groupby(['rent_date', 'country_name']).sum().reset_index().copy()
df_revenue = df_revenue.rename(columns={'rent_date':'Дата', 'country_name':'Страна','rent_cost_per_day':'Дневная выручка'})
st.line_chart(df_revenue[df_revenue['Страна'].isin(options)], x="Дата", y="Дневная выручка", color="Страна")


df_users = df[['rent_date', 'rent_id', 'country_name']].groupby(['rent_date', 'country_name']).count().reset_index().copy()
df_users = df_users.rename(columns={'rent_date':'Дата', 'country_name':'Страна', 'rent_id': 'Кол-во пользователей'})

st.subheader('Кол-во активных пользователей')
st.bar_chart(df_users[df_users['Страна'].isin(options)], x='Дата', y='Кол-во пользователей' )


