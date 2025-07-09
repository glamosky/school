# job_scraper.py
import requests
from bs4 import BeautifulSoup
import re
import time
import random
import json

def filter_entry_level(text, required_skills=None):
    # Check for explicit mentions of years of experience
    experience_match = re.search(
        r"\b(\d+)[\+]?\s*(?:to|-)\s*(\d+)[\+]?\s*(?:years?|yrs?)\b|\b(\d+)[\+]?\s*(?:years?|yrs?)\b", 
        text, 
        re.IGNORECASE
    )
    
    # First check for exclusion criteria - more than 1 year experience
    if experience_match:
        # Case 1: Range like "3-5 years"
        if experience_match.group(1) and experience_match.group(2):
            min_years = int(experience_match.group(1))
            if min_years > 1:  # If minimum is more than 1 year, exclude
                return False
        # Case 2: Single value like "3 years" or "3+ years"
        elif experience_match.group(3):
            years = int(experience_match.group(3))
            if years > 1:  # If more than 1 year experience required, exclude
                return False
    
    # Look for positive indicators of entry-level positions
    positive_patterns = [
        r"\bentry[\s-]?level\b",
        r"\bjunior\b", 
        r"\bjr\.?\b",
        r"\btrainee\b",
        r"\bbeginner\b",
        r"\bapprentice\b",
        r"\bno experience(?:\s+required)?\b",
        r"\bminimal experience\b",
        r"\bfresh(?:[\s-]?gr[ao]ds?|[\s-]?graduates?)\b",
        r"\brecent(?:[\s-]?gr[ao]ds?|[\s-]?graduates?)\b",
        r"\binternship\b",
        r"\b0-1 year\b",
        r"\bless than (a|\d+) year\b",
        r"\b(0|1) year\b",
        r"\bstart(?:ing|er) position\b",
        r"\blittle to no experience\b",
        r"\bwilling to train\b"
    ]
    
    # Look for negative indicators of senior or mid-level positions
    negative_patterns = [
        r"\bsenior\b",
        r"\bmanager\b",
        r"\blead\b", 
        r"\bdirector\b",
        r"\bexpert\b",
        r"\bhead of\b",
        r"\barchitect\b",
        r"\bprincipal\b",
        r"\bvice president\b",
        r"\bcxo\b",
        r"\bexecutive\b"
    ]
    
    # Check if the job has any negative indicators
    if any(re.search(pattern, text, re.IGNORECASE) for pattern in negative_patterns):
        return False
    
    # Check if the job matches entry-level criteria
    is_entry_level = any(re.search(pattern, text, re.IGNORECASE) for pattern in positive_patterns)
    
    # Check for specific experience mentions
    # But exclude words like "expertise" or "skilled" which don't necessarily indicate years of experience
    has_experience_mention = False
    if re.search(r"\bexperience(?:d)?\b", text, re.IGNORECASE):
        # Check if it's asking for experience specifically, not just mentioning the word
        exp_context = re.search(r"\b(?:with|require|need|must have|looking for)(?:\s+\w+){0,5}\s+experience", text, re.IGNORECASE)
        if exp_context:
            has_experience_mention = True
    
    has_years_mention = re.search(r"\b(?:years|yrs)\b(?!\s+old)", text, re.IGNORECASE) is not None
    
    # If explicitly states it's entry-level, mark it as such
    if is_entry_level:
        # If we're filtering by skills and have entry-level indicator, check skills
        if required_skills:
            matched_skills = []
            for skill in required_skills:
                skill_patterns = [r'\b{}\b'.format(re.escape(skill))]
                
                # Add variations for common skills - make more permissive
                if skill.lower() == "sql":
                    skill_patterns.extend([
                        r'\b(?:SQL|MySQL|PostgreSQL|MSSQL|SQLite|T-SQL|database|query|queries)\b',
                        r'\bdata\s?base\b',
                        r'\bdata\s?driven\b',
                    ])
                elif skill.lower() == "python":
                    skill_patterns.extend([
                        r'\b(?:Python|Django|Flask|pandas|NumPy|PyTorch|TensorFlow)\b',
                        r'\bscript(?:ing)?\b',
                        r'\bprogram(?:ming)?\b',
                    ])
                elif skill.lower() == "excel":
                    skill_patterns.extend([
                        r'\b(?:Excel|Microsoft Excel|Spreadsheet|Office|XLS)\b',
                        r'\bMS Office\b',
                        r'\bspreadsheet\b',
                    ])
                elif skill.lower() == "tableau":
                    skill_patterns.extend([
                        r'\b(?:Tableau|Data Visualization|PowerBI|dashboard|reporting)\b',
                        r'\bvisualization\b',
                        r'\breport(?:ing)?\b',
                    ])
                elif skill.lower() == "linux":
                    skill_patterns.extend([
                        r'\b(?:Linux|Unix|Bash|Shell|Ubuntu|CentOS)\b',
                        r'\bcommand\s?line\b',
                        r'\bterminal\b',
                    ])
                
                # Check all patterns for this skill
                if any(re.search(pattern, text, re.IGNORECASE) for pattern in skill_patterns):
                    matched_skills.append(skill)
            
            # Match ANY of the required skills (more flexible)
            return len(matched_skills) > 0
            
        # No skills to filter, but job is entry-level
        return True
    
    # If experience or years are mentioned but no clear entry-level indicator and no specific years
    # it's likely NOT an entry-level role
    if (has_experience_mention or has_years_mention) and not experience_match:
        # Check for "no experience" or "minimal experience" phrases
        no_exp_required = re.search(
            r"\bno\s+(?:prior\s+)?experience\b|\bminimal\s+experience\b|\bwithout\s+experience\b", 
            text, 
            re.IGNORECASE
        ) is not None
        
        # If it explicitly says no experience needed, mark as entry level
        if no_exp_required:
            is_entry_level = True
        else:
            is_entry_level = False
    
    # If no experience mentioned at all, it might be entry-level
    # This handles the "implicit entry-level" case
    if not has_experience_mention and not has_years_mention:
        is_entry_level = True
    
    # Check for data entry or assistant positions (likely entry-level)
    if re.search(r"\bdata\s+entry\b|\bassistant\b|\bintern\b|\bentry\b", text, re.IGNORECASE):
        is_entry_level = True
    
    # If we're filtering by skills, check if ANY skills match (one is enough)
    if required_skills:
        matched_skills = []
        for skill in required_skills:
            skill_patterns = [r'\b{}\b'.format(re.escape(skill))]
            
            # Add variations for common skills (similar to above)
            if skill.lower() == "sql":
                skill_patterns.extend([
                    r'\b(?:SQL|MySQL|PostgreSQL|MSSQL|SQLite|T-SQL|database|query|queries)\b',
                    r'\bdata\s?base\b',
                    r'\bdata\s?driven\b',
                ])
            elif skill.lower() == "python":
                skill_patterns.extend([
                    r'\b(?:Python|Django|Flask|pandas|NumPy|PyTorch|TensorFlow)\b',
                    r'\bscript(?:ing)?\b',
                    r'\bprogram(?:ming)?\b',
                ])
            elif skill.lower() == "excel":
                skill_patterns.extend([
                    r'\b(?:Excel|Microsoft Excel|Spreadsheet|Office|XLS)\b',
                    r'\bMS Office\b',
                    r'\bspreadsheet\b',
                ])
            elif skill.lower() == "tableau":
                skill_patterns.extend([
                    r'\b(?:Tableau|Data Visualization|PowerBI|dashboard|reporting)\b',
                    r'\bvisualization\b',
                    r'\breport(?:ing)?\b',
                ])
            elif skill.lower() == "linux":
                skill_patterns.extend([
                    r'\b(?:Linux|Unix|Bash|Shell|Ubuntu|CentOS)\b',
                    r'\bcommand\s?line\b',
                    r'\bterminal\b',
                ])
            
            # Check all patterns for this skill
            if any(re.search(pattern, text, re.IGNORECASE) for pattern in skill_patterns):
                matched_skills.append(skill)
        
        # Match ANY of the required skills (more flexible) - if entry-level
        return is_entry_level and len(matched_skills) > 0
    
    # If no skills required, just check if entry-level
    return is_entry_level

# Note: We're no longer using scrape_indeed since it was blocked by anti-scraping measures

def scrape_jobstreet(keyword, location, max_results=30, required_skills=None):
    print(f"Scraping JobStreet for '{keyword}' in '{location}'...")
    jobs = []
    
    # Also try entry-level specific searches
    entry_terms = ["", "entry-level", "junior", "fresh-graduate"]
    
    for term in [keyword] + [f"{term}-{keyword}" for term in entry_terms[1:]]:
        base_url = f"https://www.jobstreet.com.ph/{location}-jobs/{term.replace(' ', '-')}"
        
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            
            res = requests.get(base_url, headers=headers)
            if res.status_code != 200:
                print(f"Error accessing JobStreet: Status code {res.status_code}")
                continue
            
            # Debug info
            print(f"Got response from JobStreet for '{term}': {len(res.text)} characters")
                
            soup = BeautifulSoup(res.text, "html.parser")
            
            # Try different article selectors - updated for current JobStreet
            job_cards = soup.select("article") or soup.select("div[data-automation='job-card']") or soup.select(".job-card")
            
            if not job_cards:
                # Try more generic selectors
                job_cards = soup.find_all(attrs={"data-automation": "job-card"})
                if not job_cards:
                    print(f"No job cards found for {term}")
                    continue
            
            print(f"Found {len(job_cards)} job cards on JobStreet for '{term}'")
            
            for job in job_cards:
                try:
                    # Updated selectors for current JobStreet structure
                    title_elem = job.find(attrs={"data-automation": "job-title"}) or job.find("h1") or job.find("h2") or job.find("h3") or job.find("a", class_=lambda c: c and "title" in c.lower())
                    
                    company_elem = job.find(attrs={"data-automation": "job-company-name"}) or job.find("a", attrs={"data-automation": "jobCompany"}) or job.find("span", class_="company")
                    
                    # Try to get job description from multiple possible locations
                    snippet_elem = (
                        job.find(attrs={"data-automation": "job-description"}) or 
                        job.find("span", attrs={"data-automation": "job-description"}) or
                        job.find("div", class_="job-description") or
                        job.find("p", class_="job-description") or
                        job.find("div", class_=lambda c: c and "description" in c.lower())
                    )
                    
                    # If we couldn't find a title element, skip this job
                    if not title_elem:
                        print("No title element found")
                        continue
                    
                    title = title_elem.text.strip()
                    
                    # If title is empty, try to get it from attributes
                    if not title and title_elem.get("title"):
                        title = title_elem.get("title").strip()
                    
                    # Fix link to ensure it's a full URL
                    link = ""
                    if title_elem.has_attr("href"):
                        link = title_elem["href"]
                        if not link.startswith("http"):
                            link = "https://www.jobstreet.com.ph" + link
                    else:
                        # Look for any a tag that might be the link
                        a_elem = job.find("a", href=True)
                        if a_elem:
                            link = a_elem["href"]
                            if not link.startswith("http"):
                                link = "https://www.jobstreet.com.ph" + link
                        else:
                            print("No link found")
                            continue
                    
                    # Get company name and snippet text
                    company = company_elem.text.strip() if company_elem else "Unknown Company"
                    snippet = snippet_elem.text.strip() if snippet_elem else ""
                    
                    # Use the title from jobstreet-provided element or our fallback
                    if not title:
                        title = "Untitled Job"
                    
                    # Look for the job position in the h1 tag if available
                    h1_tag = job.find("h1")
                    if h1_tag and not title:
                        title = h1_tag.text.strip()
                    
                    # Full text to check for entry-level indicators
                    full_text = f"{title} {company} {snippet}"
                    
                    print(f"Processing JobStreet job: {title}")
                    
                    # Check if the job matches our criteria
                    if filter_entry_level(full_text, required_skills):
                        # Avoid duplicates based on title and company
                        job_key = (title, company)
                        if not any(job_key == (j["title"], j.get("company", "")) for j in jobs):
                            # Create a list of matched skills for reference
                            matched_skills = []
                            if required_skills:
                                for skill in required_skills:
                                    # Check for broader matches
                                    skill_patterns = [
                                        r'\b{}\b'.format(re.escape(skill)),
                                        r'\b{}s?\b'.format(re.escape(skill.rstrip('s')))  # Handle plural forms
                                    ]
                                    
                                    # Add skill-specific patterns
                                    if skill.lower() == "sql":
                                        skill_patterns.append(r'\b(?:SQL|MySQL|PostgreSQL|database|query)\b')
                                    elif skill.lower() == "python":
                                        skill_patterns.append(r'\b(?:Python|scripting|programming)\b')
                                    elif skill.lower() == "excel":
                                        skill_patterns.append(r'\b(?:Excel|Microsoft|spreadsheet|Office)\b')
                                    
                                    for pattern in skill_patterns:
                                        if re.search(pattern, full_text, re.IGNORECASE):
                                            matched_skills.append(skill)
                                            break
                            
                            jobs.append({
                                "platform": "JobStreet", 
                                "title": title, 
                                "company": company,
                                "link": link, 
                                "summary": snippet,
                                "matched_skills": matched_skills,
                                "keyword": keyword
                            })
                            print(f"Added job: {title}")
                except Exception as e:
                    print(f"Error parsing JobStreet job: {e}")
            
            # Add a short delay to avoid rate limiting
            time.sleep(random.uniform(0.5, 1))
        except Exception as e:
            print(f"Error scraping JobStreet: {e}")
    
    return jobs

def scrape_jooble(keyword, location, max_results=30, required_skills=None, api_key=None):
    """
    Search for jobs on Jooble using their API.
    
    Parameters:
    - keyword: Job title or keywords to search for
    - location: Location to search for jobs
    - max_results: Maximum number of results to return
    - required_skills: List of skills to filter jobs by
    - api_key: Your Jooble API key (required)
    
    Returns:
    - List of job dictionaries
    """
    if not api_key:
        print("Jooble API key is required. Please provide a valid API key.")
        return []
    
    print(f"Searching Jooble for '{keyword}' in '{location}'...")
    jobs = []
    
    # Determine how many pages to request based on max_results
    # Jooble returns 20 jobs per page by default
    results_per_page = 20
    pages_to_request = max(1, (max_results + results_per_page - 1) // results_per_page)
    
    # Add entry-level related terms to the search query
    entry_level_terms = ["", "entry level", "junior", "fresh graduate", "no experience"]
    
    for term in [keyword] + [f"{keyword} {t}".strip() for t in entry_level_terms if t]:
        for page in range(1, pages_to_request + 1):
            try:
                # Prepare the request payload
                payload = {
                    "keywords": term,
                    "location": location,
                    "page": str(page),
                    "ResultOnPage": str(min(max_results, results_per_page))
                }
                
                # Make the API request
                url = f"https://jooble.org/api/{api_key}"
                headers = {
                    "Content-Type": "application/json"
                }
                
                response = requests.post(url, headers=headers, data=json.dumps(payload))
                
                if response.status_code != 200:
                    print(f"Error accessing Jooble API: Status code {response.status_code}")
                    print(f"Response: {response.text}")
                    continue
                
                data = response.json()
                
                if "jobs" not in data or not data["jobs"]:
                    print(f"No jobs found for '{term}' on page {page}")
                    continue
                
                print(f"Found {len(data['jobs'])} jobs for '{term}' on page {page}")
                
                for job in data["jobs"]:
                    # Create a full text string for filtering - include more fields
                    full_text = f"{job.get('title', '')} {job.get('company', '')} {job.get('snippet', '')} {job.get('type', '')} {job.get('source', '')}"
                    
                    # Apply entry-level and skills filtering - improve skill matching
                    matched_skills = []
                    if required_skills:
                        for skill in required_skills:
                            # Create broader patterns for skill matching
                            skill_patterns = [
                                r'\b{}\b'.format(re.escape(skill)),
                                r'\b{}s?\b'.format(re.escape(skill.rstrip('s')))  # Handle plural forms
                            ]
                            
                            # Add skill-specific patterns - make more permissive
                            if skill.lower() == "sql":
                                skill_patterns.extend([
                                    r'\b(?:SQL|MySQL|PostgreSQL|database|query|queries|data\s?base)\b',
                                    r'\bdata[-\s]?driven\b',
                                    r'\brelational\s?database\b'
                                ])
                            elif skill.lower() == "python":
                                skill_patterns.extend([
                                    r'\b(?:Python|Django|Flask|pandas|scripting|programming)\b',
                                    r'\bcode\b',
                                    r'\bdevelop(?:ment|er)?\b'
                                ])
                            elif skill.lower() == "excel":
                                skill_patterns.extend([
                                    r'\b(?:Excel|Microsoft|spreadsheet|Office|XLS)\b',
                                    r'\bMS\s?Office\b',
                                    r'\bspreadsheets?\b',
                                    r'\bworkbooks?\b'
                                ])
                            elif skill.lower() == "tableau":
                                skill_patterns.extend([
                                    r'\b(?:Tableau|Power\s?BI|dashboard|visualization|reporting)\b',
                                    r'\bvisuali[sz]e\b',
                                    r'\bcharts?\b',
                                    r'\bgraphs?\b'
                                ])
                            elif skill.lower() == "linux":
                                skill_patterns.extend([
                                    r'\b(?:Linux|Unix|Bash|Shell|Ubuntu|CentOS|command\s?line)\b',
                                    r'\bterminal\b',
                                    r'\bopen\s?source\b'
                                ])
                            
                            for pattern in skill_patterns:
                                if re.search(pattern, full_text, re.IGNORECASE):
                                    matched_skills.append(skill)
                                    break
                    
                    # Debug: Print matched skills for this job
                    print(f"Job: '{full_text[:50]}...' - Matched skills: {matched_skills}")
                    
                    # If required skills specified, only include jobs that match at least one skill
                    if required_skills and not matched_skills:
                        continue
                    
                    # If job title doesn't contain keyword or related terms, check if it's relevant
                    title_lower = job.get('title', '').lower()
                    is_relevant = (
                        keyword.lower() in title_lower or
                        'analyst' in title_lower or 
                        'data' in title_lower or
                        'report' in title_lower or
                        any(term.lower() in title_lower for term in entry_level_terms if term) or
                        len(matched_skills) >= len(required_skills) // 2  # Match at least half of required skills
                    )
                    
                    # For non-relevant titles, require more skill matches
                    if not is_relevant and len(matched_skills) < 1:
                        continue
                    
                    # Create job entry
                    job_entry = {
                        "platform": "Jooble",
                        "title": job.get("title", ""),
                        "company": job.get("company", "Unknown Company"),
                        "location": job.get("location", location),
                        "link": job.get("link", ""),
                        "summary": job.get("snippet", ""),
                        "matched_skills": matched_skills,
                        "keyword": keyword,
                        "salary": job.get("salary", "")
                    }
                    
                    # Avoid duplicates
                    job_key = (job_entry["title"], job_entry["company"])
                    if not any(job_key == (j["title"], j.get("company", "")) for j in jobs):
                        jobs.append(job_entry)
                        print(f"Added job: {job_entry['title']}")
                
                # Delay between requests to avoid rate limiting
                time.sleep(random.uniform(1, 2))
                
            except Exception as e:
                print(f"Error processing Jooble results: {e}")
    
    return jobs

def search_all_roles(keywords, location="Philippines", max_results=30, required_skills=None, jooble_api_key=None, include_jobstreet=False):
    # Default skills if none provided - but make skills optional
    if required_skills == []:
        required_skills = None
    
    print(f"Searching for roles: {keywords} with skills: {required_skills}")
    
    all_jobs = []
    for role in keywords:
        # Add Jooble search if API key is provided
        jooble_jobs = []
        if jooble_api_key:
            jooble_jobs = scrape_jooble(role, location, max_results, required_skills, jooble_api_key)
        
        # Optionally include JobStreet results
        jobstreet_jobs = []
        if include_jobstreet:
            jobstreet_jobs = scrape_jobstreet(role, location, max_results, required_skills)
        
        print(f"Found {len(jooble_jobs)} Jooble jobs and {len(jobstreet_jobs)} JobStreet jobs for {role}")
        
        all_jobs.extend(jooble_jobs)
        all_jobs.extend(jobstreet_jobs)
    
    print(f"Total jobs found: {len(all_jobs)}")
    return all_jobs

# Define default roles for when this script is run directly
my_roles = [
    "data analyst",
    "business analyst",
    "business intelligence",
    "entry level python",
    "junior data scientist",
    "research assistant",
    "data engineer",
    "reporting analyst",
    "data reporting specialist",
    "ETL developer",
    "machine learning engineer",
    "data operations analyst"
]

# Define skills to filter by
my_skills = ["SQL", "Tableau", "Excel", "Python", "Linux"]

# Only run this when the script is executed directly (not imported)
if __name__ == "__main__":
    # You need to replace this with your actual Jooble API key
    JOOBLE_API_KEY = "NULL"
    
    results = search_all_roles(
        my_roles[:2], 
        location="Metro Manila", 
        max_results=10, 
        required_skills=my_skills, 
        jooble_api_key=JOOBLE_API_KEY,
        include_jobstreet=False  # Set to True to include JobStreet results
    )
    
    for job in results:
        print(f"[{job['platform']}] {job['title']} - {job.get('company', '')}")
        print(f"Link: {job['link']}")
        print(f"Skills matched: {', '.join(job.get('matched_skills', []))}")
        print(f"Summary: {job['summary']}")
        print("---\n")


