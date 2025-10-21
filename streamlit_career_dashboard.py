
import streamlit as st
import pandas as pd
from datetime import datetime, date
import plotly.express as px

st.set_page_config(page_title="Alexander R. Moritz — Career Dashboard", layout="wide")

st.title("Alexander R. Moritz — Data Engineer")
st.caption("TS/SCI | AWS • Databricks • Spark • Python • RMF/NIST")

# Load data
@st.cache_data
def load_data():
    exp = pd.read_csv("resume_experience.csv")
    proj = pd.read_csv("resume_projects.csv")
    skills = pd.read_csv("resume_skills.csv")
    certs = pd.read_csv("resume_certifications.csv")
    edu = pd.read_csv("resume_education.csv")
    rel = pd.read_csv("resume_project_skill_relations.csv")
    return exp, proj, skills, certs, edu, rel

exp, proj, skills, certs, edu, rel = load_data()

# KPIs
col1, col2, col3, col4 = st.columns(4)
with col1:
    min_start = pd.to_datetime(exp['start_date']).min()
    years_exp = round((pd.Timestamp.today() - min_start).days / 365.25, 1)
    st.metric("Years of Experience", f"{years_exp}+")

with col2:
    st.metric("Active Certifications", f"{(certs['status']=='Active').sum()}")

with col3:
    st.metric("Projects", f"{len(proj)}")

with col4:
    cloud_skills = skills[skills['category'].isin(['AWS','Platform','Data Warehouse'])]['skill'].nunique()
    st.metric("Cloud/Platform Skills", f"{cloud_skills}")

st.markdown("---")

# Skills matrix
st.subheader("Skills Matrix")
cat = st.multiselect("Filter by category", sorted(skills['category'].unique()))
skills_view = skills.copy()
if cat:
    skills_view = skills_view[skills_view['category'].isin(cat)]
fig1 = px.bar(skills_view.sort_values(by='level_1to5', ascending=True),
              x='level_1to5', y='skill', orientation='h',
              hover_data=['category','frequency_per_month'])
st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# Project impact
st.subheader("Project Impact")
proj_col, skills_col = st.columns((2,1))
with proj_col:
    st.dataframe(proj[['project_name','tools_stack','metrics','description']])
with skills_col:
    skill_counts = rel['skill'].value_counts().rename_axis('skill').reset_index(name='count')
    fig2 = px.bar(skill_counts, x='skill', y='count', title='Skills used across projects')
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Experience timeline (simple)
st.subheader("Experience Timeline")
exp_view = exp.copy()
exp_view['start_date'] = pd.to_datetime(exp_view['start_date'])
exp_view['end_date'] = pd.to_datetime(exp_view['end_date'], errors='coerce')
exp_view['end_date'] = exp_view['end_date'].fillna(pd.Timestamp.today())
exp_view['duration_days'] = (exp_view['end_date'] - exp_view['start_date']).dt.days
fig3 = px.timeline(exp_view, x_start='start_date', x_end='end_date', y='role', color='organization',
                   hover_data=['summary','key_technologies','outcomes'])
fig3.update_yaxes(autorange="reversed")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.subheader("Certifications & Education")
c1, c2 = st.columns(2)
with c1:
    st.dataframe(certs)
with c2:
    st.dataframe(edu)

st.info("Tip: Add this app link to your résumé header or as a QR code. Host with `streamlit run app.py` on a server or share via Streamlit Community Cloud.")
