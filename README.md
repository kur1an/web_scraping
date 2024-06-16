# B2B Events Data Scraping

## Description
This script scrapes data from several B2B event websites and compiles the information into structured JSON and CSV files. The following event websites are included:
- [Renegade Marketing](https://renegademarketing.com/blog/the-top-b2b-marketing-events-on-our-radar/)
- [INBOUND](https://www.inbound.com/)
- [Generative AI Summit](https://generative-ai-summit.com/)
- [SaaStr Annual 2024](https://www.saastrannual2024.com/)
- [Salesforce Dreamforce](https://www.salesforce.com/dreamforce/)

## Scraped Information
The script extracts the following information for each event:
- Event Name
- Event Date(s)
- Location (if applicable)
- Website URL
- Description
- Key Speakers
- Agenda/Schedule
- Registration Details
- Pricing
- Categories
- Audience Type

## Prerequisites
Ensure you have Python installed on your machine. You will also need the following Python packages:
- requests
- beautifulsoup4
- pandas

You can install these packages using pip:
```bash
pip install requests beautifulsoup4 pandas
