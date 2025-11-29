# 🎬 Netflix Content Intelligence Platform

## Complete Production Analytics Dashboard
**6 Dashboards | 28+ Charts | Advanced ML | Network Analysis**

---

## 🚀 Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Run Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📊 Dashboard Overview

### **Dashboard 1: Content Universe Overview** 🌍
- **Purpose:** Understand market landscape and content distribution
- **Charts:** 4+ (Genre bars, Popularity vs Quality scatter, Performance matrix, Poster grids)
- **Key Insights:** Market composition, quality-popularity dynamics, top performers
- **Use When:** Starting analysis, getting 30,000-foot view

### **Dashboard 2: Performance Deep Dive** 📊
- **Purpose:** Analyze what drives content success
- **Charts:** 6 (Anomaly detection, Correlation matrix, Seasonal patterns, Engagement analysis)
- **Key Insights:** Success factors, outliers, seasonal strategies, engagement drivers
- **Use When:** Understanding WHY content succeeds/fails

### **Dashboard 3: Market Opportunity Intelligence** 🎯
- **Purpose:** Identify gaps, saturation, and opportunities
- **Charts:** 5 (Saturation index, Pareto chart, Network graph, Release heatmap, Performance bands)
- **Key Insights:** GREEN zones (opportunities), RED zones (oversaturation), optimal timing
- **Use When:** Deciding WHERE to invest resources

### **Dashboard 4: Recommendation & Risk Copilot** 💡
- **Purpose:** ML-powered predictions and risk assessment
- **Charts:** 4+ (Budget forecast, DNA radar, Benchmarks, Similar titles)
- **Key Insights:** Predicted performance, hit probability, risk levels, recommendations
- **Use When:** Validating specific investment decisions

### **Dashboard 5: Predictive Forecasting** 🔮
- **Purpose:** Future trends and emerging patterns
- **Charts:** 5 (12-month forecasts, Seasonal analysis, Lifecycle curves, Rising stars, Momentum)
- **Key Insights:** Growth trajectories, declining trends, viral content
- **Use When:** Strategic planning, pipeline development

### **Dashboard 6: Head-to-Head Comparison** ⚖️
- **Purpose:** Direct side-by-side analysis
- **Charts:** 4+ (Metrics table, Dual radar, Trend comparison, Top performers)
- **Key Insights:** Winner determination, strengths/weaknesses comparison
- **Use When:** Final decision between 2 alternatives

---

## 🤖 Machine Learning Models

### **1. Gradient Boosting Regressor**
- **Use:** Popularity prediction in Dashboard 4
- **Parameters:** 100 estimators, learning rate 0.1, max depth 3
- **Accuracy:** Trained on genre-specific data for personalized predictions

### **2. Ridge Regression**
- **Use:** Time-series forecasting in Dashboard 5
- **Parameters:** Alpha 1.0 for stability
- **Accuracy:** 12-month genre trend predictions

### **3. Z-Score Anomaly Detection**
- **Use:** Outlier identification in Dashboard 2
- **Method:** Statistical analysis (>2 standard deviations)
- **Purpose:** Find surprise hits and cult classics

### **4. NetworkX Graph Analysis**
- **Use:** Genre co-occurrence in Dashboard 3
- **Method:** Spring layout algorithm
- **Purpose:** Identify winning genre combinations

---

## 🎨 Design Features

✅ **Netflix-inspired dark theme** (#0A0A0A background)
✅ **Genre color coding** (consistent across all dashboards)
✅ **Red accent system** (active states, winners, highlights)
✅ **Gradient effects** (buttons, cards, badges)
✅ **Interactive hover states** (posters, charts)
✅ **Responsive layouts** (3x4 grids, 2-column charts)
✅ **Professional insights** (every chart has analysis)

---

## 🔧 Interactive Features

### Global Filters (Sidebar)
- **Genre Multiselect:** Filter by one or multiple genres
- **Content Type:** Movies, TV Shows, or All
- **Year Range:** Dynamic slider (2000-2025)

### Dashboard-Specific Controls
- **Dashboard 1:** Movie/TV tabs
- **Dashboard 4:** Genre, Type, Budget, Quarter inputs
- **Dashboard 6:** Genre vs Genre OR Title vs Title modes

---

## 📈 Complete Analytical Flow

**The Journey:**
1. **Content Universe** → What exists in the market?
2. **Performance Deep Dive** → What drives success?
3. **Market Opportunities** → Where are the gaps?
4. **Recommendation Copilot** → Should we invest in X?
5. **Predictive Forecasting** → What's coming next?
6. **Head-to-Head Comparison** → Final decision: A or B?

**Analyst Conclusion:**
> "Based on 6 dashboards of analysis, invest in [Genre X] with [Budget Y] releasing in [Quarter Z]. Expected popularity: [Score]. Risk: [Level]. Data confidence: High."

---

## 📝 Key Innovations

✅ **Real TMDB data** (800+ titles, NO synthetic data)
✅ **Complete descriptions** (every chart has analysis text)
✅ **ML-powered** (3 algorithms for predictions)
✅ **Network analysis** (genre relationships)
✅ **Anomaly detection** (statistical outliers)
✅ **Risk assessment** (Low/Medium/High with badges)
✅ **Winner determination** (auto-calculated in comparisons)
✅ **Professional insights** (actionable recommendations)

---

## 💡 Usage Tips

### For Executives:
- Start with Dashboard 1 (big picture)
- Jump to Dashboard 6 for quick A/B decisions
- Use Dashboard 4 for investment validation

### For Analysts:
- Follow the complete 1→2→3→4→5→6 flow
- Study chart descriptions for methodology
- Export insights for presentations

### For Data Scientists:
- Examine ML model parameters in code
- Customize prediction algorithms
- Add your own features

---

## 🛠 Technical Details

- **Total Lines:** 1,384
- **Total Charts:** 28+
- **Data Source:** TMDB API (real-time)
- **Cache Duration:** 1 hour (optimized performance)
- **Frameworks:** Streamlit, Plotly, scikit-learn
- **Python Version:** 3.8+

---

## 📂 Project Structure

```
netflix-intelligence-platform/
├── app.py                    # Main application (1,384 lines)
├── requirements.txt          # Dependencies
├── .streamlit/
│   └── config.toml          # Theme configuration
└── README.md                # This file
```

---

## 🎬 You're All Set!

Run `streamlit run app.py` and start analyzing!

**Questions?** All chart descriptions are built into the app for guidance.

---

**Built with ❤️ for Netflix Content Strategy**
