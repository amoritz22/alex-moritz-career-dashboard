
Interactive Career Dashboard — Quick Deploy

FILES
- streamlit_career_dashboard.py
- resume_experience.csv
- resume_projects.csv
- resume_skills.csv
- resume_certifications.csv
- resume_education.csv
- resume_project_skill_relations.csv
- requirements.txt

RUN LOCALLY
1) Create/activate a virtual environment
2) pip install -r requirements.txt
3) streamlit run streamlit_career_dashboard.py

HOSTING OPTIONS
- Streamlit Community Cloud (free): upload these files to a GitHub repo and deploy.
- Your server: `streamlit run` behind nginx or use `gunicorn` + reverse proxy.
- Databricks: import CSVs to DBFS and adapt code to read from `/dbfs/...`.

ADD TO RÉSUMÉ
- Include a link (and QR code) to the live app in your résumé header.
- Keep the PDF résumé as the primary attachment for HR.
