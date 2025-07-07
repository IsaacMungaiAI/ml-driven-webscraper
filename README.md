# 🔍 ML Job & Hackathon Notifier

A smart web scraper that finds and filters **machine learning** and **mobile app development** opportunities from the web using **semantic similarity models**. It scrapes job listings and hackathons, ranks them using NLP, and sends relevant ones as notifications.
You can fine tune it to suit your desires
Built by [Isaac Mungai](https://github.com/IsaacMungaiAI) – Machine Learning & Mobile App Developer.

---

## 🚀 Features

- ✅ Scrapes jobs from [RemoteOK](https://remoteok.com/)
- ✅ Uses `sentence-transformers` to semantically rank job relevance
- ✅ Filters listings based on ML and mobile development interests
- ✅ Easy to extend with new job sources (e.g., Devpost, AngelList)
- ✅ Designed for automation and future deployment

---

## 📁 Project Structure

ml-job-notifier/
├── scrapers/ # Web scraping modules
│ └── remoteok_scraper.py
├── model/ # Semantic similarity ranking
│ ├── embedder.py
│ └── ranker.py
├── notifier/ # Email/Telegram notification (to be added)
├── requirements.txt # Python dependencies
├── main.py # Entry point
└── README.md # This file



---

## 🧠 How It Works

1. Scrapes job data from RemoteOK by keyword tags.
2. Converts job titles & tags into embeddings using Sentence-BERT.
3. Computes cosine similarity against predefined interest topics.
4. Filters and prints or stores jobs above the similarity threshold.

---

## 🔧 Installation

```bash
# Clone the repo
git clone https://github.com/your-github-username/ml-driven-webscraper.git
cd ml-driven-webscraper

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt


Run the Project
python main.py


✅ Tech Stack
Python 3.11

sentence-transformers

BeautifulSoup + requests

Scikit-learn for similarity scoring


 Example Output
📌 Android Engineer at OpenAI (Score: 0.61)
🏷️ Tags: remote, react-native, android
🔗 https://remoteok.com/remote-jobs/abc123
📅 Posted: 2025-07-05
