import requests
from bs4 import BeautifulSoup
import sys

def test_indeed():
    print("Testing connection to Indeed...")
    url = "https://ph.indeed.com/jobs?q=data+analyst&l=Philippines"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"Status code: {response.status_code}")
        print(f"Content length: {len(response.text)} characters")
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Try to find job cards
        job_cards = soup.select("div.job_seen_beacon") or soup.select("div.jobsearch-SerpJobCard") or soup.select("div.result")
        print(f"Job cards found: {len(job_cards)}")
        
        # If no job cards found with standard selectors, look for any potential job-related divs
        if not job_cards:
            potential_cards = soup.find_all("div", attrs={"data-jk": True})
            print(f"Potential cards with data-jk attribute: {len(potential_cards)}")
            
            # Look for any divs with 'job' in class name
            job_divs = soup.find_all("div", class_=lambda c: c and ("job" in c.lower()))
            print(f"Divs with 'job' in class name: {len(job_divs)}")
            
            # Check for any anchor tags with job titles
            job_links = soup.find_all("a", string=lambda s: s and "analyst" in s.lower())
            print(f"Links containing 'analyst': {len(job_links)}")
            
            # Save HTML for inspection
            with open("indeed_response.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Saved HTML response to indeed_response.html")
        
    except Exception as e:
        print(f"Error: {e}")

def test_jobstreet():
    print("\nTesting connection to JobStreet...")
    url = "https://www.jobstreet.com.ph/Philippines-jobs/data-analyst"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"Status code: {response.status_code}")
        print(f"Content length: {len(response.text)} characters")
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Try to find job cards
        job_cards = soup.select("article") or soup.select("div[data-automation='job-card']") or soup.select(".job-card")
        print(f"Job cards found: {len(job_cards)}")
        
        # If no job cards found with standard selectors, try alternative approaches
        if not job_cards:
            job_cards = soup.find_all(attrs={"data-automation": "job-card"})
            print(f"Job cards with data-automation='job-card': {len(job_cards)}")
            
            # Look for job titles
            job_titles = soup.find_all(attrs={"data-automation": "job-title"})
            print(f"Elements with data-automation='job-title': {len(job_titles)}")
            
            # Save HTML for inspection
            with open("jobstreet_response.html", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Saved HTML response to jobstreet_response.html")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        print(f"Python version: {sys.version}")
        print(f"Requests version: {requests.__version__}")
        
        test_indeed()
        test_jobstreet()
        
    except Exception as e:
        print(f"Overall error: {e}") 