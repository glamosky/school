import streamlit as st
import job_scraper
import pandas as pd

st.title("Job Scraper Test")

# Configuration sidebar
st.sidebar.header("Search Settings")
search_term = st.sidebar.text_input("Job Title/Keyword", "data analyst")
location = st.sidebar.text_input("Location", "Philippines")
max_results = st.sidebar.slider("Max Results per Source", min_value=5, max_value=30, value=10)

# Skills selection
skills_options = ["SQL", "Excel", "Python", "Tableau", "Linux"]
selected_skills = st.sidebar.multiselect("Required Skills", skills_options, default=["SQL", "Excel"])

# API key input
jooble_api_key = st.sidebar.text_input("Jooble API Key", "fdee36f0-c7ca-4c9a-a4a6-395c4bcaa4b6")

# Toggle for including JobStreet
include_jobstreet = st.sidebar.checkbox("Include JobStreet results", value=False)

# Search button
if st.sidebar.button("Search Jobs"):
    if not search_term:
        st.error("Please enter a job title or keyword")
    elif not jooble_api_key:
        st.error("Please enter your Jooble API key")
    else:
        # Show progress spinner
        with st.spinner(f"Searching for {search_term} jobs in {location}..."):
            try:
                # Convert the search term to a list with a single item
                search_terms = [search_term]
                
                # Print debug info to verify parameters
                st.write("Debug Info:", {
                    "keywords": search_terms,
                    "location": location,
                    "max_results": max_results,
                    "required_skills": selected_skills,
                    "jooble_api_key": jooble_api_key[:5] + "..." if jooble_api_key else None,
                    "include_jobstreet": include_jobstreet
                })
                
                # Run the search
                results = job_scraper.search_all_roles(
                    search_terms,
                    location=location,
                    max_results=max_results,
                    required_skills=selected_skills,
                    jooble_api_key=jooble_api_key,
                    include_jobstreet=include_jobstreet
                )
                
                # Display results count
                st.success(f"Found {len(results)} matching jobs!")
                
                if not results:
                    st.warning("No jobs found matching your criteria. Try adjusting your search terms or skills requirements.")
                else:
                    # Convert to DataFrame for easier display
                    df = pd.DataFrame(results)
                    
                    # Add a formatted skills column
                    if 'matched_skills' in df.columns:
                        df['Skills'] = df['matched_skills'].apply(lambda x: ', '.join(x) if x else "None")
                    
                    # Display results in expandable sections
                    for i, job in enumerate(results):
                        with st.expander(f"{i+1}. {job.get('title', 'Untitled')} - {job.get('company', 'Unknown')}"):
                            st.write(f"**Platform:** {job.get('platform', 'N/A')}")
                            st.write(f"**Skills matched:** {', '.join(job.get('matched_skills', []))}")
                            st.write(f"**Location:** {job.get('location', 'N/A')}")
                            st.write(f"**Link:** {job.get('link', 'N/A')}")
                            st.write("**Description:**")
                            st.write(job.get('summary', 'No description available'))
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                import traceback
                st.code(traceback.format_exc())
else:
    st.info("Use the sidebar to set your search criteria and click 'Search Jobs'")

# Display help info
st.sidebar.markdown("---")
st.sidebar.markdown("### Help")
st.sidebar.markdown("""
- Enter a job title or keyword to search for
- Select required skills to filter results
- Enter your Jooble API key (get one from https://jooble.org/api/about)
- Click Search Jobs to find matching jobs
""") 