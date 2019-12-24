import json
import requests
from bs4 import BeautifulSoup


with open('archive-18.html') as f:
    soup = BeautifulSoup(f, 'lxml')

print("Done")

link_tags = soup.findAll('a', class_='organization-card__link')


org_links = [ ('https://summerofcode.withgoogle.com' + link.attrs['href']) for link in link_tags ]
print(len(org_links))
print(org_links[0])

organizations = []

for link in org_links:
    org_page = requests.get(link)
    soup = BeautifulSoup(org_page.content)    
    org_name = soup.find('h3', class_='banner__title').text
    org_url = soup.find('p', class_="page-organizations__org-url").a.attrs['href']
    org_description = soup.find('div', class_="org__long-description").p.text
    org_technologies = [li.text for li in soup.findAll('li', class_='organization__tag organization__tag--technology')]
    organization = {
        'name': org_name,
        'website': org_url,
        'description': org_description,
        'technologies': org_technologies
    }
    organizations.append(organization)
    print(org_name)

print(organizations[0])

with open('orgs-18.json', 'w') as file:
    json.dump(organizations, file)

