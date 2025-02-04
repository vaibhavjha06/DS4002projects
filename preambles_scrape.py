import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_constitution_links(base_url):
    links = []
    while True:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        constitution_elements = soup.select("a[href*='/constitution/']")
        new_links = [a['href'] for a in constitution_elements if 'constitution' in a['href']]
        if not new_links:  # Stop if no new links are found
            break
        links.extend(new_links)
        next_page = soup.find('a', attrs={'rel': 'next'})
        if not next_page:
            break
        base_url = f"https://constituteproject.org{next_page['href']}"
    return set(links)  # Remove duplicates

def scrape_preamble(links):
    data = []
    for link in links:
        full_url = f"https://constituteproject.org{link}"
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        preamble_section = soup.find('div', id='s1')  # Adjust selector if needed
        if preamble_section:
            preamble_text = preamble_section.get_text(strip=True)
            data.append((link.split('/')[-1].replace('_', ' '), preamble_text))
        else:
            data.append((link.split('/')[-1].replace('_', ' '), "No preamble found"))
    return data

def save_to_excel(data):
    df = pd.DataFrame(data, columns=['Country', 'Preamble'])
    df.to_excel('preambles.xlsx', index=False)

# Main execution
base_url = "https://constituteproject.org/constitutions?lang=en&status=in_force&status=is_draft"
constitution_links = get_constitution_links(base_url)
preamble_data = scrape_preamble(constitution_links)
save_to_excel(preamble_data)

print("Done scraping and saving preambles to Excel.")
