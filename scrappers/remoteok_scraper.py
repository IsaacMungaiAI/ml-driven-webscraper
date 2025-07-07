import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

ua=UserAgent()
headers = {
    'User-Agent':ua.random,
    'Accept-Language':'en-US,en;q=0.9',
    'Accept':'text/html,application/xhtml',
}

BASE_URL= 'https://remoteok.com'

def scrape_remoteok(tags=['machine learning', 'mobile'], delay=2):
    jobs=[]

    for tag in tags:
        url=f'{BASE_URL}/remote-{tag}-jobs'
        print(f'Scraping {url}')

        try:
            res=requests.get(url,headers=headers)
            soup=BeautifulSoup(res.text,'html.parser')
            listings=soup.select('tr.job')

            for job in listings:
                try:
                    title=job.select_one("h2").get_text(strip=True)
                    company=job.select_one("h3").get_text(strip=True)
                    relative_link= job.get('data-href')
                    link=BASE_URL+relative_link if relative_link else "No link available"
                    tags=[tag.get_text(strip=True) for tag in job.select('.tag')]
                    date=job.select_one("time")
                    date_posted=date.get('datetime') if date else 'unknown'

                    jobs.append({
                        'title':title,
                        'company':company,
                        'tags':tags,
                        'link':link,
                        'date_posted':date_posted,
                        'source':'RemoteOk',
                    })

                except Exception as e:
                    print(f'Failed to parse a job row: {e}')
            time.sleep(delay)
        except Exception as e:
            print(f'Failed to fetch page : {e}')
    return jobs