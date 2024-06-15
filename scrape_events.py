import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

with open('events_data.json', 'r') as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))

import pandas as pd

df = pd.read_csv('events_data.csv')
print(df)

def get_text_or_default(soup_element, default='N/A'):
    return soup_element.text.strip() if soup_element else default

def scrape_event_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if 'renegademarketing.com' in url:
        event_data = {
            "Event Name": "Top B2B Marketing Events",
            "Event Date(s)": 'N/A',
            "Location": 'N/A',
            "Website URL": url,
            "Description": get_text_or_default(soup.find('meta', {'name': 'description'}), 'N/A'),
            "Key Speakers": 'N/A',
            "Agenda/Schedule": 'N/A',
            "Registration Details": 'N/A',
            "Pricing": 'N/A',
            "Categories": 'Marketing',
            "Audience Type": 'Marketers',
        }
    elif 'inbound.com' in url:
        event_data = {
            "Event Name": get_text_or_default(soup.find('title')).split('-')[0].strip(),
            "Event Date(s)": get_text_or_default(soup.find('div', class_='inbound__hero__date')),
            "Location": get_text_or_default(soup.find('div', class_='inbound__hero__location')),
            "Website URL": url,
            "Description": get_text_or_default(soup.find('meta', {'name': 'description'})),
            "Key Speakers": [speaker.text.strip() for speaker in soup.find_all('h3', class_='speaker-name')] or 'N/A',
            "Agenda/Schedule": [item.text.strip() for item in soup.find_all('div', class_='agenda-item')] or 'N/A',
            "Registration Details": 'N/A',
            "Pricing": 'N/A',
            "Categories": 'Marketing, Sales',
            "Audience Type": 'Marketers, Sales Professionals',
        }
    elif 'generative-ai-summit.com' in url:
        event_data = {
            "Event Name": get_text_or_default(soup.find('h1')),
            "Event Date(s)": get_text_or_default(soup.find('div', class_='date')),
            "Location": get_text_or_default(soup.find('div', class_='location')),
            "Website URL": url,
            "Description": get_text_or_default(soup.find('meta', {'name': 'description'})),
            "Key Speakers": [speaker.text.strip() for speaker in soup.find_all('div', class_='speaker-name')] or 'N/A',
            "Agenda/Schedule": [item.text.strip() for item in soup.find_all('div', class_='agenda-item')] or 'N/A',
            "Registration Details": 'N/A',
            "Pricing": get_text_or_default(soup.find('div', class_='pricing')),
            "Categories": 'Artificial Intelligence',
            "Audience Type": 'AI Enthusiasts, Professionals',
        }
    elif 'saastrannual2024.com' in url:
        event_data = {
            "Event Name": get_text_or_default(soup.find('h1', class_='event-title')),
            "Event Date(s)": get_text_or_default(soup.find('div', class_='event-dates')),
            "Location": get_text_or_default(soup.find('div', class_='event-location')),
            "Website URL": url,
            "Description": get_text_or_default(soup.find('meta', {'name': 'description'})),
            "Key Speakers": [speaker.text.strip() for speaker in soup.find_all('div', class_='speaker-name')] or 'N/A',
            "Agenda/Schedule": [item.text.strip() for item in soup.find_all('div', class_='agenda-item')] or 'N/A',
            "Registration Details": 'N/A',
            "Pricing": 'N/A',
            "Categories": 'SaaS, Technology',
            "Audience Type": 'SaaS Professionals, Entrepreneurs',
        }
    elif 'salesforce.com' in url:
        event_data = {
            "Event Name": "Dreamforce",
            "Event Date(s)": get_text_or_default(soup.find('div', class_='date')),
            "Location": get_text_or_default(soup.find('div', class_='location')),
            "Website URL": url,
            "Description": get_text_or_default(soup.find('meta', {'name': 'description'})),
            "Key Speakers": [speaker.text.strip() for speaker in soup.find_all('div', class_='speaker-name')] or 'N/A',
            "Agenda/Schedule": [item.text.strip() for item in soup.find_all('div', class_='agenda-item')] or 'N/A',
            "Registration Details": 'N/A',
            "Pricing": 'N/A',
            "Categories": 'Technology, CRM',
            "Audience Type": 'CRM Professionals, Developers',
        }
    else:
        event_data = {
            "Event Name": 'N/A',
            "Event Date(s)": 'N/A',
            "Location": 'N/A',
            "Website URL": url,
            "Description": 'N/A',
            "Key Speakers": 'N/A',
            "Agenda/Schedule": 'N/A',
            "Registration Details": 'N/A',
            "Pricing": 'N/A',
            "Categories": 'N/A',
            "Audience Type": 'N/A',
        }
    return event_data

# URLs of the events
event_urls = [
    "https://renegademarketing.com/blog/the-top-b2b-marketing-events-on-our-radar/",
    "https://www.inbound.com/",
    "https://generative-ai-summit.com/",
    "https://www.saastrannual2024.com/",
    "https://www.salesforce.com/dreamforce/",
]

# Collect data for all events
events_data = []
for url in event_urls:
    events_data.append(scrape_event_data(url))

# Convert to DataFrame and then to CSV/JSON
df = pd.DataFrame(events_data)
df.to_csv('events_data.csv', index=False)
df.to_json('events_data.json', orient='records', indent=4)

print("Data scraped and saved successfully.")
