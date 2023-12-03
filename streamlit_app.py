import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dash App",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

df = pd.read_csv('vacancy1.csv', sep=',', encoding='utf-8')
recruiter_list = df['Рекрутер'].unique()
vacancy_state_list = df['vacancy_state'].unique()

st.header('HR Dash 👋')


options = st.multiselect(
        'Выберите рекрутера',
        recruiter_list,
        recruiter_list[:3])
        
        


fig = px.bar(df[df['Рекрутер'].isin(options)].drop_duplicates(subset='candidate_id').vacancy_state.value_counts(),title='Кол-во по статусам', labels={'value':'Кол-во', 'vacancy_state':'Статус' })
fig_2 = px.bar(df[df['Рекрутер'].isin(options)].drop_duplicates(subset='candidate_id').entrance_type.value_counts(),title='Канал привлечения', labels={'value':'Кол-во', 'entrance_type':'Канал привлечения' })
fig_3 = px.pie(df[df['Рекрутер'].isin(options)].drop_duplicates(subset='candidate_id').csource.value_counts().reset_index(), values='count', names='csource', hole=.6 ,title='Канал привлечения')

fig.update_layout(width = 500,showlegend=False)
fig_2.update_layout(width = 500,showlegend=False)
fig_3.update_layout(width = 500,showlegend=True)


col1, col2 = st.columns(2)
with col1:
    st.write(fig)
    st.write(fig_2)

with col2:
    st.write(fig_3)
    
    st.markdown('**Текущий статус вакансии**')
    options_2 = st.selectbox(
        'Выберите статус вакансии',
        vacancy_state_list,index=2)
        
    df_3 = df[(df['Рекрутер'].isin(options))&(df['vacancy_state']==options_2)].drop_duplicates(subset='vacancy_id')[['vacancy_name','vacancy_state_date']].reset_index(drop=True)
    df_3 = df_3.rename(columns={'vacancy_name':'Вакансия', 'vacancy_state_date':'Дата статуса'})
    
    st.table(df_3)


