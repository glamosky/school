# streamlit_app.py
import streamlit as st
import pandas as pd
from job_scraper import search_all_roles

st.set_page_config(page_title="Entry-Level Job Scraper", layout="wide")
st.title("🧑‍💻 Entry-Level Job Scraper")
st.write("Search for entry-level jobs across multiple platforms.")

# Sidebar for API key and sources
st.sidebar.header("API Keys and Settings")
jooble_api_key = st.sidebar.text_input("Jooble API Key", "fdee36f0-c7ca-4c9a-a4a6-395c4bcaa4b6", help="Required for Jooble searching")
include_jobstreet = st.sidebar.checkbox("Include JobStreet results (may be less reliable)", value=False)

# User input in main area
st.subheader("Search Criteria")
roles = st.text_area("Job titles (comma-separated)", "data analyst, business analyst, entry level python, junior data scientist", 
                      help="Enter multiple job titles separated by commas. Each will be searched separately.")
location = st.text_input("Location", "Philippines")
max_results = st.slider("Max results per role per platform", 10, 50, 30, step=10)

# Skills input
st.subheader("Required Skills")
st.write("Select skills to filter job descriptions. A job will match if it contains ANY of these skills:")
col1, col2, col3 = st.columns(3)
with col1:
    sql = st.checkbox("SQL", value=True)
    python = st.checkbox("Python", value=False)
with col2:
    excel = st.checkbox("Excel", value=True)
    tableau = st.checkbox("Tableau", value=False)
with col3:
    linux = st.checkbox("Linux", value=False)
    other_skill = st.text_input("Other skill (optional)")

if st.button("Search Jobs"):
    if not jooble_api_key:
        st.error("Jooble API key is required. Please enter it in the sidebar.")
    else:
        with st.spinner("Scraping job listings... This may take a minute."):
            # Build skills list based on selections
            skills = []
            if sql: skills.append("SQL")
            if python: skills.append("Python")
            if excel: skills.append("Excel")
            if tableau: skills.append("Tableau")
            if linux: skills.append("Linux")
            if other_skill: skills.append(other_skill)
            
            # Display search criteria
            st.info(f"Searching for: {roles}\nLocation: {location}\nSkills filter: {', '.join(skills) if skills else 'None (showing all entry-level jobs)'}")
            
            # Parse comma-separated roles
            keywords = [r.strip() for r in roles.split(",") if r.strip()]
            
            # Display roles being searched
            if len(keywords) > 1:
                st.write(f"Searching for {len(keywords)} roles: {', '.join(keywords)}")
            
            # Search for jobs using both JobStreet and Jooble
            jobs = search_all_roles(
                keywords, 
                location=location, 
                max_results=max_results, 
                required_skills=skills,
                jooble_api_key=jooble_api_key,
                include_jobstreet=include_jobstreet
            )
            
            if jobs:
                df = pd.DataFrame(jobs)
                st.success(f"Found {len(jobs)} entry-level jobs!")
                
                # Add filtering options
                st.subheader("Filter Results")
                col1, col2 = st.columns(2)
                with col1:
                    platform_filter = st.multiselect("Platform", options=df["platform"].unique(), default=df["platform"].unique())
                
                with col2:
                    if "keyword" in df.columns:
                        keyword_filter = st.multiselect("Job Category", options=df["keyword"].unique(), default=df["keyword"].unique())
                    else:
                        keyword_filter = None
                
                # Apply filters
                filtered_df = df
                if platform_filter:
                    filtered_df = filtered_df[filtered_df["platform"].isin(platform_filter)]
                
                if keyword_filter:
                    filtered_df = filtered_df[filtered_df["keyword"].isin(keyword_filter)]
                
                st.write(f"Showing {len(filtered_df)} jobs after filtering")
                
                # Display as dataframe
                st.subheader("All Matched Jobs")
                display_cols = ["platform", "title", "company", "link"]
                if "matched_skills" in df.columns:
                    # Convert list of skills to comma-separated string
                    filtered_df["matched_skills_str"] = filtered_df["matched_skills"].apply(lambda x: ", ".join(x) if isinstance(x, list) else "")
                    display_cols.append("matched_skills_str")
                
                # Add salary column if available
                if "salary" in df.columns:
                    display_cols.append("salary")
                
                st.dataframe(filtered_df[display_cols])
                
                # Display as cards
                st.subheader("Job Details")
                for _, job in filtered_df.iterrows():
                    with st.expander(f"[{job['platform']}] {job['title']} - {job.get('company', '')}"):
                        if "matched_skills" in job and isinstance(job["matched_skills"], list) and job["matched_skills"]:
                            st.write(f"**Skills matched:** {', '.join(job['matched_skills'])}")
                        elif "matched_skills" in job and isinstance(job["matched_skills"], str) and job["matched_skills"]:
                            st.write(f"**Skills matched:** {job['matched_skills']}")
                        
                        if "location" in job:
                            st.write(f"**Location:** {job['location']}")
                        
                        if "salary" in job and job["salary"]:
                            st.write(f"**Salary:** {job['salary']}")
                        
                        st.write("**Description:**")
                        st.write(job["summary"])
                        st.markdown(f"[Apply Here]({job['link']})")
            else:
                st.warning("No entry-level jobs found with the given criteria and skills.")
                st.info("Try with fewer or no skill requirements, or use different job titles.")

# Add explanatory documentation at the bottom
st.markdown("---")
st.subheader("💡 How This Works")
st.markdown("""
- **Multi-source search**: Searches job listings from both Jooble API and (optionally) JobStreet
- **Entry-level filter**: Only shows jobs suitable for entry-level candidates based on job descriptions
- **Skills matching**: Shows jobs that mention ANY of your selected skills
- **Flexible input**: Enter multiple job titles separated by commas to search for various roles at once
""")
