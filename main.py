from scrappers.remoteok_scraper import scrape_remoteok

if __name__ == '__main__':
    jobs = scrape_remoteok(tags=['machine-learning', 'android', 'react-native'])

    for job in jobs:
        print(f"\n📌 {job['title']} at {job['company']}")
        print(f"🏷️ Tags: {', '.join(job['tags'])}")
        print(f"🔗 {job['link']}")
        print(f"📅 Posted: {job['date_posted']}")