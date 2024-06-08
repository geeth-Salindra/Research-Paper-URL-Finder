import requests
from bs4 import BeautifulSoup
from scholarly import scholarly

# List of research studies with their titles
research_studies = [
    {
        "title": "An Automated Timetabling System for University Courses",
        "authors": "Lewis, R., Paechter, B., & McCollum, B.",
        "journal": "European Journal of Operational Research"
    },
    {
        "title": "The Impact of Learning Analytics on Student Performance and Retention",
        "authors": "Siemens, G., & Long, P.",
        "journal": "Journal of Educational Technology & Society"
    },
    {
        "title": "Artificial Intelligence in Education: Promises and Implications for Teaching and Learning",
        "authors": "Luckin, R., Holmes, W., Griffiths, M., & Forcier, L. B.",
        "journal": "Learning, Media and Technology"
    },
    {
        "title": "Effective Strategies for Managing Student Absenteeism in Higher Education",
        "authors": "Moore, R., & Kearsley, G.",
        "journal": "Journal of Higher Education Policy and Management"
    },
    {
        "title": "Scalable and Adaptable Systems for Educational Resource Allocation",
        "authors": "Roberts, G., & Baker, M.",
        "journal": "Computers & Education"
    }
]

def get_url(title):
    search_query = scholarly.search_pubs(title)
    try:
        paper = next(search_query)
        if 'pub_url' in paper:
            return paper['pub_url']
        else:
            return None
    except StopIteration:
        print(f"No results found for title: {title}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error accessing paper URL for title '{title}': {e}")
        return None

# Loop through the research studies and find the URL for each paper
for study in research_studies:
    url = get_url(study["title"])
    if url:
        print(f"URL found for {study['title']}: {url}")
    else:
        print(f"URL not found for {study['title']}")
