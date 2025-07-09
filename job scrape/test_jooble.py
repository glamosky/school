import requests
import json
import sys

def test_jooble_api(api_key):
    """Test the Jooble API with a simple search"""
    print("Testing Jooble API...")
    
    # Prepare the API request
    url = f"https://jooble.org/api/{api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "keywords": "data analyst",
        "location": "Philippines",
        "page": "1",
        "ResultOnPage": "5"
    }
    
    try:
        # Make the API request
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            print(f"Success! Found {data.get('totalCount', 0)} total jobs.")
            
            # Print job details
            if 'jobs' in data and data['jobs']:
                print("\nJOB RESULTS:")
                for i, job in enumerate(data['jobs'], 1):
                    print(f"\nJob #{i}:")
                    print(f"Title: {job.get('title', 'N/A')}")
                    print(f"Company: {job.get('company', 'N/A')}")
                    print(f"Location: {job.get('location', 'N/A')}")
                    print(f"Salary: {job.get('salary', 'N/A')}")
                    # Print a snippet of the job description
                    snippet = job.get('snippet', 'N/A')
                    print(f"Description snippet: {snippet[:150]}..." if len(snippet) > 150 else f"Description: {snippet}")
            else:
                print("No jobs found in the response.")
                
            print("\nRaw API Response:")
            print(json.dumps(data, indent=2))
        else:
            print(f"Error: API returned status code {response.status_code}")
            print(f"Response: {response.text}")
    
    except Exception as e:
        print(f"Error testing Jooble API: {e}")

if __name__ == "__main__":
    # Check if API key was provided as command-line argument
    if len(sys.argv) > 1:
        api_key = sys.argv[1]
    else:
        # Use the API key from your previous code
        api_key = "fdee36f0-c7ca-4c9a-a4a6-395c4bcaa4b6"
    
    test_jooble_api(api_key) 