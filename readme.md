# 📰 NewzScrapper

A Python-based automated news scraper and AI-powered summarizer that fetches top headlines from **Hacker News**, scrapes full article content, analyzes it using **Google Gemini**, and sends formatted notifications via **ntfy.sh**.

---

## 📂 Project Structure

```
└── tecanmol-newzscrapper/
    ├── analyze.py
    ├── main.py
    ├── notify.py
    ├── ScrapData.py
    └── ScrapLinks.py
```

---

## 🚀 Features

* Scrapes top **10 headlines** from Hacker News.
* Extracts full article content using multiple fallback selectors.
* Sends all scraped data to **Gemini 2.5 Flash** for summary analysis.
* Receives structured JSON output with:

  * TL;DR
  * Key Takeaways
  * Category
  * Original link
* Sends formatted notifications through **ntfy.sh**.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/tecanmol/NewzScrapper.git
cd tecanmol-newzscrapper
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

(If `requirements.txt` doesn’t exist, install manually:)

```bash
pip install requests beautifulsoup4 python-dotenv google-genai
```

### 3️⃣ Add your Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 📌 How It Works

### **1. Scraping Headlines — `ScrapLinks.py`**

* Fetches Hacker News HTML
* Extracts rank, title, and direct article link using CSS selectors
* Stops after collecting the top **10 articles**

### **2. Scraping Full Article — `ScrapData.py`**

Tries multiple selectors to extract article text:

* `article`
* `.content`, `.entry-content`, `.prose`, etc.

Returns fallbacks if nothing is found.

### **3. AI Summary Analysis — `analyze.py`**

Sends cleaned JSON payload to Gemini with a structured prompt.
Gemini returns:

* TL;DR
* Key Takeaways
* Category
* Link

### **4. Sending Notification — `notify.py`**

Uses `ntfy.sh` topic **personal_newz_scrapper0808** to push each summary.

---

## ▶️ Running the Project

Run the main script:

```bash
python main.py
```

You will see logs like:

```
Fetching headlines...
Scraping: Example Title...
Analyzing all articles...
sent: Example Title
```

Notifications will appear in your ntfy client.

---

## 📤 Output Example (Sent to ntfy.sh)

```
Title: OpenAI Releases New Model
TL;DR: A major breakthrough in AI performance.
Key Takeaways:
    - Faster inference
    - Lower cost
    - More accurate
Category: AI
Link: https://example.com/article
```

---

## 🧩 File Overview

### **analyze.py**

Handles sending collected data to Gemini for structured summarization.

### **main.py**

Main runner:

* Scrapes
* Processes
* Analyzes
* Sends notifications

### **notify.py**

Simple wrapper for posting messages to ntfy.

### **ScrapData.py**

Scrapes article body content using BeautifulSoup.

### **ScrapLinks.py**

Extracts top Hacker News headline links.

---

## 🤝 Contributing

Pull requests and improvements are welcome!

---

## 📜 License

MIT License.

---

## ⭐ Acknowledgements

* Hacker News
* Google Gemini API
* ntfy.sh notification service
