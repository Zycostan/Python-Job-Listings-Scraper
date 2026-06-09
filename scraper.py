from os import link

import requests, csv
from bs4 import BeautifulSoup

def scrape_jobs():
    res = requests.get('https://realpython.github.io/fake-jobs/') #requests the shit

    soup =  BeautifulSoup(res.content, 'html.parser') # this parses it

    job = soup.find_all('div', attrs={'class': 'card-content'}) # finds all of the job cards

    with open('job_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        headers = ['Job Title', 'Company', 'Location', 'Link']
        writer.writerow(headers)
        
    
        for card in job:
            title = card.find('h2', attrs={'class': 'title'}).text.strip() # SHOULD get the title of the jobs n' shit
            company = card.find('h3', attrs={'class': 'company'}).text.strip() # SHOULD get the company of the jobs
            location = card.find('p', attrs={'class': 'location'}).text.strip() # SHOULD get the location of the jobs

            rizz  = card.find_all('a')
            if rizz:
                link = rizz[1]['href']
            else:
                link = 'ITS NOT THERE BRO'
            
            writer.writerow([title, company, location, link]) # THIS SHIT WRITES IT INTO THE CSV
        
        

if __name__ == '__main__':
    scrape_jobs()

    # DONE, FUCK THIS