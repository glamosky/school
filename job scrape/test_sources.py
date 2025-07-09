import job_scraper
import json

def test_and_compare_sources():
    """Test both JobStreet and Jooble and compare results"""
    search_term = "data analyst"
    location = "Philippines"
    skills = ["SQL", "Excel"]
    jooble_api_key = "fdee36f0-c7ca-4c9a-a4a6-395c4bcaa4b6"
    
    print(f"Testing job sources for: {search_term} in {location} with skills: {skills}\n")
    
    # Get results from JobStreet
    print("\n===== TESTING JOBSTREET =====")
    jobstreet_results = job_scraper.scrape_jobstreet(search_term, location, max_results=5, required_skills=skills)
    
    # Get results from Jooble
    print("\n===== TESTING JOOBLE API =====")
    jooble_results = job_scraper.scrape_jooble(search_term, location, max_results=5, required_skills=skills, api_key=jooble_api_key)
    
    # Print JobStreet results
    print("\n\n===== JOBSTREET RESULTS =====")
    print(f"Found {len(jobstreet_results)} results")
    for i, job in enumerate(jobstreet_results, 1):
        print(f"\nJob #{i}:")
        print(f"Title: {job.get('title', 'N/A')}")
        print(f"Company: {job.get('company', 'N/A')}")
        print(f"Skills Matched: {', '.join(job.get('matched_skills', []))}")
        # Print a snippet of the job description
        snippet = job.get('summary', 'N/A')
        print(f"Description snippet: {snippet[:150]}..." if len(snippet) > 150 else f"Description: {snippet}")
    
    # Print Jooble results
    print("\n\n===== JOOBLE RESULTS =====")
    print(f"Found {len(jooble_results)} results")
    for i, job in enumerate(jooble_results, 1):
        print(f"\nJob #{i}:")
        print(f"Title: {job.get('title', 'N/A')}")
        print(f"Company: {job.get('company', 'N/A')}")
        print(f"Skills Matched: {', '.join(job.get('matched_skills', []))}")
        # Print a snippet of the job description
        snippet = job.get('summary', 'N/A')
        print(f"Description snippet: {snippet[:150]}..." if len(snippet) > 150 else f"Description: {snippet}")

if __name__ == "__main__":
    test_and_compare_sources() 