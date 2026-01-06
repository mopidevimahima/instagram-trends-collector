# 📱 Instagram Trends Collector

Automated Python scraper that collects **Instagram Reels trends & trending audio** daily from Later.com. Perfect for content creators.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Demo-brightgreen.svg)](https://streamlit.io/)

## 🎯 What it does

- **Scrapes** [Later.com Instagram Trends](https://later.com/blog/instagram-reels-trends/) weekly updates
- **Extracts** 100+ trending sounds, challenges, audio clips (e.g., "I Wanna Thank Me", "Girl to Girl")
- **Saves** to `trends.csv` with timestamps
- **Runs automatically** daily via Windows Task Scheduler
- **Dashboard** with Streamlit to browse/filter trends

**Live demo**: Scraped **144 real trends** from Jan 2026 (see `trends.csv`)

## 📊 Sample Data

| trend_name | platform | source | found_at |
|------------|----------|--------|----------|
| Trend: I Wanna Thank Me — January 2, 2026 | Instagram Reels | later.com | 2026-01-06 10:50:00 |
| Trend: Girl to Girl — January 2, 2026 | Instagram Reels | later.com | 2026-01-06 10:50:00 |

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/instagram-trends-collector
cd instagram-trends-collector

# 2. Install
pip install -r requirements.txt

# 3. Run scraper
python trends.py
# → Creates trends.csv with 144+ trends

# 4. View dashboard
streamlit run viewer.py
