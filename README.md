# Netflix Content Intelligence Platform

## 🎯 Project Overview

The **Netflix Content Intelligence Platform** is a comprehensive, data-driven analytics dashboard designed for entertainment industry professionals, content strategists, and business decision-makers. This application transforms raw entertainment data into strategic insights through advanced visualizations, statistical analysis, and machine learning predictions.

Built as a complete decision-support system, it enables users to explore market landscapes, identify opportunities, predict performance, and validate investment decisions—all backed by real data from **The Movie Database (TMDB)** covering **6000+ titles** across movies and TV shows.

---

## 📊 What This Platform Does

### The Complete Analytical Journey

This platform guides you through **six strategic stages** of content analysis:

| Stage | Dashboard | Question Answered |
|-------|-----------|-------------------|
| **EXPLORE** | Content Universe | What content exists in the market? |
| **UNDERSTAND** | Performance Deep Dive | What patterns drive success? |
| **IDENTIFY** | Market Opportunities | Where are the opportunities? |
| **PREDICT** | Recommendation Copilot | Should I invest in this? |
| **FORECAST** | Predictive Forecasting | What will happen next? |
| **DECIDE** | Head-to-Head Comparison | Which option is better? |

Each dashboard builds on the previous one, creating a logical flow from market exploration to final investment decisions.

---

## 🚀 Key Features & Capabilities

### Six Intelligence Dashboards

#### 1. Content Universe (Market Landscape)
- **Purpose:** Get baseline understanding of the content market
- **Key Insights:** Genre distribution, quality vs popularity patterns, top performers
- **Business Use:** Market composition analysis, competitive benchmarking
- **Charts:** 6+ visualizations including genre bars, scatter plots, performance matrices, poster grids
- **Special Feature:** Shows ALL content types (Movies + TV combined) with separate tabs for detailed analysis

#### 2. Performance Deep Dive (Statistical Analysis)
- **Purpose:** Identify what metrics and patterns drive content success
- **Key Insights:** Correlation analysis, anomaly detection, seasonal patterns, engagement drivers
- **Business Use:** Success factor identification, content strategy optimization
- **Charts:** 6+ visualizations including Spearman correlation heatmaps, Isolation Forest anomaly scatter, monthly trends
- **Special Feature:** Multi-dimensional anomaly detection using Isolation Forest algorithm (~2% outlier detection)

#### 3. Market Opportunities (Strategic Intelligence)
- **Purpose:** Find underserved market segments with high potential
- **Key Insights:** Market saturation analysis, 80/20 distribution, optimal release timing
- **Business Use:** Portfolio gap analysis, competitive positioning, launch planning
- **Charts:** 5+ visualizations including bubble charts (GREEN/RED zones), Pareto analysis, release window heatmaps
- **Special Feature:** Market Saturation Index with color-coded opportunity zones

#### 4. Recommendation Copilot (ML-Powered Advisor)
- **Purpose:** Get quantitative predictions for specific content investments
- **Key Insights:** Popularity forecasts, budget impact curves, risk assessment, similar title benchmarks
- **Business Use:** Investment validation, greenlight decisions, risk evaluation
- **Interactive Controls:** Genre selector, content type, budget slider (1-10), release quarter
- **Machine Learning:** LightGBM Regressor + Random Forest Classifier
- **Charts:** 4+ visualizations including forecast curves, radar profiles, benchmark posters
- **Special Feature:** Outputs comprehensive recommendation with hit probability and risk level

#### 5. Predictive Forecasting (Future Trends)
- **Purpose:** Anticipate market conditions 6-12 months ahead
- **Key Insights:** Genre trend forecasts, seasonal patterns, momentum tracking, velocity analysis
- **Business Use:** Strategic planning, portfolio rebalancing, timing optimization
- **Machine Learning:** Facebook Prophet models predict 12-month trends for top 6 genres
- **Charts:** 5+ visualizations including multi-line forecasts, velocity rankings
- **Special Feature:** Rising stars analysis identifying viral content by engagement velocity

#### 6. Head-to-Head Comparison (Final Decision Tool)
- **Purpose:** Direct comparison between two options to make final choice
- **Comparison Modes:** Genre vs Genre OR Title vs Title
- **Key Insights:** Side-by-side metrics, winner identification, historical trends, performance deltas
- **Business Use:** Final greenlight decisions, A/B investment choices, competitive analysis
- **Charts:** 4+ visualizations including metrics tables, diverging bars, trend lines
- **Special Feature:** Auto-calculated winner with score based on metrics won

---

## 🤖 Machine Learning & Advanced Analytics

### Five Production ML Models

| Model | Algorithm | Use Case | Dashboard |
|-------|-----------|----------|-----------|
| **LightGBM Regressor** | Gradient Boosting | Popularity Prediction | Recommendation Copilot |
| **XGBoost Regressor** | Gradient Boosting (Fallback) | Popularity Prediction | Recommendation Copilot |
| **Random Forest Classifier** | Ensemble Classification | Hit Probability | Recommendation Copilot |
| **Facebook Prophet** | Time Series Forecasting | 12-Month Genre Trends | Predictive Forecasting |
| **Isolation Forest** | Unsupervised Anomaly Detection | Outlier Identification | Performance Deep Dive |

### Model Details

#### LightGBM Regressor (Primary - Popularity Prediction)
```python
LGBMRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=-1,          # No limit, let boosting decide
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
```
- **Training Data:** Vote average, vote count per genre
- **Output:** Predicted popularity score
- **Accuracy:** Trained per-genre for higher precision

#### XGBoost Regressor (Fallback)
```python
XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    objective="reg:squarederror"
)
```
- **Use Case:** Automatic fallback if LightGBM fails

#### Random Forest Classifier (Hit Probability)
```python
RandomForestClassifier(
    n_estimators=300,
    max_depth=None,
    min_samples_split=4,
    class_weight="balanced",  # Handles class imbalance
    random_state=42
)
```
- **Training Data:** Vote average, vote count, release quarter
- **Target:** Top 25th percentile engagement (binary classification)
- **Output:** Probability score (0-100%)

#### Facebook Prophet (Time Series Forecasting)
```python
Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False,
    seasonality_mode="multiplicative"
)
```
- **Training Data:** Historical monthly engagement scores
- **Output:** 12 future monthly predictions per genre
- **Features:** Automatic seasonality detection, trend modeling

#### Isolation Forest (Anomaly Detection)
```python
IsolationForest(
    n_estimators=200,
    contamination=0.02,    # ~2% outliers
    random_state=42
)
```
- **Detection Features:** Popularity, vote average, vote count, engagement score
- **Output:** Boolean flag for anomalous titles
- **Visualization:** Red dots on scatter plots

### Advanced Analytical Techniques

- **Spearman Correlation:** Non-parametric correlation for metric relationships
- **Pareto Analysis:** 80/20 rule visualization for content concentration
- **Engagement Scoring:** Custom formula: `popularity * 0.4 + (vote_average * vote_count_factor) * 0.6`
- **Market Saturation Mapping:** Multi-dimensional bubble charts with opportunity zones
- **Velocity Analysis:** Popularity per day since release for momentum tracking

---

## 📈 Visualization Excellence

### 28+ Interactive Charts

Every chart in the platform includes:
- **Chart Analysis Section:** Explains what the chart shows and how to read it
- **Insight Panels:** 3-4 actionable takeaways with highlighted key metrics
- **Interactive Features:** Hover details, zoom, pan capabilities
- **Professional Styling:** Netflix-inspired dark theme with color-coded genres

### Chart Categories

| Category | Examples | Purpose |
|----------|----------|---------|
| **Distribution** | Bar charts, histograms | Volume and spread analysis |
| **Correlation** | Scatter plots, heatmaps | Relationship discovery |
| **Trend** | Line charts, area charts | Change tracking |
| **Comparison** | Diverging bars, dual axes | Head-to-head analysis |
| **Forecast** | Predictive curves | Future projections |
| **Matrix** | Heatmaps | Release timing optimization |

### Color-Coded Genre System

Consistent across all dashboards for instant pattern recognition:

| Genre | Color | Hex Code |
|-------|-------|----------|
| Drama | Purple | `#8b5cf6` |
| Action | Red | `#ef4444` |
| Comedy | Yellow | `#fbbf24` |
| Science Fiction | Blue | `#3b82f6` |
| Horror | Dark Red | `#7f1d1d` |
| Romance | Pink | `#ec4899` |
| Thriller | Dark Red | `#991b1b` |
| Animation | Green | `#10b981` |
| Documentary | Indigo | `#6366f1` |
| Fantasy | Purple | `#a855f7` |

---

## 💼 Business Value & Use Cases

### For C-Suite Executives

**Use the platform to:**
- Make data-driven greenlight decisions with ML predictions
- Identify portfolio gaps and rebalancing opportunities
- Understand competitive positioning across genres
- Evaluate ROI potential before content acquisition

**Typical Workflow:** Dashboard 1 → Dashboard 3 → Dashboard 4 → Dashboard 6

### For Content Strategists

**Use the platform to:**
- Optimize release calendars by genre-specific windows
- Track emerging trends and momentum shifts
- Benchmark performance against top titles
- Plan content mix for maximum engagement

**Typical Workflow:** Dashboard 2 → Dashboard 3 → Dashboard 5

### For Data Analysts

**Use the platform to:**
- Explore statistical relationships and correlations
- Validate hypotheses with anomaly detection
- Extract insights for presentation decks
- Build custom analysis using interactive filters

**Typical Workflow:** All dashboards with deep filtering

### Real-World Scenario Example

**Scenario: New Sci-Fi Content Acquisition**

| Step | Dashboard | Finding |
|------|-----------|---------|
| 1 | Market Opportunities | Sci-fi in GREEN zone (low competition, high performance) |
| 2 | Predictive Forecasting | +25% growth projected over 12 months |
| 3 | Recommendation Copilot | Predicted popularity: 78, Hit probability: 68% |
| 4 | Head-to-Head Comparison | Sci-fi wins vs Drama on 5/7 metrics |

**Decision:** GREENLIGHT with medium risk, strong upside

---

## 🛠️ Technical Architecture

### Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| **Framework** | Streamlit | 1.28+ |
| **Data Processing** | Pandas, NumPy | 2.0+, 1.24+ |
| **Visualizations** | Plotly | 5.18+ |
| **ML - Gradient Boosting** | LightGBM, XGBoost | 4.1+, 2.0+ |
| **ML - Classification** | scikit-learn | 1.3+ |
| **ML - Time Series** | Prophet | 1.1.5+ |
| **Statistical Analysis** | SciPy | 1.11+ |
| **Network Analysis** | NetworkX | 3.2+ |
| **Data Source** | TMDB API | v3 |

### Data Pipeline

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   TMDB API      │────▶│  Data Enrichment│────▶│  Feature        │
│   (11 endpoints)│     │  & Cleaning     │     │  Engineering    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
┌─────────────────┐     ┌─────────────────┐            ▼
│  Visualization  │◀────│  ML Inference   │◀────┌─────────────────┐
│  & Insights     │     │  (On-demand)    │     │  Caching        │
└─────────────────┘     └─────────────────┘     │  (1 hour TTL)   │
                                                └─────────────────┘
```

### High-Performance Data Fetching

```python
# Parallel API fetching with ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=64) as executor:
    # 11 endpoints × up to 500 pages = 5,500+ potential requests
    # Connection pooling with 100 connections
    # Result: 10,000+ unique titles in under 60 seconds
```

### Performance Metrics

| Metric | Value |
|--------|-------|
| First load | 30-60 seconds (API fetch + processing) |
| Subsequent navigation | <1 second (cached) |
| Filter updates | <0.5 seconds |
| Memory usage | ~300MB |
| Unique titles | 10,000+ |

---

## 📦 Installation & Setup

### System Requirements

- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- Internet connection (for TMDB API)
- Modern web browser

### Quick Start (3 Steps)

```bash
# 1. Clone or download the project
git clone https://github.com/yourusername/netflix-intelligence.git
cd netflix-intelligence

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
streamlit run app.py

# Opens automatically at http://localhost:8501
```

### Dependencies (requirements.txt)

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.18.0
requests>=2.31.0
scipy>=1.11.0
networkx>=3.2
scikit-learn>=1.3.0
xgboost>=2.0.0
lightgbm>=4.1.0
prophet>=1.1.5
```

### Prophet Installation Note

Prophet may require additional setup on some systems:

```bash
# For Mac/Linux
pip install prophet

# For Windows (if issues occur)
conda install -c conda-forge prophet
```

---

## 🎨 Design Philosophy

### Netflix-Inspired Professional Theme

| Element | Color | Purpose |
|---------|-------|---------|
| Background | `#0A0A0A` | Pure black, premium feel |
| Accent | `#E50914` | Netflix red for highlights |
| Cards | `#1A1A1A` | Content separation |
| Text | `#FFFFFF` | Maximum readability |
| Secondary | `#B3B3B3` | Supporting information |

### User Experience Principles

- **Progressive Disclosure:** Simple overview → detailed analysis
- **Minimal Clicks:** Key insights accessible in 1-2 clicks
- **Consistent Navigation:** Same pattern across all dashboards
- **Explanatory Text:** Every chart has "how to read this" guidance
- **Actionable Insights:** Not just data, but what to DO with it

---


## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Total Dashboards | 6 |
| Total Charts | 28+ |
| ML Models | 5 |
| Data Points | 10,000+ titles |
| Genres Covered | 27 categories |
| Code Lines | ~1,500 |
| Years of Data | 1990-2025 |

---

## 🎯 What Makes This Platform Unique

| Feature | Description |
|---------|-------------|
| **Complete Journey** | Full decision-making workflow, not just charts |
| **ML-Powered** | Real predictions with LightGBM, Prophet, Random Forest |
| **Actionable Insights** | Every chart tells you WHAT TO DO |
| **Production Quality** | Professional design, robust code, real data |
| **Business-Focused** | Built for executives and strategists |
| **Self-Service** | No technical skills needed |
| **High-Volume Data** | 10,000+ titles via parallel API fetching |

---

## 📝 Version Information

| Field | Value |
|-------|-------|
| Current Version | 3.0 |
| Release Date | December 2024 |
| Status | Production Ready |
| Python Support | 3.8+ |

### Changelog (v3.0)

- **NEW:** LightGBM replaces Gradient Boosting for faster predictions
- **NEW:** XGBoost as automatic fallback
- **NEW:** Facebook Prophet for time series forecasting
- **NEW:** Parallel data fetching (64 workers) for 10,000+ titles
- **IMPROVED:** Isolation Forest with multi-dimensional anomaly detection
- **IMPROVED:** Spearman correlation for more robust relationships
- **IMPROVED:** Connection pooling for API performance

---

<div align="center">

**Built for content strategists who demand data-driven decisions** 🎬

</div>
