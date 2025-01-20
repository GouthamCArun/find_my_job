from linkedin_api import Linkedin
from typing import List, Dict, Literal, Optional

def search_jobs(
    keywords: Optional[str] = None,
    companies: Optional[List[str]] = None,
    experience: Optional[List[Literal['1', '2', '3', '4', '5', '6']]] = None,
    job_type: Optional[List[Literal['F', 'C', 'P', 'T', 'I', 'V', 'O']]] = None,
    job_title: Optional[List[str]] = None,
    industries: Optional[List[str]] = None,
    location_name: Optional[str] = None,
    remote: Optional[List[Literal['1', '2', '3']]] = None,
    listed_at: int = 86400,  # Default to 24 hours
    distance: Optional[int] = None,
    limit: int = -1,  # Default to no limit
    offset: int = 0,
    **kwargs
) -> List[Dict]:
    """
    Perform a LinkedIn search for jobs using the Linkedin API.

    Parameters are described as per the job search requirements in LinkedIn.

    Returns:
        list: A list of job listings
    """
    
    # Replace with your LinkedIn credentials
    user_cred=os.getenv("USERNAME")
    pas=os.getenv("PASS")
    api = Linkedin(user_cred, pas)
    
    # Perform the job search (using the search method available in linkedin_api)
    results = api.search_jobs(
        keywords=keywords,
        companies=companies,
        experience=experience,
        job_type=job_type,
        job_title=job_title,
        industries=industries,
        location_name=location_name,
        remote=remote,
        listed_at=listed_at,
        distance=distance,
        limit=limit,
        offset=offset,
        **kwargs
    )
    return results

def find_jobs(skill_list):
    # Dynamic keyword list

    # List to store the job details
    job_list = []

    # Iterate over keywords and search jobs
    for keyword in skill_list:
        print(f"\nSearching jobs for keyword: {keyword}")
        results = search_jobs(
            keywords=keyword,
            companies=None,                  # No specific companies
            experience=["2", "3"],           # Entry level, Associate
            job_type=["F"],                  # Full-time jobs
            job_title=None,                  # No specific job title URNs
            industries=None,                 # No specific industries
            location_name="New York",        # Search within New York location
            remote=["2"],                    # Remote jobs (remote: "2")
            listed_at=86400,                 # Posted within the last 24 hours
            distance=25,                     # Within 25 miles
            limit=10,                        # Limit to 10 results
            offset=0                         # Start from the first result
        )
        
        # Append job details to the list
        for job in results:
            entity_urn = job.get('entityUrn', None)
            if entity_urn:
                job_url = f"https://www.linkedin.com/jobs/view/{entity_urn.split(':')[-1]}/"
                job_details = {
                    "title": job.get('title', 'Unknown'),
                    "company": job.get('companyName', 'Unknown'),
                    "url": job_url
                }
                job_list.append(job_details)
    return job_list

# Print the final job list
# print(find_jobs(["Data Scientist"]))
