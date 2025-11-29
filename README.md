# Netflix Content Intelligence Platform

## 🎯 Project Overview

The Netflix Content Intelligence Platform is a comprehensive, data-driven analytics dashboard designed for entertainment industry professionals, content strategists, and business decision-makers. This application transforms raw entertainment data into strategic insights through advanced visualizations, statistical analysis, and machine learning predictions.

Built as a complete decision-support system, it enables users to explore market landscapes, identify opportunities, predict performance, and validate investment decisions—all backed by real data from The Movie Database (TMDB) covering over 800 titles across movies and TV shows.

---

## 📊 What This Platform Does

### **The Complete Analytical Journey**

This platform guides you through six strategic stages of content analysis:

1. **EXPLORE** → What content exists in the market? (Dashboard 1: Content Universe)
2. **UNDERSTAND** → What patterns drive success? (Dashboard 2: Performance Deep Dive)
3. **IDENTIFY** → Where are the opportunities? (Dashboard 3: Market Opportunities)
4. **PREDICT** → Should I invest in this? (Dashboard 4: Recommendation Copilot)
5. **FORECAST** → What will happen next? (Dashboard 5: Predictive Forecasting)
6. **DECIDE** → Which option is better? (Dashboard 6: Head-to-Head Comparison)

Each dashboard builds on the previous one, creating a logical flow from market exploration to final investment decisions.

---

## 🚀 Key Features & Capabilities

### **Six Intelligence Dashboards**

#### **1. Content Universe** (Market Landscape)
- **Purpose**: Get baseline understanding of the content market
- **Key Insights**: Genre distribution, quality vs popularity patterns, top performers
- **Business Use**: Market composition analysis, competitive benchmarking
- **Charts**: 6+ visualizations including genre bars, scatter plots, performance matrices, poster grids
- **Special Feature**: Shows ALL content types (Movies + TV combined) for complete market view

#### **2. Performance Deep Dive** (Statistical Analysis)
- **Purpose**: Identify what metrics and patterns drive content success
- **Key Insights**: Correlation analysis, anomaly detection, seasonal patterns, engagement drivers
- **Business Use**: Success factor identification, content strategy optimization
- **Charts**: 6+ visualizations including correlation heatmaps, Z-score anomaly scatter, monthly trends
- **Special Feature**: Statistical outlier detection using 2-sigma threshold to find breakout hits

#### **3. Market Opportunities** (Strategic Intelligence)
- **Purpose**: Find underserved market segments with high potential
- **Key Insights**: Market saturation analysis, 80/20 distribution, genre combinations, optimal release timing
- **Business Use**: Portfolio gap analysis, competitive positioning, launch planning
- **Charts**: 5+ visualizations including bubble charts (GREEN/RED zones), Pareto analysis, network graphs
- **Special Feature**: Genre co-occurrence network showing which genres succeed together

#### **4. Recommendation Copilot** (ML-Powered Advisor)
- **Purpose**: Get quantitative predictions for specific content investments
- **Key Insights**: Popularity forecasts, budget impact curves, risk assessment, similar title benchmarks
- **Business Use**: Investment validation, greenlight decisions, risk evaluation
- **Interactive Controls**: Genre selector, content type, budget slider (1-10), release quarter
- **Machine Learning**: Gradient Boosting Regressor predicts expected popularity score
- **Charts**: 4+ visualizations including forecast curves, radar profiles, benchmark bars
- **Special Feature**: Outputs comprehensive recommendation with hit probability and risk level

#### **5. Predictive Forecasting** (Future Trends)
- **Purpose**: Anticipate market conditions 6-12 months ahead
- **Key Insights**: Genre trend forecasts, seasonal patterns, momentum tracking, lifecycle analysis
- **Business Use**: Strategic planning, portfolio rebalancing, timing optimization
- **Machine Learning**: Ridge Regression models predict 12-month trends for top 6 genres
- **Charts**: 5+ visualizations including multi-line forecasts, seasonal bars, velocity rankings
- **Special Feature**: Rising stars analysis identifying viral content by engagement velocity

#### **6. Head-to-Head Comparison** (Final Decision Tool)
- **Purpose**: Direct comparison between two options to make final choice
- **Comparison Modes**: Genre vs Genre OR Title vs Title
- **Key Insights**: Side-by-side metrics, winner identification, historical trends, performance deltas
- **Business Use**: Final greenlight decisions, A/B investment choices, competitive analysis
- **Charts**: 4+ visualizations including metrics tables, diverging bars, trend lines, top titles grids
- **Special Feature**: Auto-calculated winner with score based on metrics won

---

## 🤖 Machine Learning & Advanced Analytics

### **Three Production ML Models**

1. **Gradient Boosting Regressor** (Popularity Prediction)
   - **Algorithm**: Ensemble decision trees with boosting
   - **Parameters**: 100 estimators, 0.1 learning rate, max depth 3
   - **Training Data**: Genre, rating, vote count from filtered dataset
   - **Output**: Predicted popularity score (0-100 scale)
   - **Use Case**: Dashboard 4 - Investment recommendations
   - **Accuracy**: Trained per-genre for higher precision

2. **Ridge Regression** (Time Series Forecasting)
   - **Algorithm**: Linear regression with L2 regularization
   - **Parameters**: Alpha 1.0 for regularization strength
   - **Training Data**: Historical engagement scores with time index
   - **Output**: 12 future monthly predictions per genre
   - **Use Case**: Dashboard 5 - Trend forecasting
   - **Accuracy**: Non-negative predictions with trend smoothing

3. **Z-Score Anomaly Detection** (Outlier Identification)
   - **Algorithm**: Statistical deviation analysis
   - **Parameters**: 2-sigma threshold (98% confidence)
   - **Detection**: Absolute Z-score > 2 standard deviations
   - **Output**: Boolean flag for anomalous titles
   - **Use Case**: Dashboard 2 - Breakout hit identification
   - **Visualization**: Red dots on scatter plots

### **Advanced Analytical Techniques**

- **Network Analysis**: Genre co-occurrence using NetworkX graph theory
- **Pareto Analysis**: 80/20 rule visualization for content concentration
- **Correlation Matrices**: Pearson correlation for metric relationships
- **Seasonal Decomposition**: Monthly and quarterly pattern analysis
- **Engagement Scoring**: Custom formula combining popularity, votes, and ratings
- **Market Saturation Mapping**: Multi-dimensional bubble charts with opportunity zones

---

## 📈 Visualization Excellence

### **33+ Interactive Charts**

Every chart in the platform includes:
- **Chart Analysis Section**: Explains what the chart shows and how to read it
- **Insight Panels**: 3-4 actionable takeaways with highlighted key metrics
- **Interactive Features**: Hover details, drill-down capabilities, dynamic filtering
- **Professional Styling**: Netflix-inspired dark theme with color-coded genres

### **Chart Categories**

- **Distribution Charts**: Bar charts, histograms showing volume and spread
- **Correlation Charts**: Scatter plots, heatmaps revealing relationships
- **Trend Charts**: Line charts, area charts tracking changes over time
- **Comparison Charts**: Diverging bars, dual axes for head-to-head analysis
- **Network Charts**: Graph visualizations showing genre connections
- **Forecast Charts**: Predictive curves with confidence intervals
- **Performance Matrices**: Grid visualizations for release timing optimization

### **Color-Coded Genre System**

Consistent across all dashboards for instant pattern recognition:
- Drama: Purple (#8b5cf6)
- Action: Red (#ef4444)
- Comedy: Yellow (#fbbf24)
- Science Fiction: Blue (#3b82f6)
- Horror: Dark Red (#7f1d1d)
- Romance: Pink (#ec4899)
- Thriller: Dark Red (#991b1b)
- Animation: Green (#10b981)

---

## 💼 Business Value & Use Cases

### **For C-Suite Executives**

**Use the platform to:**
- Make data-driven greenlight decisions with ML predictions
- Identify portfolio gaps and rebalancing opportunities
- Understand competitive positioning across genres
- Evaluate ROI potential before content acquisition

**Typical Workflow**: Dashboard 1 (market overview) → Dashboard 3 (opportunities) → Dashboard 4 (investment prediction) → Dashboard 6 (final comparison)

### **For Content Strategists**

**Use the platform to:**
- Optimize release calendars by genre-specific windows
- Track emerging trends and momentum shifts
- Benchmark performance against top titles
- Plan content mix for maximum engagement

**Typical Workflow**: Dashboard 2 (performance patterns) → Dashboard 3 (release timing) → Dashboard 5 (trend forecasting)

### **For Data Analysts**

**Use the platform to:**
- Explore statistical relationships and correlations
- Validate hypotheses with anomaly detection
- Extract insights for presentation decks
- Build custom analysis using interactive filters

**Typical Workflow**: All dashboards with deep filtering and cross-referencing

### **Real-World Scenarios**

**Scenario 1: New Content Acquisition**
- Question: Should we acquire this sci-fi film for $50M?
- Dashboard 3: Check sci-fi market saturation → GREEN zone (opportunity)
- Dashboard 5: Review 12-month forecast → +25% growth projected
- Dashboard 4: Input profile → Predicted popularity: 78, Hit probability: 68%
- Dashboard 6: Compare sci-fi vs alternatives → Sci-fi wins on 5/7 metrics
- Decision: GREENLIGHT with medium risk, strong upside

**Scenario 2: Release Calendar Planning**
- Question: When should we release our Q4 slate?
- Dashboard 3: Review release window heatmap → Drama peaks Nov-Dec, Action peaks June-Aug
- Dashboard 2: Analyze seasonality → December +30% above average
- Dashboard 5: Check seasonal bars → Q4 consistently strong for drama
- Decision: Drama titles in November, hold action for summer

**Scenario 3: Portfolio Health Check**
- Question: Is our content mix balanced?
- Dashboard 1: Current distribution → 40% Drama, 25% Action, 15% Comedy (top 3 = 80%)
- Dashboard 3: Market opportunities → Sci-fi is GREEN zone (underserved)
- Dashboard 5: Future projections → Sci-fi +25%, Drama -5%, Action flat
- Decision: Increase sci-fi allocation, reduce drama development

---

## 🛠️ Technical Architecture

### **Technology Stack**

- **Framework**: Streamlit 1.28+ (Python web framework)
- **Data Processing**: Pandas 2.0+, NumPy 1.24+
- **Visualizations**: Plotly 5.14+ (interactive JavaScript charts)
- **Machine Learning**: scikit-learn 1.3+ (Gradient Boosting, Ridge Regression)
- **Statistical Analysis**: SciPy 1.10+ (Z-score, correlations)
- **Network Analysis**: NetworkX 3.0+ (genre graphs)
- **Data Source**: The Movie Database (TMDB) public API
- **Styling**: Custom CSS with Netflix theme colors

### **Data Pipeline**

1. **Data Fetch**: TMDB API calls for movies and TV shows (top 800 titles)
2. **Data Enrichment**: Calculate engagement scores, extract genres, parse dates
3. **Feature Engineering**: Create time-based features, normalize metrics, detect anomalies
4. **Caching**: 1-hour cache for API results and computed metrics
5. **Filtering**: Real-time filter application across genre, content type, year range
6. **Visualization**: Dynamic chart generation with Plotly
7. **ML Inference**: On-demand predictions based on user inputs

### **Performance Optimization**

- First load: 5-10 seconds (includes API fetch)
- Subsequent navigation: <1 second (cached data)
- Filter updates: <0.5 seconds (in-memory operations)
- Chart rendering: Progressive loading for smooth UX
- Memory usage: ~200MB for full dataset
- Concurrent users: Designed for single-user analysis sessions

### **Code Structure**

- **Total Lines**: 1,472 lines of Python
- **Functions**: 15+ modular functions for each dashboard
- **Helper Functions**: Color mapping, insight panels, poster grids, filtering
- **Global Configurations**: Colors, page config, theme styling
- **ML Models**: Inline training with parameter tuning
- **Error Handling**: Graceful fallbacks for missing data

---

## 📦 Installation & Setup

### **System Requirements**

- Python 3.8 or higher
- 4GB RAM minimum
- Internet connection (for TMDB API access)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### **Quick Start (3 Steps)**

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
streamlit run app.py

# 3. Open browser
# Automatically opens at http://localhost:8501
```

### **Dependencies**

All required packages with minimum versions:
```
streamlit >= 1.28.0      # Web framework
pandas >= 2.0.0          # Data manipulation
numpy >= 1.24.0          # Numerical computing
plotly >= 5.14.0         # Interactive charts
requests >= 2.31.0       # API calls
scikit-learn >= 1.3.0    # Machine learning
scipy >= 1.10.0          # Statistical functions
networkx >= 3.0          # Graph analysis
python-dateutil >= 2.8.0 # Date parsing
```

---

## 🎨 Design Philosophy

### **Netflix-Inspired Professional Theme**

- **Pure Black Background** (#0A0A0A): Reduces eye strain, premium feel
- **Netflix Red Accents** (#E50914): Primary actions, highlights, winners
- **Dark Card Backgrounds** (#1A1A1A): Content separation, depth
- **Professional Gradients**: Subtle depth without distraction
- **White Text** (#FFFFFF): Maximum readability

### **User Experience Principles**

1. **Progressive Disclosure**: Simple overview → detailed analysis
2. **Minimal Clicks**: Key insights accessible in 1-2 clicks
3. **Consistent Navigation**: Same pattern across all dashboards
4. **Explanatory Text**: Every chart has "how to read this" guidance
5. **Actionable Insights**: Not just data, but what to DO with it
6. **Visual Hierarchy**: Size, color, position guide attention
7. **Responsive Design**: Works on different screen sizes

---

## 🔧 Customization Options

### **Modify Theme Colors**

Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#E50914"              # Change accent color
backgroundColor = "#0A0A0A"            # Change page background
secondaryBackgroundColor = "#1A1A1A"  # Change card backgrounds
textColor = "#FFFFFF"                 # Change text color
```

### **Adjust ML Model Parameters**

In app.py, find the model definitions:
```python
# Gradient Boosting (Dashboard 4)
GradientBoostingRegressor(
    n_estimators=100,      # Increase for more trees
    learning_rate=0.1,     # Lower for slower, more precise learning
    max_depth=3,           # Increase for more complex patterns
    random_state=42
)

# Ridge Regression (Dashboard 5)
Ridge(alpha=1.0)           # Increase alpha for more regularization
```

### **Add More Charts**

Template for new visualizations:
```python
st.subheader("Your Chart Title")
st.markdown("**Chart Analysis:** Explain what this shows...")

# Create your chart
fig = go.Figure(...)
st.plotly_chart(fig, width="stretch")

# Add insights
create_insight_panel("Key Insights", [
    "First insight with <span class='insight-highlight'>highlights</span>",
    "Second actionable recommendation",
    "Third strategic guidance"
])
```

---

## ❓ Troubleshooting

### **Common Issues & Solutions**

**Issue**: Charts not displaying  
**Solution**: `pip install --upgrade plotly streamlit`

**Issue**: Slow first load  
**Solution**: Normal - fetching 800+ titles from TMDB API (5-10 seconds)

**Issue**: Import errors  
**Solution**: `pip install -r requirements.txt --upgrade`

**Issue**: Port 8501 already in use  
**Solution**: `streamlit run app.py --server.port 8502`

**Issue**: No data showing  
**Solution**: Check internet connection (TMDB API requires connectivity)

---

## 📊 Project Statistics

- **Total Dashboards**: 6 specialized intelligence views
- **Total Charts**: 33+ interactive visualizations
- **ML Models**: 3 production-ready algorithms
- **Data Points**: 800+ titles analyzed
- **Genres Covered**: 18 major entertainment categories
- **Code Lines**: 1,472 lines of Python
- **Functions**: 15+ modular components
- **Years of Data**: 2018-2024 (7 years historical)
- **Metrics Tracked**: 15+ performance indicators
- **Visualizations Types**: 10+ chart categories

---

## 🎯 What Makes This Platform Unique

1. **Complete Journey**: Not just charts - a full decision-making workflow
2. **ML-Powered**: Real predictions, not just historical analysis
3. **Actionable Insights**: Every chart tells you WHAT TO DO
4. **Production Quality**: Professional design, robust code, real data
5. **Business-Focused**: Built for executives and strategists, not just analysts
6. **Strategic Flow**: Dashboards build on each other logically
7. **Self-Service**: No technical skills needed to extract insights
8. **Industry-Specific**: Designed specifically for content/entertainment decisions

---

## 📝 Version Information

**Current Version**: 2.0  
**Release Date**: November 2024  
**Status**: Production Ready  
**Maintenance**: Active  

---

## 🙏 Credits & Attribution

**Data Source**: This product uses the TMDB API but is not endorsed or certified by TMDB.

**Built With**: Streamlit, Plotly, scikit-learn, NetworkX, Pandas, NumPy, SciPy

---

## 📄 License

This project is provided as-is for analytical and educational purposes.  
TMDB data usage subject to TMDB terms of service.

---

**Built for content strategists who demand data-driven decisions** 🎬
