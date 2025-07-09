import job_scraper

def main():
    # Test settings
    search_terms = ["data analyst"]
    location = "Philippines"
    skills = ["SQL", "Excel"]
    jooble_api_key = "fdee36f0-c7ca-4c9a-a4a6-395c4bcaa4b6"
    
    print(f"Searching for jobs matching: {search_terms} in {location}")
    print(f"Required skills: {skills}")
    
    # Run the search
    results = job_scraper.search_all_roles(
        search_terms,
        location=location,
        max_results=10,
        required_skills=skills,
        jooble_api_key=jooble_api_key,
        include_jobstreet=False
    )
    
    # Display results
    print(f"\nFound {len(results)} matching jobs:")
    
    for i, job in enumerate(results, 1):
        print(f"\n--- Job #{i} ---")
        print(f"Title: {job.get('title', 'N/A')}")
        print(f"Company: {job.get('company', 'N/A')}")
        print(f"Platform: {job.get('platform', 'N/A')}")
        print(f"Skills matched: {', '.join(job.get('matched_skills', []))}")
        print(f"Link: {job.get('link', 'N/A')}")
        
        # Show a snippet of the summary
        summary = job.get('summary', '')
        if len(summary) > 150:
            summary = summary[:150] + "..."
        print(f"Summary: {summary}")

if __name__ == "__main__":
    main() 