import job_scraper
import re

def debug_filter(description, skills):
    """Debug function to show step-by-step how the filter processes a job description"""
    print("--- DEBUG FILTER PROCESS ---")
    
    # Check for specific experience mentions
    has_experience_mention = "experience" in description.lower()
    has_years_mention = re.search(r"\b(?:years|yrs)\b", description, re.IGNORECASE) is not None
    is_entry_level = any(re.search(pattern, description, re.IGNORECASE) for pattern in [
        r"\bentry[\s-]?level\b",
        r"\bjunior\b", 
        r"\bjr\.?\b",
        r"\btrainee\b",
        r"\bbeginner\b"
    ])
    
    print(f"Has 'experience' mention: {has_experience_mention}")
    print(f"Has 'years' mention: {has_years_mention}")
    print(f"Has explicit entry-level terms: {is_entry_level}")
    
    # Check for skill matches
    if skills:
        matched_skills = []
        for skill in skills:
            skill_patterns = [r'\b{}\b'.format(re.escape(skill))]
            
            if skill.lower() == "excel":
                skill_patterns.extend([
                    r'\b(?:Excel|Microsoft Excel|Spreadsheet|Office|XLS)\b',
                    r'\bMS Office\b',
                    r'\bspreadsheet\b',
                ])
            
            for pattern in skill_patterns:
                if re.search(pattern, description, re.IGNORECASE):
                    print(f"Found skill match for {skill} using pattern: {pattern}")
                    matched_skills.append(skill)
                    break
        
        print(f"Matched skills: {matched_skills}")
    
    print("--------------------------")

# Test job descriptions
test_cases = [
    {
        "description": "Fresh graduate with 0-1 year experience needed for data entry role. Excel knowledge required.",
        "expected": True,
        "skills": ["Excel", "SQL"],
        "label": "Clear entry-level with Excel skill match"
    },
    {
        "description": "Senior Data Analyst with 5+ years experience in Python and SQL.",
        "expected": False,
        "skills": ["Python", "SQL"],
        "label": "Senior position - should be filtered out"
    },
    {
        "description": "Data entry position requiring Excel expertise. No specific experience mentioned.",
        "expected": True,
        "skills": ["Excel"],
        "label": "Implicit entry-level with skill match"
    },
    {
        "description": "Junior developer position. Knowledge of Python and SQL preferred.",
        "expected": True,
        "skills": ["Python", "SQL"],
        "label": "Junior position with skills"
    },
    {
        "description": "Financial analyst with strong Excel skills. 1 year experience.",
        "expected": True,
        "skills": ["Excel"],
        "label": "1 year experience - should match"
    },
    {
        "description": "Lead Data Scientist with 3 years experience in machine learning.",
        "expected": False,
        "skills": ["Python"],
        "label": "Lead position - should be filtered out"
    },
    {
        "description": "Marketing position with database management responsibilities.",
        "expected": True,
        "skills": ["SQL"],
        "label": "SQL skill match through 'database' mention"
    }
]

print("Testing entry-level filtering and skill matching...\n")

success = 0
total = len(test_cases)

for i, test in enumerate(test_cases):
    print(f"Test {i+1}: {test['label']}")
    print(f"Job: '{test['description']}'")
    print(f"Skills to match: {test['skills']}")
    
    # Debug info for failing test case
    if i == 2:  # The failing implicit entry-level case
        debug_filter(test["description"], test["skills"])
    
    result = job_scraper.filter_entry_level(test["description"], test["skills"])
    print(f"Expected: {test['expected']}, Actual: {result}")
    
    if result == test["expected"]:
        print("✓ PASS")
        success += 1
    else:
        print("✗ FAIL")
    
    print()

print(f"Results: {success}/{total} tests passed") 