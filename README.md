# Netflix Content Intelligence Platform

A Streamlit analytics app that turns live TMDB movie and TV data into content strategy insights: what is in the market, what drives performance, where the gaps are, and which content to prioritize next.

**Live app:** https://netflixanalytics452.streamlit.app/
**Author:** [Shreya Anekar](https://github.com/rsm-sanekar)

---

## Overview

The app is organized as six dashboards that take a user from exploring the market to making a decision:

| Stage | Dashboard | Question it answers |
|---|---|---|
| Explore | Content Universe | What content exists, and how do quality and popularity relate? |
| Understand | Performance Deep Dive | Which metrics and patterns are linked to strong performance? |
| Identify | Market Opportunities | Which genres are underserved, and when should titles be released? |
| Predict | Recommendation Copilot | For a given genre, content type, and release quarter, what popularity and hit probability can be expected? |
| Forecast | Predictive Forecasting | How are the top genres likely to trend over the next 12 months? |
| Decide | Head-to-Head Comparison | Genre vs. genre or title vs. title: which option is stronger, and on which metrics? |

Each chart includes a short explanation of how to read it and what it means for content strategy.

---

## Data pipeline

- **Ingestion:** pulls 10,000+ unique movie and TV titles from 11 TMDB endpoints (popular, top rated, now playing, upcoming, on the air, trending, and discover)
- **Parallel fetching:** requests run concurrently through a thread pool with connection pooling, which keeps a full data refresh fast
- **Transformation:** deduplication, genre mapping, and a custom engagement score that combines popularity with vote quality weighted by vote count
- **Caching:** results are cached for one hour, so navigation and filtering stay responsive after the first load

---

## Models and analysis

| Method | Purpose |
|---|---|
| LightGBM regressor (XGBoost fallback) | Predict popularity for a proposed title, trained on the selected genre and content type |
| Random Forest classifier | Estimate the probability that a title lands in the top 25% for engagement, with balanced class weights |
| Prophet | 12-month genre trend forecasts with yearly seasonality |
| Isolation Forest | Flag unusual titles across popularity, rating, vote count, and engagement |

Supporting analysis includes Spearman correlation, Pareto (80/20) concentration, a market saturation index, release-window heatmaps, and popularity velocity to track momentum.

---

## Tech stack

Python, Streamlit, Pandas, NumPy, Plotly, scikit-learn, LightGBM, XGBoost, Prophet, SciPy, NetworkX, TMDB API

---

## Run locally

```bash
git clone https://github.com/rsm-sanekar/NetflixProject.git
cd NetflixProject
pip install -r requirements.txt
```

Get a free API key from [TMDB](https://www.themoviedb.org/settings/api). Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and add the key, or set `TMDB_API_KEY` as an environment variable.

```bash
streamlit run app.py
```

The app opens at http://localhost:8501. The first load takes 30 to 60 seconds while data is fetched.

---

## Project walkthrough

[Netflix-Content-Intelligence-Platform.pdf](Netflix-Content-Intelligence-Platform.pdf) walks through each dashboard with screenshots and key findings.

---

Data from [TMDB](https://www.themoviedb.org/). This project uses the TMDB API but is not endorsed or certified by TMDB, and it is not affiliated with Netflix.
