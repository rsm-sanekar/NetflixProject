# Netflix Content Intelligence Platform

A Streamlit analytics app that turns live TMDB movie and TV data into content-strategy decisions: what's in the market, what drives performance, where the gaps are, and what to greenlight next.

**Live demo:** https://netflixanalytics452.streamlit.app/
**Author:** [Shreya Anekar](https://github.com/rsm-sanekar)

---

## What it does

Six dashboards take a user from exploring the market to making a final call:

| Stage | Dashboard | Question it answers |
|---|---|---|
| Explore | Content Universe | What content exists, and how do quality and popularity relate? |
| Understand | Performance Deep Dive | Which metrics and patterns drive success? |
| Identify | Market Opportunities | Which genres are underserved, and when should titles release? |
| Predict | Recommendation Copilot | Given a genre, budget, and release quarter, what is the predicted popularity and hit probability? |
| Forecast | Predictive Forecasting | How will the top genres trend over the next 12 months? |
| Decide | Head-to-Head Comparison | Genre vs. genre or title vs. title: which option wins, and on which metrics? |

Every chart comes with a short note on how to read it and what to take from it.

## Data pipeline

- Pulls 10,000+ unique titles from 11 TMDB endpoints (popular, top rated, trending, discover, and more) for movies and TV
- Parallel fetching with a thread pool and connection pooling, so a full refresh runs in under a minute
- Cleaning, genre mapping, and a custom engagement score (`0.4 × popularity + 0.6 × vote quality weighted by vote count`)
- Results cached for one hour, so navigation and filtering are near-instant after the first load

## Models

| Model | Purpose |
|---|---|
| LightGBM regressor (XGBoost fallback) | Predict popularity for a proposed title, trained per genre |
| Random Forest classifier | Probability a title lands in the top 25% for engagement (balanced class weights) |
| Prophet | 12-month genre trend forecasts with yearly seasonality |
| Isolation Forest | Flag anomalous titles (about 2% contamination) across popularity, rating, vote count, and engagement |

Supporting analysis: Spearman correlation, Pareto (80/20) concentration, a market saturation index, release-window heatmaps, and popularity velocity for momentum.

## Tech stack

Python, Streamlit, Pandas, NumPy, Plotly, scikit-learn, LightGBM, XGBoost, Prophet, SciPy, NetworkX, TMDB API

## Run locally

```bash
git clone https://github.com/rsm-sanekar/NetflixProject.git
cd NetflixProject
pip install -r requirements.txt
```

Get a free API key from [TMDB](https://www.themoviedb.org/settings/api), then copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and add it (or set `TMDB_API_KEY` as an environment variable).

```bash
streamlit run app.py
```

The app opens at http://localhost:8501. The first load takes 30 to 60 seconds while it fetches data.

## Project walkthrough

[Netflix-Content-Intelligence-Platform.pdf](Netflix-Content-Intelligence-Platform.pdf) walks through each dashboard with screenshots and findings.

---

Data from [TMDB](https://www.themoviedb.org/). This project uses the TMDB API but is not endorsed or certified by TMDB, and it is not affiliated with Netflix.
