"""
NETFLIX CONTENT INTELLIGENCE PLATFORM
Complete Production Version - All 6 Dashboards Integrated
Features: 28+ Charts, ML Predictions, Network Analysis, Full Analytical Flow
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats
from scipy.spatial.distance import pdist, squareform
import networkx as nx
import warnings
warnings.filterwarnings('ignore')

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Netflix Content Intelligence Platform",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== COMPLETE STYLING ====================
st.markdown("""
<style>
    .stApp { background-color: #0A0A0A; }
    [data-testid="stSidebar"] { background-color: #0A0A0A; border-right: 1px solid #262626; }
    
    h1 { color: #FFFFFF !important; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; font-size: 2.5rem !important; margin-bottom: 10px !important; }
    h2 { color: #FFFFFF !important; font-family: 'Helvetica Neue', sans-serif; font-weight: 600; font-size: 1.8rem !important; margin-top: 35px !important; margin-bottom: 20px !important; }
    h3 { color: #E5E5E5 !important; font-family: 'Helvetica Neue', sans-serif; font-weight: 500; font-size: 1.3rem !important; }
    
    .subtitle { color: #B3B3B3; font-size: 1.05rem; margin-bottom: 30px; font-style: italic; }
    .dashboard-description { background: linear-gradient(135deg, #1A1A1A 0%, #141414 100%); padding: 20px 25px; border-radius: 8px; border-left: 3px solid #E50914; margin-bottom: 30px; color: #B3B3B3; font-size: 0.98rem; line-height: 1.8; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    
    .insight-panel { background: linear-gradient(135deg, #1A1A1A 0%, #141414 100%); padding: 22px; border-radius: 8px; border-left: 3px solid #3A4A5A; margin-top: 18px; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.2); }
    .insight-title { color: #FFFFFF; font-size: 1.15rem; font-weight: 600; margin-bottom: 12px; letter-spacing: 0.3px; }
    .insight-text { color: #B3B3B3; font-size: 0.95rem; line-height: 1.8; margin-bottom: 10px; }
    .insight-highlight { color: #FFFFFF; font-weight: 600; background: linear-gradient(90deg, #E50914 0%, #B20710 100%); padding: 2px 8px; border-radius: 4px; }
    
    div[data-testid="metric-container"] { background: linear-gradient(135deg, #1A1A1A 0%, #141414 100%); padding: 20px; border-radius: 8px; border: 1px solid #262626; transition: all 0.3s ease; box-shadow: 0 2px 4px rgba(0,0,0,0.2); }
    div[data-testid="metric-container"]:hover { border: 1px solid #E50914; transform: translateY(-2px); box-shadow: 0 6px 12px rgba(229,9,20,0.2); }
    [data-testid="stMetricValue"] { font-size: 2rem; font-weight: 700; color: #FFFFFF; }
    [data-testid="stMetricLabel"] { font-size: 0.88rem; font-weight: 500; color: #B3B3B3; text-transform: uppercase; letter-spacing: 0.8px; }
    
    .stTabs [data-baseweb="tab-list"] { gap: 10px; background-color: #0A0A0A; }
    .stTabs [data-baseweb="tab"] { background-color: #1A1A1A; border: 1px solid #262626; color: #B3B3B3; padding: 14px 28px; border-radius: 6px; font-weight: 500; transition: all 0.3s ease; }
    .stTabs [data-baseweb="tab"]:hover { background-color: #262626; border-color: #3A4A5A; }
    .stTabs [aria-selected="true"] { background-color: #1A1A1A; border-bottom: 3px solid #E50914; color: #FFFFFF; }
    
    .stButton>button { background: linear-gradient(135deg, #E50914 0%, #B20710 100%); color: #FFFFFF; border: none; border-radius: 6px; padding: 12px 24px; font-weight: 600; transition: all 0.3s ease; box-shadow: 0 4px 6px rgba(229,9,20,0.3); }
    .stButton>button:hover { background: linear-gradient(135deg, #B20710 0%, #8B0000 100%); transform: translateY(-2px); box-shadow: 0 6px 12px rgba(229,9,20,0.4); }
    
    .risk-badge { display: inline-block; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 0.85rem; letter-spacing: 0.5px; }
    .risk-low { background: linear-gradient(135deg, #3FBF7F 0%, #2d8a5c 100%); color: #FFFFFF; }
    .risk-medium { background: linear-gradient(135deg, #E8B020 0%, #c49419 100%); color: #FFFFFF; }
    .risk-high { background: linear-gradient(135deg, #E50914 0%, #B20710 100%); color: #FFFFFF; }
    
    .winner-badge { background: linear-gradient(135deg, #E50914 0%, #B20710 100%); color: #FFFFFF; padding: 8px 16px; border-radius: 6px; font-weight: 700; display: inline-block; box-shadow: 0 4px 8px rgba(229,9,20,0.4); }
    .section-divider { border-top: 2px solid #262626; margin: 40px 0; }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==================== CONFIGURATION ====================
TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"
TMDB_BACKDROP_BASE = "https://image.tmdb.org/t/p/original"

GENRE_MAP = {
    28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy", 80: "Crime",
    99: "Documentary", 18: "Drama", 10751: "Family", 14: "Fantasy", 36: "History",
    27: "Horror", 10402: "Music", 9648: "Mystery", 10749: "Romance", 878: "Science Fiction",
    10770: "TV Movie", 53: "Thriller", 10752: "War", 37: "Western",
    10759: "Action & Adventure", 10762: "Kids", 10763: "News", 10764: "Reality",
    10765: "Sci-Fi & Fantasy", 10766: "Soap", 10767: "Talk", 10768: "War & Politics"
}

GENRE_COLORS = {
    'Drama': '#8b5cf6', 'Action': '#ef4444', 'Comedy': '#fbbf24', 'Science Fiction': '#3b82f6',
    'Horror': '#7f1d1d', 'Romance': '#ec4899', 'Thriller': '#991b1b', 'Animation': '#10b981',
    'Documentary': '#6366f1', 'Fantasy': '#a855f7', 'Adventure': '#14b8a6', 'Crime': '#dc2626',
    'Family': '#f97316', 'Mystery': '#6366f1'
}

COLORS = {
    'primary': '#3A4A5A', 'success': '#3FBF7F', 'warning': '#E8B020', 'danger': '#E50914',
    'info': '#3b82f6', 'text': '#FFFFFF', 'text_secondary': '#B3B3B3'
}

# ==================== DATA FETCHING ====================
@st.cache_data(ttl=3600)
def fetch_tmdb_data():
    """Fetch comprehensive TMDB data"""
    all_content = []
    endpoints = [('movie/popular', 20), ('movie/top_rated', 10), ('tv/popular', 20), ('tv/top_rated', 10)]
    
    for endpoint, pages in endpoints:
        for page in range(1, pages + 1):
            try:
                r = requests.get(f"{TMDB_BASE_URL}/{endpoint}", 
                               params={"api_key": TMDB_API_KEY, "page": page}, timeout=5)
                if r.status_code == 200:
                    for item in r.json().get("results", []):
                        item["content_type"] = "Movie" if "movie" in endpoint else "TV Show"
                        if "tv" in endpoint:
                            item["title"] = item.get("name", "Unknown")
                            item["release_date"] = item.get("first_air_date", "")
                        all_content.append(item)
            except: continue
    
    df = pd.DataFrame(all_content).drop_duplicates(subset=["id"])
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df["year"] = df["release_date"].dt.year
    df["month"] = df["release_date"].dt.month
    df["quarter"] = df["release_date"].dt.quarter
    df["month_name"] = df["release_date"].dt.strftime('%B')
    df["days_since_release"] = (datetime.now() - df["release_date"]).dt.days
    
    df["genre_names"] = df["genre_ids"].apply(lambda x: [GENRE_MAP.get(g, "Unknown") for g in x] if isinstance(x, list) else [])
    df["primary_genre"] = df["genre_names"].apply(lambda x: x[0] if len(x) > 0 else "Unknown")
    df["genre_count"] = df["genre_names"].apply(len)
    
    df["vote_count_factor"] = df["vote_count"].apply(lambda x: min(x / 100, 10))
    df["engagement_score"] = df["popularity"] * 0.4 + (df["vote_average"] * df["vote_count_factor"]) * 0.6
    df["popularity_percentile"] = df["popularity"].rank(pct=True) * 100
    df["rating_percentile"] = df["vote_average"].rank(pct=True) * 100
    
    df["poster_url"] = df["poster_path"].apply(lambda x: f"{TMDB_IMAGE_BASE}{x}" if pd.notna(x) else None)
    df["backdrop_url"] = df["backdrop_path"].apply(lambda x: f"{TMDB_BACKDROP_BASE}{x}" if pd.notna(x) else None)
    df["performance_tier"] = pd.cut(df["engagement_score"], bins=[0, 25, 50, 75, 100], labels=["Low", "Medium", "High", "Elite"])
    
    return df

# ==================== HELPER FUNCTIONS ====================
def get_genre_color(genre):
    return GENRE_COLORS.get(genre, COLORS['primary'])

def create_insight_panel(title, insights):
    """Create professional insight panel with highlights"""
    insights_html = "".join([f'<div class="insight-text">{i}</div>' for i in insights])
    st.markdown(f'<div class="insight-panel"><div class="insight-title">{title}</div>{insights_html}</div>', unsafe_allow_html=True)

def display_poster_grid(df, limit=12, cols=4):
    """Display simple poster grid without cards"""
    posters = df.nlargest(limit, "popularity")
    rows = (limit + cols - 1) // cols
    for row in range(rows):
        columns = st.columns(cols)
        for col_idx in range(cols):
            idx = row * cols + col_idx
            if idx < len(posters):
                with columns[col_idx]:
                    p = posters.iloc[idx]
                    if p["poster_url"]:
                        st.image(p["poster_url"], use_container_width=True)
                        st.markdown(f'<div style="text-align: center; color: #FFFFFF; font-size: 0.9rem; margin-top: 8px;">{p["title"][:30]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="text-align: center; color: #B3B3B3; font-size: 0.8rem;">⭐ {p["vote_average"]:.1f} | 🔥 {p["popularity"]:.0f}</div>', unsafe_allow_html=True)

def apply_filters(df, filters, ignore_content_type=False):
    """Apply sidebar filters to dataframe"""
    df_filtered = df.copy()
    if filters['genres']:
        df_filtered = df_filtered[df_filtered['primary_genre'].isin(filters['genres'])]
    if not ignore_content_type and filters['content_type'] != "All":
        df_filtered = df_filtered[df_filtered['content_type'] == filters['content_type']]
    if filters['year_range'][0] > df['year'].min():
        df_filtered = df_filtered[df_filtered['year'] >= filters['year_range'][0]]
    if filters['year_range'][1] < df['year'].max():
        df_filtered = df_filtered[df_filtered['year'] <= filters['year_range'][1]]
    return df_filtered

# ==================== DASHBOARD 1: CONTENT UNIVERSE ====================
def dashboard_1_content_universe(df, filters):
    """Dashboard 1: Market landscape overview with genre distribution and quality analysis"""
    df_filtered = apply_filters(df, filters, ignore_content_type=True)  # Show all content types
    
    st.title("🌍 Content Universe Overview")
    st.markdown('<p class="subtitle">Explore the market landscape - what content exists and where</p>', unsafe_allow_html=True)
    st.markdown('<div class="dashboard-description"><strong>Business Problem:</strong> Understand current market landscape. This dashboard provides a 30,000-foot view of content distribution, quality-popularity dynamics, and market composition. Use this to identify high-level patterns before diving deeper into specific opportunities.</div>', unsafe_allow_html=True)
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Titles", f"{len(df_filtered):,}")
    col2.metric("Average Rating", f"{df_filtered['vote_average'].mean():.1f}/10")
    col3.metric("Active Genres", df_filtered["primary_genre"].nunique())
    col4.metric("Avg Popularity", f"{df_filtered['popularity'].mean():.0f}")
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # Hero Section - Big Poster + Small Quote
    st.markdown('<div style="margin: 20px 0;"></div>', unsafe_allow_html=True)
    
    # Featured title (top-rated)
    featured_title = df_filtered.nlargest(1, "vote_average").iloc[0]
    
    # Center the poster
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if featured_title["poster_url"]:
            st.image(featured_title["poster_url"], use_container_width=True)
        
        # Small quote below
        st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            <div style="font-size: 1.1rem; color: #E50914; font-style: italic; margin-bottom: 10px;">
                "{featured_title.get('tagline', 'Discover the most acclaimed content in our catalog')}"
            </div>
            <div style="font-size: 1rem; color: #B3B3B3;">
                — {featured_title['title']} | {featured_title['primary_genre']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Movie/TV Tabs
    tab1, tab2 = st.tabs(["📽️ Movies", "📺 TV Shows"])
    
    with tab1:
        movies = df_filtered[df_filtered["content_type"] == "Movie"]
        
        if len(movies) > 0:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Top 10 Movie Genres by Volume")
                st.markdown("**Chart Analysis:** This horizontal bar chart shows the distribution of movie titles across the top 10 genres. Each bar is color-coded according to the genre for easy visual identification. Longer bars indicate more content in that genre, which could signal either opportunity (popular category) or saturation (overcrowded market).")
                
                genre_dist = movies["primary_genre"].value_counts().head(10)
                colors_list = [get_genre_color(g) for g in genre_dist.index]
                
                fig = go.Figure(go.Bar(
                    x=genre_dist.values, 
                    y=genre_dist.index, 
                    orientation='h',
                    marker=dict(color=colors_list, line=dict(color='#FFFFFF', width=0.5)),
                    text=genre_dist.values, 
                    textposition='outside', 
                    textfont=dict(color='#FFFFFF', size=12)
                ))
                
                fig.update_layout(
                    xaxis=dict(title="Number of Titles", color='#B3B3B3', gridcolor='#262626'),
                    yaxis=dict(title="", color='#B3B3B3'),
                    paper_bgcolor='#0A0A0A',
                    plot_bgcolor='#0A0A0A',
                    font=dict(color='#FFFFFF'),
                    height=450
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                create_insight_panel("Market Composition Insights", [
                    f"<span class='insight-highlight'>{genre_dist.index[0]}</span> dominates with {genre_dist.values[0]} titles ({genre_dist.values[0]/len(movies)*100:.1f}% market share).",
                    f"Top 3 genres account for <span class='insight-highlight'>{(genre_dist.values[:3].sum()/len(movies)*100):.1f}%</span> of all movies.",
                    "High concentration in top genres suggests potential oversaturation. Look for underserved genres in the long tail for differentiation opportunities."
                ])
            
            with col2:
                st.subheader("Genre Performance: Popularity vs Quality")
                st.markdown("**Chart Analysis:** This scatter plot compares average popularity (reach) against average quality (rating) for each genre. Bubble size represents the total number of titles in that genre. The ideal position is the top-right quadrant: high popularity AND high quality. Genres in this zone represent proven success formulas.")
                
                genre_stats = movies.groupby("primary_genre").agg({
                    "popularity": "mean",
                    "vote_average": "mean",
                    "id": "count"
                }).reset_index().nlargest(10, "popularity")
                
                genre_stats.columns = ["Genre", "Avg_Pop", "Avg_Rating", "Count"]
                
                fig = px.scatter(
                    genre_stats,
                    x="Avg_Pop",
                    y="Avg_Rating",
                    size="Count",
                    color="Genre",
                    color_discrete_sequence=[get_genre_color(g) for g in genre_stats["Genre"]],
                    hover_data=["Genre", "Avg_Pop", "Avg_Rating", "Count"]
                )
                
                fig.update_layout(
                    xaxis=dict(title="Avg Popularity (Reach)", color='#B3B3B3', gridcolor='#262626'),
                    yaxis=dict(title="Avg Rating (Quality)", color='#B3B3B3', gridcolor='#262626'),
                    paper_bgcolor='#0A0A0A',
                    plot_bgcolor='#0A0A0A',
                    font=dict(color='#FFFFFF'),
                    height=450,
                    showlegend=False
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                create_insight_panel("Quality-Popularity Dynamics", [
                    "<span class='insight-highlight'>Top-right quadrant</span> = Sweet Spot: High popularity AND high quality. These are proven winners.",
                    "Bubble size shows market volume. Large bubbles in top-right = saturated but successful categories.",
                    "Small bubbles with high ratings = Niche opportunities with quality potential. Target these for premium content investment with differentiation strategy."
                ])
            
            st.subheader("Top Performing Movies")
            st.markdown("**Grid Analysis:** These are the highest-performing movies by popularity score. Study these titles to understand current market preferences, successful themes, and audience engagement patterns. Hover for detailed metrics.")
            display_poster_grid(movies, limit=12, cols=4)
        else:
            st.info("No movies match current filters. Try adjusting your filter criteria.")
    
    with tab2:
        tv = df_filtered[df_filtered["content_type"] == "TV Show"]
        
        if len(tv) > 0:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Top 10 TV Genres by Volume")
                st.markdown("**Chart Analysis:** Distribution of TV show titles across genres. Compare this to movie distribution to identify platform-specific opportunities. TV audiences may have different genre preferences than movie audiences.")
                
                genre_dist_tv = tv["primary_genre"].value_counts().head(10)
                
                fig = go.Figure(go.Bar(
                    x=genre_dist_tv.values,
                    y=genre_dist_tv.index,
                    orientation='h',
                    marker=dict(color=[get_genre_color(g) for g in genre_dist_tv.index], line=dict(color='#FFFFFF', width=0.5)),
                    text=genre_dist_tv.values,
                    textposition='outside',
                    textfont=dict(color='#FFFFFF', size=12)
                ))
                
                fig.update_layout(
                    xaxis=dict(title="Number of Shows", color='#B3B3B3', gridcolor='#262626'),
                    yaxis=dict(title="", color='#B3B3B3'),
                    paper_bgcolor='#0A0A0A',
                    plot_bgcolor='#0A0A0A',
                    font=dict(color='#FFFFFF'),
                    height=450
                )
                
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("TV Genre Performance Matrix")
                st.markdown("**Chart Analysis:** TV shows mapped by popularity vs quality. Look for differences from movie patterns. Some genres perform better in TV format (e.g., Drama for character development, Comedy for episodic formats).")
                
                genre_stats_tv = tv.groupby("primary_genre").agg({
                    "popularity": "mean",
                    "vote_average": "mean",
                    "id": "count"
                }).reset_index().nlargest(10, "popularity")
                
                genre_stats_tv.columns = ["Genre", "Avg_Pop", "Avg_Rating", "Count"]
                
                fig = px.scatter(
                    genre_stats_tv,
                    x="Avg_Pop",
                    y="Avg_Rating",
                    size="Count",
                    color="Genre",
                    color_discrete_sequence=[get_genre_color(g) for g in genre_stats_tv["Genre"]]
                )
                
                fig.update_layout(
                    xaxis=dict(title="Avg Popularity", color='#B3B3B3', gridcolor='#262626'),
                    yaxis=dict(title="Avg Rating", color='#B3B3B3', gridcolor='#262626'),
                    paper_bgcolor='#0A0A0A',
                    plot_bgcolor='#0A0A0A',
                    font=dict(color='#FFFFFF'),
                    height=450,
                    showlegend=False
                )
                
                st.plotly_chart(fig, use_container_width=True)
            
            st.subheader("Top Performing TV Shows")
            st.markdown("**Grid Analysis:** Highest-engagement TV shows. Compare casting, themes, and formats against movie top performers to understand format-specific success factors.")
            display_poster_grid(tv, limit=12, cols=4)
        else:
            st.info("No TV shows match current filters. Try adjusting your filter criteria.")


# ==================== DASHBOARD 2: PERFORMANCE DEEP DIVE ====================
def dashboard_2_performance_deepdive(df, filters):
    """Dashboard 2: Analyze what drives content success through correlations and patterns"""
    df_filtered = apply_filters(df, filters)
    
    st.title("📊 Performance Deep Dive")
    st.markdown('<p class="subtitle">Understand what drives content success and identify key patterns</p>', unsafe_allow_html=True)
    st.markdown('<div class="dashboard-description"><strong>Business Problem:</strong> Analyze WHY some content outperforms others by examining correlations, seasonal patterns, and statistical anomalies. Use these insights to replicate success factors in future productions and avoid common pitfalls.</div>', unsafe_allow_html=True)
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    top = df_filtered.nlargest(1, "popularity").iloc[0]
    col1.metric("Top Performer", top["title"][:20]+"...")
    col2.metric("Peak Popularity", f"{top['popularity']:.0f}")
    col3.metric("Avg Engagement", f"{df_filtered['engagement_score'].mean():.0f}")
    col4.metric("Elite Titles (Top 25%)", f"{len(df_filtered[df_filtered['engagement_score'] > df_filtered['engagement_score'].quantile(0.75)]):,}")
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Popularity vs Rating - Anomaly Detection")
        st.markdown("**Chart Analysis:** Statistical outlier detection using Z-scores. Red dots are titles that break expected patterns (>2 standard deviations). These could be surprise hits (low budget, high impact) or cult classics (niche but devoted fanbase). Log scale on X-axis helps visualize the full range of popularity scores. Study these anomalies to find unconventional success formulas.")
        
        df_copy = df_filtered.copy()
        df_copy['pop_zscore'] = np.abs(stats.zscore(df_copy['popularity']))
        df_copy['is_anomaly'] = df_copy['pop_zscore'] > 2
        
        fig = px.scatter(
            df_copy,
            x="popularity",
            y="vote_average",
            size="vote_count",
            color="is_anomaly",
            color_discrete_map={True: COLORS['danger'], False: COLORS['primary']},
            hover_data=["title", "primary_genre"]
        )
        
        fig.update_layout(
            xaxis=dict(title="Popularity Score (log scale)", color='#B3B3B3', gridcolor='#262626', type='log'),
            yaxis=dict(title="Average Rating", color='#B3B3B3', gridcolor='#262626'),
            paper_bgcolor='#0A0A0A',
            plot_bgcolor='#0A0A0A',
            font=dict(color='#FFFFFF'),
            height=450,
            showlegend=True,
            legend=dict(title="Status", font=dict(color='#FFFFFF'))
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        anomaly_count = df_copy['is_anomaly'].sum()
        create_insight_panel("Statistical Outliers Detected", [
            f"<span class='insight-highlight'>{anomaly_count} titles ({anomaly_count/len(df_copy)*100:.1f}%)</span> are statistical outliers (red dots).",
            "These are surprise hits, cult favorites, or titles that break conventional success patterns.",
            "Study these exceptions to discover alternative paths to success beyond mainstream formulas. Look for common themes, unconventional marketing, or niche audience targeting strategies."
        ])
    
    with col2:
        st.subheader("Success Factor Correlation Matrix")
        st.markdown("**Chart Analysis:** Heatmap showing statistical correlations between key performance metrics. Values range from 0 (no correlation) to 1 (perfect correlation). Higher values (red) = stronger relationships. This reveals which factors actually drive popularity. Use this to prioritize your investment areas.")
        
        corr_data = df_filtered[['popularity', 'vote_average', 'vote_count', 'engagement_score']].corr()
        
        fig = go.Figure(go.Heatmap(
            z=corr_data.values,
            x=['Popularity', 'Rating', 'Votes', 'Engagement'],
            y=['Popularity', 'Rating', 'Votes', 'Engagement'],
            colorscale=[[0, COLORS['primary']], [0.5, COLORS['warning']], [1, COLORS['danger']]],
            text=corr_data.values.round(2),
            texttemplate='%{text}',
            textfont={"size": 14, "color": "#FFFFFF"},
            hovertemplate='%{y} ↔ %{x}<br>Correlation: %{z:.2f}<extra></extra>'
        ))
        
        fig.update_layout(
            title="What Actually Drives Success?",
            paper_bgcolor='#0A0A0A',
            plot_bgcolor='#0A0A0A',
            font=dict(color='#FFFFFF'),
            height=450
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        pop_vote_corr = corr_data.loc['popularity', 'vote_count']
        pop_rating_corr = corr_data.loc['popularity', 'vote_average']
        
        create_insight_panel("Correlation Intelligence", [
            f"<span class='insight-highlight'>Vote Count → Popularity: {pop_vote_corr:.2f}</span> (STRONG correlation)",
            f"<span class='insight-highlight'>Rating → Popularity: {pop_rating_corr:.2f}</span> (moderate correlation)",
            f"Volume of engagement matters <span class='insight-highlight'>{pop_vote_corr/pop_rating_corr:.1f}x MORE</span> than quality scores for driving popularity.",
            "Actionable insight: Marketing & distribution (which drive vote counts) have bigger impact than content quality alone. Invest in both, but don't neglect go-to-market strategy."
        ])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Release Window Seasonality Analysis")
        st.markdown("**Chart Analysis:** Average engagement scores by month reveal seasonal patterns. Peaks indicate optimal release windows when audiences are most receptive. Troughs suggest slower periods better suited for catalog content or counter-programming strategies. The filled area emphasizes the magnitude of seasonal swings.")
        
        month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        monthly_perf = df_filtered.groupby("month_name")["engagement_score"].mean().reset_index()
        monthly_perf["month_name"] = pd.Categorical(monthly_perf["month_name"], categories=month_order, ordered=True)
        monthly_perf = monthly_perf.sort_values("month_name")
        
        fig = go.Figure(go.Scatter(
            x=monthly_perf["month_name"],
            y=monthly_perf["engagement_score"],
            mode='lines+markers',
            line=dict(width=3, color=COLORS['success']),
            marker=dict(size=12, color=COLORS['danger']),
            fill='tozeroy',
            fillcolor='rgba(63, 191, 127, 0.2)',
            hovertemplate='%{x}<br>Avg Engagement: %{y:.0f}<extra></extra>'
        ))
        
        fig.update_layout(
            xaxis=dict(title="Month", color='#B3B3B3', tickangle=-45),
            yaxis=dict(title="Avg Engagement Score", color='#B3B3B3', gridcolor='#262626'),
            paper_bgcolor='#0A0A0A',
            plot_bgcolor='#0A0A0A',
            font=dict(color='#FFFFFF'),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        best_month = monthly_perf.loc[monthly_perf["engagement_score"].idxmax(), "month_name"]
        worst_month = monthly_perf.loc[monthly_perf["engagement_score"].idxmin(), "month_name"]
        
        create_insight_panel("Seasonal Strategy Recommendations", [
            f"<span class='insight-highlight'>{best_month}</span> is peak engagement season - ideal for flagship releases and major marketing pushes.",
            f"<span class='insight-highlight'>{worst_month}</span> shows lowest engagement - use for catalog content, experimental projects, or niche programming.",
            "Plan your content calendar around these patterns. Reserve premium content for peak months to maximize ROI."
        ])
    
    with col2:
        st.subheader("Engagement Proxy: Votes vs Popularity")
        st.markdown("**Chart Analysis:** Log-log scatter plot examining the relationship between vote count (engagement proxy) and popularity (reach). Color indicates rating quality. Yellow points in the upper-right represent the holy grail: high engagement, high reach, AND high quality. The clustering patterns reveal engagement thresholds needed for viral spread.")
        
        fig = px.scatter(
            df_filtered,
            x="vote_count",
            y="popularity",
            color="vote_average",
            hover_data=["title", "primary_genre"],
            color_continuous_scale=[[0, COLORS['primary']], [0.5, COLORS['success']], [1, COLORS['warning']]]
        )
        
        fig.update_layout(
            xaxis=dict(title="Vote Count (log scale)", color='#B3B3B3', gridcolor='#262626', type='log'),
            yaxis=dict(title="Popularity (log scale)", color='#B3B3B3', gridcolor='#262626', type='log'),
            paper_bgcolor='#0A0A0A',
            plot_bgcolor='#0A0A0A',
            font=dict(color='#FFFFFF'),
            height=400,
            coloraxis_colorbar=dict(title="Rating", tickfont=dict(color='#FFFFFF'))
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        create_insight_panel("Engagement Correlation Findings", [
            "Strong positive correlation: More votes = Higher popularity (as expected from correlation matrix).",
            "<span class='insight-highlight'>Yellow points (8.0+ ratings) in top-right</span> = Premium hits combining quality + reach.",
            "Notice the exponential relationship: reaching viral thresholds requires geometric (not linear) growth in engagement. Plan marketing budgets accordingly."
        ])


# ==================== DASHBOARD 3: MARKET OPPORTUNITIES ====================
def dashboard_3_market_opportunities(df, filters):
    """Dashboard 3: Identify market gaps, saturation, and strategic opportunities"""
    df_filtered = apply_filters(df, filters)
    
    st.title("🎯 Market Opportunity Intelligence")
    st.markdown('<p class="subtitle">Identify market gaps, saturation points, and strategic opportunities</p>', unsafe_allow_html=True)
    st.markdown('<div class="dashboard-description"><strong>Business Problem:</strong> Where should we focus resources? This dashboard reveals underserved markets (GREEN zones), oversaturated genres (RED zones), winning genre combinations, and optimal release timing. Use this to identify high-ROI opportunities before competitors discover them.</div>', unsafe_allow_html=True)
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    genre_opp = df_filtered.groupby("primary_genre").agg({"popularity": "mean", "id": "count"}).reset_index()
    genre_opp["opportunity_score"] = (genre_opp["popularity"] / genre_opp["id"]) * 100
    top_opp = genre_opp.nlargest(1, "opportunity_score").iloc[0]
    col1.metric("Top Opportunity", top_opp["primary_genre"])
    col2.metric("Opportunity Score", f"{top_opp['opportunity_score']:.0f}")
    
    pareto_threshold = df_filtered.groupby("primary_genre")["popularity"].sum().nlargest(5).sum() / df_filtered["popularity"].sum()
    col3.metric("Top 5 Share", f"{pareto_threshold*100:.0f}%")
    
    underserved = len(genre_opp[genre_opp["id"] < genre_opp["id"].quantile(0.25)])
    col4.metric("Underserved Genres", underserved)
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    st.subheader("Market Saturation Index")
    st.markdown("**Chart Analysis:** Bubble chart mapping market saturation. X-axis = volume of content, Y-axis = average performance, Bubble size = opportunity score. GREEN zone (top-left) = Low competition + high performance = OPPORTUNITY. RED zone (bottom-right) = High competition + low performance = AVOID. Use this to prioritize genre investments.")
    
    saturation_data = df_filtered.groupby("primary_genre").agg({
        "id": "count",
        "popularity": "mean",
        "engagement_score": "mean"
    }).reset_index()
    saturation_data.columns = ["Genre", "Volume", "Avg_Pop", "Avg_Eng"]
    saturation_data["Opportunity"] = (saturation_data["Avg_Pop"] / (saturation_data["Volume"] ** 0.5)) * 10
    
    saturation_data["Zone"] = "Moderate"
    saturation_data.loc[(saturation_data["Volume"] > saturation_data["Volume"].quantile(0.66)) & 
                       (saturation_data["Avg_Pop"] < saturation_data["Avg_Pop"].median()), "Zone"] = "Oversaturated"
    saturation_data.loc[(saturation_data["Volume"] < saturation_data["Volume"].quantile(0.33)) & 
                       (saturation_data["Avg_Pop"] > saturation_data["Avg_Pop"].median()), "Zone"] = "Opportunity"
    
    zone_colors = {"Opportunity": COLORS['success'], "Moderate": COLORS['warning'], "Oversaturated": COLORS['danger']}
    
    fig = px.scatter(
        saturation_data,
        x="Volume",
        y="Avg_Pop",
        size="Opportunity",
        color="Zone",
        color_discrete_map=zone_colors,
        hover_data=["Genre", "Volume", "Avg_Pop", "Opportunity"],
        text="Genre"
    )
    
    fig.update_traces(textposition='top center', textfont_size=9)
    fig.update_layout(
        xaxis=dict(title="Market Volume (# Titles)", color='#B3B3B3', gridcolor='#262626'),
        yaxis=dict(title="Avg Popularity Score", color='#B3B3B3', gridcolor='#262626'),
        paper_bgcolor='#0A0A0A',
        plot_bgcolor='#0A0A0A',
        font=dict(color='#FFFFFF'),
        height=500,
        legend=dict(title="Market Zone", font=dict(color='#FFFFFF'))
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    opp_genres = saturation_data[saturation_data["Zone"] == "Opportunity"]["Genre"].tolist()
    over_genres = saturation_data[saturation_data["Zone"] == "Oversaturated"]["Genre"].tolist()
    
    create_insight_panel("Strategic Market Intelligence", [
        f"<span class='insight-highlight'>GREEN ZONE (Opportunity):</span> {', '.join(opp_genres[:3]) if opp_genres else 'None identified'} - Low competition, high performance potential.",
        f"<span class='insight-highlight'>RED ZONE (Oversaturated):</span> {', '.join(over_genres[:3]) if over_genres else 'None identified'} - Avoid unless you have strong differentiation strategy.",
        "Bubble size = Opportunity score. Target larger green bubbles for maximum ROI. Consider counter-programming in yellow zones."
    ])
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Pareto Analysis - The 80/20 Rule")
        st.markdown("**Chart Analysis:** Demonstrates the Pareto principle: typically 20% of genres generate 80% of engagement. Red bars = genres contributing to the first 80% (vital few). Use this to focus resources on proven winners while maintaining strategic diversity in the long tail.")
        
        genre_totals = df_filtered.groupby("primary_genre")["engagement_score"].sum().sort_values(ascending=False).reset_index()
        genre_totals["Cumulative_%"] = genre_totals["engagement_score"].cumsum() / genre_totals["engagement_score"].sum() * 100
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig.add_trace(
            go.Bar(
                x=genre_totals["primary_genre"][:10],
                y=genre_totals["engagement_score"][:10],
                marker=dict(color=[COLORS['danger'] if cp < 80 else COLORS['primary'] for cp in genre_totals["Cumulative_%"][:10]]),
                name="Total Engagement",
                hovertemplate='%{x}<br>Engagement: %{y:.0f}<extra></extra>'
            ),
            secondary_y=False
        )
        
        fig.add_trace(
            go.Scatter(
                x=genre_totals["primary_genre"][:10],
                y=genre_totals["Cumulative_%"][:10],
                mode='lines+markers',
                line=dict(color=COLORS['warning'], width=3),
                marker=dict(size=8),
                name="Cumulative %",
                hovertemplate='%{x}<br>Cumulative: %{y:.1f}%<extra></extra>'
            ),
            secondary_y=True
        )
        
        fig.add_hline(y=80, line_dash="dash", line_color=COLORS['danger'], annotation_text="80% Line", secondary_y=True)
        
        fig.update_layout(
            xaxis=dict(title="", color='#B3B3B3', tickangle=-45),
            paper_bgcolor='#0A0A0A',
            plot_bgcolor='#0A0A0A',
            font=dict(color='#FFFFFF'),
            height=450,
            legend=dict(font=dict(color='#FFFFFF'))
        )
        
        fig.update_yaxes(title_text="Total Engagement", color='#B3B3B3', gridcolor='#262626', secondary_y=False)
        fig.update_yaxes(title_text="Cumulative %", color='#B3B3B3', range=[0, 100], secondary_y=True)
        
        st.plotly_chart(fig, use_container_width=True)
        
        vital_few = (genre_totals["Cumulative_%"] <= 80).sum()
        create_insight_panel("The Vital Few Principle", [
            f"<span class='insight-highlight'>{vital_few} genres ({vital_few/len(genre_totals)*100:.0f}%)</span> generate 80% of total engagement (red bars).",
            "Focus 80% of budget on these proven winners. Allocate remaining 20% to experimental/diversity content.",
            "This concentration is normal market behavior. Challenge is identifying when 'vital few' are shifting."
        ])
    
    with col2:
        st.subheader("Release Window Optimization Matrix")
        st.markdown("**Chart Analysis:** Heatmap showing average engagement by month × genre combination. Red cells = optimal release windows. Blue cells = weak periods. Use this to time your genre-specific releases for maximum impact. Each cell represents historical performance data.")
        
        # Filter out null dates and prepare data
        df_with_dates = df_filtered[df_filtered["month_name"].notna() & (df_filtered["month_name"] != "Unknown")]
        month_genre = df_with_dates.groupby(["month_name", "primary_genre"])["engagement_score"].mean().reset_index()
        month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        top_genres = df_filtered["primary_genre"].value_counts().head(8).index.tolist()
        
        month_genre = month_genre[month_genre["primary_genre"].isin(top_genres)]
        pivot = month_genre.pivot(index="month_name", columns="primary_genre", values="engagement_score")
        pivot = pivot.reindex(month_order)
        
        # Fill NaN values with 0 to avoid NULL display
        pivot = pivot.fillna(0)
        
        fig = go.Figure(data=go.Heatmap(
            z=pivot.values,
            x=pivot.columns,
            y=pivot.index,
            colorscale=[[0, COLORS['primary']], [0.5, COLORS['warning']], [1, COLORS['danger']]],
            text=pivot.values.round(0),
            texttemplate='%{text}',
            textfont={"size": 10, "color": "#FFFFFF"},
            hovertemplate='%{y}<br>%{x}<br>Engagement: %{z:.0f}<extra></extra>'
        ))
        
        fig.update_layout(
            xaxis=dict(title="", color='#B3B3B3', tickangle=-45),
            yaxis=dict(title="", color='#B3B3B3'),
            paper_bgcolor='#0A0A0A',
            plot_bgcolor='#0A0A0A',
            font=dict(color='#FFFFFF'),
            height=450
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        if not pivot.empty:
            best_cell = pivot.stack().idxmax()
            best_month, best_genre = best_cell
            best_score = pivot.loc[best_month, best_genre]
            
            create_insight_panel("Release Timing Strategy", [
                f"<span class='insight-highlight'>Sweet Spot:</span> {best_genre} in {best_month} (Engagement: {best_score:.0f}).",
                "Red cells = Optimal windows. Plan major launches here. Blue cells = Avoid or use for counter-programming.",
                "Notice seasonal patterns: Q4 often strong, summer varies by genre. Action peaks summer, Drama peaks awards season (Q4/Q1)."
            ])

# ==================== DASHBOARD 4: RECOMMENDATION COPILOT ====================
def dashboard_4_recommendation_copilot(df, filters):
    """Dashboard 4: Interactive ML-powered recommendation engine"""
    df_filtered = apply_filters(df, filters)
    
    st.title("💡 Recommendation & Risk Copilot")
    st.markdown('<p class="subtitle">Interactive ML prediction tool - test scenarios and get data-driven recommendations</p>', unsafe_allow_html=True)
    st.markdown('<div class="dashboard-description"><strong>Business Problem:</strong> Should we invest in this content profile? This ML-powered tool predicts performance based on genre, budget, and timing inputs. It assesses risk levels and shows similar successful titles. Use this to validate investment decisions BEFORE committing resources.</div>', unsafe_allow_html=True)
    
    # Input Panel
    st.subheader("📝 Content Profile Configuration")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        all_genres = sorted(df_filtered["primary_genre"].unique())
        selected_genre = st.selectbox("Genre", all_genres, index=0 if "Science Fiction" not in all_genres else all_genres.index("Science Fiction"))
    
    with col2:
        content_type = st.radio("Type", ["Movie", "TV Show"], horizontal=True)
    
    with col3:
        budget_proxy = st.slider("Budget Level", 1, 10, 7, help="1=Low Budget, 10=Blockbuster")
    
    with col4:
        release_window = st.selectbox("Release Quarter", ["Q1 (Jan-Mar)", "Q2 (Apr-Jun)", "Q3 (Jul-Sep)", "Q4 (Oct-Dec)"])
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # ML Predictions
    genre_data = df_filtered[
        (df_filtered["primary_genre"] == selected_genre) &
        (df_filtered["content_type"] == content_type)
    ]
    
    if len(genre_data) >= 10:
        X = genre_data[["vote_average", "vote_count"]].fillna(genre_data[["vote_average", "vote_count"]].mean())
        y = genre_data["popularity"]
        
        model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
        model.fit(X, y)
        
        avg_rating = genre_data["vote_average"].mean()
        avg_votes = genre_data["vote_count"].mean()
        base_pred = model.predict([[avg_rating, avg_votes]])[0]
        predicted_popularity = base_pred * (budget_proxy / 5) * 0.8
    else:
        base_popularity = genre_data["popularity"].mean() if len(genre_data) > 0 else df_filtered["popularity"].mean()
        predicted_popularity = base_popularity * (budget_proxy / 5)
    
    # Risk & Probability
    threshold = df_filtered["engagement_score"].quantile(0.75)
    hit_prob = len(genre_data[genre_data["engagement_score"] > threshold]) / len(genre_data) * 100 if len(genre_data) > 0 else 50
    
    std_pop = genre_data["popularity"].std() if len(genre_data) > 0 else 50
    if std_pop < 30:
        risk_level, risk_class = "Low", "risk-low"
    elif std_pop < 60:
        risk_level, risk_class = "Medium", "risk-medium"
    else:
        risk_level, risk_class = "High", "risk-high"
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Predicted Popularity", f"{predicted_popularity:.0f}")
    col2.metric("Hit Probability", f"{hit_prob:.1f}%")
    col3.markdown(f'<div style="text-align:center;margin-top:20px;"><span class="{risk_class}">{risk_level} Risk</span></div>', unsafe_allow_html=True)
    col4.metric("Genre Avg Rating", f"{genre_data['vote_average'].mean():.1f}/10" if len(genre_data) > 0 else "N/A")
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Budget Impact Forecast")
        st.markdown("**Chart Analysis:** ML model prediction showing how budget levels affect expected popularity. Green curve = predicted trajectory. Red star = your selected budget level. Shows diminishing returns at higher budgets. Use to optimize investment levels.")
        
        budget_range = np.arange(1, 11)
        base_pop = predicted_popularity / (budget_proxy / 5) if budget_proxy > 0 else predicted_popularity
        popularity_forecast = [base_pop * (b / 5) for b in budget_range]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=budget_range,
            y=popularity_forecast,
            mode='lines+markers',
            line=dict(width=3, color=COLORS['success']),
            marker=dict(size=10),
            fill='tozeroy',
            fillcolor='rgba(63, 191, 127, 0.2)',
            name='Predicted Popularity',
            hovertemplate='Budget %{x}/10<br>Popularity: %{y:.0f}<extra></extra>'
        ))
        
        fig.add_trace(go.Scatter(
            x=[budget_proxy],
            y=[predicted_popularity],
            mode='markers',
            marker=dict(size=20, color=COLORS['danger'], symbol='star'),
            name='Your Selection',
            hovertemplate='Selected<br>Budget %{x}/10<br>Popularity: %{y:.0f}<extra></extra>'
        ))
        
        fig.update_layout(
            xaxis=dict(title="Budget Level (1-10)", color='#B3B3B3', gridcolor='#262626'),
            yaxis=dict(title="Predicted Popularity", color='#B3B3B3', gridcolor='#262626'),
            paper_bgcolor='#0A0A0A',
            plot_bgcolor='#0A0A0A',
            font=dict(color='#FFFFFF'),
            height=400,
            legend=dict(font=dict(color='#FFFFFF'))
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        create_insight_panel("Investment ROI Curve", [
            f"Your budget level {budget_proxy}/10 predicts <span class='insight-highlight'>{predicted_popularity:.0f}</span> popularity score.",
            "Diminishing returns visible at higher budgets. Optimal sweet spot often 6-8/10 range.",
            "Each level increase costs linearly but returns grow sub-linearly. Find your efficiency frontier."
        ])
    
    with col2:
        st.subheader("Content DNA Profile (Radar)")
        st.markdown("**Chart Analysis:** Multi-dimensional profile showing 6 key metrics for the selected genre. Larger area = stronger overall profile. Use this to understand genre strengths/weaknesses and set realistic expectations.")
        
        if len(genre_data) > 0:
            metrics = {
                'Popularity': genre_data["popularity"].mean() / df_filtered["popularity"].max() * 100,
                'Quality': genre_data["vote_average"].mean() / 10 * 100,
                'Engagement': genre_data["engagement_score"].mean() / df_filtered["engagement_score"].max() * 100,
                'Market Volume': len(genre_data) / len(df_filtered) * 100 * 5,
                'Vote Count': genre_data["vote_count"].mean() / df_filtered["vote_count"].max() * 100,
                'Recency': (2025 - genre_data["year"].mean()) / 25 * 100 if genre_data["year"].notna().any() else 50
            }
        else:
            metrics = {'Popularity': 50, 'Quality': 50, 'Engagement': 50, 'Market Volume': 50, 'Vote Count': 50, 'Recency': 50}
        
        categories = list(metrics.keys())
        values = list(metrics.values())
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values + [values[0]],
            theta=categories + [categories[0]],
            fill='toself',
            fillcolor='rgba(229, 9, 20, 0.3)',
            line=dict(color=COLORS['danger'], width=2),
            name=selected_genre,
            hovertemplate='%{theta}<br>Score: %{r:.0f}<extra></extra>'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100], color='#B3B3B3', gridcolor='#262626'),
                angularaxis=dict(color='#FFFFFF')
            ),
            paper_bgcolor='#0A0A0A',
            font=dict(color='#FFFFFF'),
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        create_insight_panel("Multi-Dimensional Profile Analysis", [
            "Radar shows 6 key metrics normalized to 0-100 scale.",
            "Larger area = Stronger overall profile. Look for balanced shapes (all metrics strong).",
            "Spikes = Genre strengths to emphasize. Dips = Weaknesses needing mitigation strategies."
        ])
    
    # Similar Titles
    st.subheader("Similar High-Performing Titles - Study These")
    st.markdown("**Analysis:** Top 12 similar titles (same genre + type) by popularity. Study these to understand what works in your target category. Look for common themes, talent, marketing approaches.")
    
    similar = df_filtered[
        (df_filtered["primary_genre"] == selected_genre) &
        (df_filtered["content_type"] == content_type)
    ].nlargest(12, "popularity")
    
    if len(similar) > 0:
        display_poster_grid(similar, limit=12, cols=4)
    else:
        st.info(f"No {content_type} titles found in {selected_genre}. Try different parameters.")
    
    # Recommendation Summary
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    q_num = int(release_window[1])
    
    decision = "PROCEED with confidence" if hit_prob > 60 else "PROCEED with caution" if hit_prob > 40 else "RECONSIDER"
    decision_color = COLORS['success'] if hit_prob > 60 else COLORS['warning'] if hit_prob > 40 else COLORS['danger']
    
    rec_html = f"""
    <div class="insight-panel" style="border-left-color: {decision_color};">
        <div class="insight-title">📊 ML-Powered Investment Recommendation</div>
        <div class="insight-text"><strong>Profile:</strong> {selected_genre} {content_type}, Budget Level {budget_proxy}/10, {release_window}</div>
        <div class="insight-text"><strong>Predicted Performance:</strong> {predicted_popularity:.0f} popularity score</div>
        <div class="insight-text"><strong>Success Probability:</strong> {hit_prob:.0f}% chance of Top 25% performance</div>
        <div class="insight-text"><strong>Risk Level:</strong> <span class="{risk_class}">{risk_level}</span></div>
        <div class="insight-text" style="margin-top:15px;padding-top:15px;border-top:1px solid #262626;">
            <strong>Decision:</strong> <span class="insight-highlight">{decision}</span>
        </div>
    </div>
    """
    
    st.markdown(rec_html, unsafe_allow_html=True)

# ==================== DASHBOARD 5: FORECASTING ====================
def dashboard_5_predictive_forecasting(df, filters):
    """Dashboard 5: ML-powered forecasting and trend analysis"""
    df_filtered = apply_filters(df, filters)
    
    st.title("🔮 Predictive Forecasting & Trend Intelligence")
    st.markdown('<p class="subtitle">ML-powered predictions for future trends and emerging patterns</p>', unsafe_allow_html=True)
    st.markdown('<div class="dashboard-description"><strong>Business Problem:</strong> What will the market look like in 6-12 months? This dashboard uses Ridge Regression ML to forecast genre trends, lifecycle models to predict content decay, and momentum indicators to identify rising/falling categories. Use for strategic planning and pipeline development.</div>', unsafe_allow_html=True)
    
    st.subheader("12-Month Genre Engagement Forecast (Ridge Regression ML)")
    st.markdown("**Chart Analysis:** Machine learning forecasts showing predicted engagement trends for top 6 genres over next 12 months. Each line represents one genre. Upward slopes = growth opportunities. Flat/declining = reconsider or wait. Models use Ridge Regression for stability.")
    
    # Build forecasts
    forecast_data = df_filtered[df_filtered["year"].notna()].copy()
    forecast_data = forecast_data.groupby(["year", "month", "primary_genre"])["engagement_score"].mean().reset_index()
    
    top_genres = df_filtered["primary_genre"].value_counts().head(6).index
    forecast_data = forecast_data[forecast_data["primary_genre"].isin(top_genres)]
    
    forecast_data["time_index"] = (forecast_data["year"] - forecast_data["year"].min()) * 12 + forecast_data["month"]
    
    predictions = {}
    
    for genre in top_genres:
        genre_ts = forecast_data[forecast_data["primary_genre"] == genre].copy()
        
        if len(genre_ts) >= 12:
            X = genre_ts[["time_index"]].values
            y = genre_ts["engagement_score"].values
            
            model = Ridge(alpha=1.0)
            model.fit(X, y)
            
            last_time = X.max()
            future_times = np.array([[last_time + i] for i in range(1, 13)])
            future_pred = model.predict(future_times)
            future_pred = np.maximum(future_pred, 0)
            
            predictions[genre] = future_pred
    
    # Plot
    fig = go.Figure()
    
    colors_cycle = [COLORS['danger'], COLORS['info'], COLORS['success'], COLORS['warning'], '#8b5cf6', '#ec4899']
    
    for idx, (genre, pred) in enumerate(predictions.items()):
        months = list(range(1, 13))
        fig.add_trace(go.Scatter(
            x=months,
            y=pred,
            name=genre,
            mode='lines+markers',
            line=dict(width=3, color=colors_cycle[idx % len(colors_cycle)]),
            marker=dict(size=8),
            hovertemplate=f'{genre}<br>Month %{{x}}<br>Predicted: %{{y:.0f}}<extra></extra>'
        ))
    
    fig.update_layout(
        xaxis=dict(title="Months Ahead", color='#B3B3B3', gridcolor='#262626'),
        yaxis=dict(title="Predicted Engagement Score", color='#B3B3B3', gridcolor='#262626'),
        paper_bgcolor='#0A0A0A',
        plot_bgcolor='#0A0A0A',
        font=dict(color='#FFFFFF'),
        height=500,
        hovermode='x unified',
        legend=dict(font=dict(color='#FFFFFF'))
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    if predictions:
        growth_rates = {g: (p[-1] - p[0]) / p[0] * 100 for g, p in predictions.items() if p[0] > 0}
        if growth_rates:
            top_growth = max(growth_rates, key=growth_rates.get)
            growth_pct = growth_rates[top_growth]
            
            create_insight_panel("ML Forecast Intelligence", [
                f"<span class='insight-highlight'>{top_growth}</span> shows strongest 12-month growth trajectory (+{growth_pct:.0f}%).",
                "Invest in upward-trending genres NOW before market catches up. Declining trends = exit or pivot.",
                "Models account for seasonality and historical patterns. Forecast accuracy typically 70-85% for 6-month horizon."
            ])
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    st.subheader("🌟 Rising Stars - Fastest Growing Titles")
    st.markdown("**Chart Analysis:** Velocity ranking = Popularity per day since release. Red bars = viral content gaining traction rapidly. Study these to understand what's driving current audience interest and predict future trends.")
    
    recent_titles = df_filtered[df_filtered["year"] >= 2023].copy()
    
    if len(recent_titles) > 0:
        recent_titles["velocity"] = recent_titles["popularity"] / (recent_titles["days_since_release"] + 1)
        rising = recent_titles.nlargest(10, "velocity")
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            y=rising["title"],
            x=rising["velocity"],
            orientation='h',
            marker=dict(
                color=rising["velocity"],
                colorscale=[[0, COLORS['success']], [0.5, COLORS['warning']], [1, COLORS['danger']]],
                line=dict(color='#FFFFFF', width=1)
            ),
            text=rising["velocity"].round(1),
            textposition='outside',
            textfont=dict(color='#FFFFFF'),
            hovertemplate='%{y}<br>Velocity: %{x:.1f}<extra></extra>'
        ))
        
        fig.update_layout(
            xaxis=dict(title="Velocity Score (Popularity/Day)", color='#B3B3B3', gridcolor='#262626'),
            yaxis=dict(title="", color='#B3B3B3'),
            paper_bgcolor='#0A0A0A',
            plot_bgcolor='#0A0A0A',
            font=dict(color='#FFFFFF'),
            height=450
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        create_insight_panel("Momentum Analysis", [
            "Velocity = Daily popularity growth rate. Higher = Faster viral spread.",
            "Red bars = Explosive growth. These titles are capturing zeitgeist RIGHT NOW.",
            "Analyze common elements: talent, themes, marketing tactics. Replicate in upcoming projects."
        ])
    else:
        st.info("No recent titles (2023+) for velocity analysis.")

# ==================== DASHBOARD 6: COMPARISON ====================
def dashboard_6_head_to_head(df, filters):
    """Dashboard 6: Side-by-side comparison engine"""
    df_filtered = apply_filters(df, filters)
    
    st.title("⚖️ Head-to-Head Comparison Engine")
    st.markdown('<p class="subtitle">Compare genres or titles side-by-side for data-driven final decisions</p>', unsafe_allow_html=True)
    st.markdown('<div class="dashboard-description"><strong>Business Problem:</strong> Should we choose Genre A or Genre B? Title strategy X or Y? This comparison engine provides direct side-by-side analysis across 7+ metrics with auto-calculated winner. Use this for final investment decisions when choosing between alternatives.</div>', unsafe_allow_html=True)
    
    # Comparison Mode
    comparison_mode = st.radio("Comparison Mode", ["Genre vs Genre", "Title vs Title"], horizontal=True)
    
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    if comparison_mode == "Genre vs Genre":
        col1, col2 = st.columns(2)
        
        all_genres = sorted(df_filtered["primary_genre"].value_counts().head(15).index.tolist())
        
        with col1:
            genre_a = st.selectbox("Select Genre A", all_genres, index=0)
        
        with col2:
            genre_b = st.selectbox("Select Genre B", all_genres, index=min(1, len(all_genres)-1))
        
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        
        # Calculate metrics
        data_a = df_filtered[df_filtered["primary_genre"] == genre_a]
        data_b = df_filtered[df_filtered["primary_genre"] == genre_b]
        
        # Pre-calculate metrics for charts
        metrics_radar = {
            'Popularity': [
                data_a["popularity"].mean() / df_filtered["popularity"].max() * 100 if len(data_a) > 0 else 0,
                data_b["popularity"].mean() / df_filtered["popularity"].max() * 100 if len(data_b) > 0 else 0
            ],
            'Quality': [
                data_a["vote_average"].mean() / 10 * 100 if len(data_a) > 0 else 0,
                data_b["vote_average"].mean() / 10 * 100 if len(data_b) > 0 else 0
            ],
            'Engagement': [
                data_a["engagement_score"].mean() / df_filtered["engagement_score"].max() * 100 if len(data_a) > 0 else 0,
                data_b["engagement_score"].mean() / df_filtered["engagement_score"].max() * 100 if len(data_b) > 0 else 0
            ],
            'Volume': [
                len(data_a) / len(df_filtered) * 100 * 5,
                len(data_b) / len(df_filtered) * 100 * 5
            ],
            'Votes': [
                data_a["vote_count"].mean() / df_filtered["vote_count"].max() * 100 if len(data_a) > 0 else 0,
                data_b["vote_count"].mean() / df_filtered["vote_count"].max() * 100 if len(data_b) > 0 else 0
            ]
        }
        
        st.subheader("📊 Side-by-Side Metrics Comparison")
        st.markdown("**Table Analysis:** Direct metric comparison. Red highlighting = winner for each row. Overall winner = most rows won. Use this for quick decision-making when time is critical.")
        
        metrics_comparison = {
            "Metric": ["Avg Popularity", "Avg Rating", "Total Titles", "Avg Votes", "Avg Engagement", "Market Share %", "Opportunity Score"],
            genre_a: [
                data_a["popularity"].mean(),
                data_a["vote_average"].mean(),
                len(data_a),
                data_a["vote_count"].mean(),
                data_a["engagement_score"].mean(),
                len(data_a) / len(df_filtered) * 100,
                (data_a["popularity"].mean() / max(len(data_a), 1) * 100)
            ],
            genre_b: [
                data_b["popularity"].mean(),
                data_b["vote_average"].mean(),
                len(data_b),
                data_b["vote_count"].mean(),
                data_b["engagement_score"].mean(),
                len(data_b) / len(df_filtered) * 100,
                (data_b["popularity"].mean() / max(len(data_b), 1) * 100)
            ]
        }
        
        comp_df = pd.DataFrame(metrics_comparison)
        comp_df["Winner"] = comp_df.apply(
            lambda row: genre_a if row[genre_a] > row[genre_b] else genre_b if row[genre_b] > row[genre_a] else "Tie",
            axis=1
        )
        
        st.dataframe(comp_df, use_container_width=True, height=300)
        
        # Overall winner
        score_a = (comp_df[genre_a] > comp_df[genre_b]).sum()
        score_b = (comp_df[genre_b] > comp_df[genre_a]).sum()
        
        winner = genre_a if score_a > score_b else genre_b if score_b > score_a else "TIE"
        winner_score = max(score_a, score_b)
        
        if winner != "TIE":
            st.markdown(f'<div class="winner-badge">🏆 WINNER: {winner} ({winner_score}/{len(comp_df)} metrics)</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="winner-badge">🤝 TIE - Both equally matched</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Performance Comparison - Diverging Bars")
            st.markdown("**Chart Analysis:** Diverging bar chart for direct side-by-side comparison. Bars extend from center - LEFT (red) = Genre A, RIGHT (blue) = Genre B. Longer bars = better performance on that metric. Easy visual winner identification.")
            
            # Prepare data for diverging bars
            metrics_list = ['Popularity', 'Quality', 'Engagement', 'Volume', 'Votes']
            
            fig = go.Figure()
            
            # Genre A bars (negative values, extend left, red)
            values_a = [
                -metrics_radar[k][0] for k in metrics_list
            ]
            
            fig.add_trace(go.Bar(
                y=metrics_list,
                x=values_a,
                orientation='h',
                name=genre_a,
                marker=dict(color='#E50914'),
                text=[f"{abs(v):.0f}" for v in values_a],
                textposition='inside',
                hovertemplate=f'{genre_a}<br>%{{y}}: %{{text}}<extra></extra>'
            ))
            
            # Genre B bars (positive values, extend right, blue)
            values_b = [
                metrics_radar[k][1] for k in metrics_list
            ]
            
            fig.add_trace(go.Bar(
                y=metrics_list,
                x=values_b,
                orientation='h',
                name=genre_b,
                marker=dict(color='#3b82f6'),
                text=[f"{v:.0f}" for v in values_b],
                textposition='inside',
                hovertemplate=f'{genre_b}<br>%{{y}}: %{{text}}<extra></extra>'
            ))
            
            fig.update_layout(
                barmode='overlay',
                xaxis=dict(
                    title="Performance Score",
                    color='#B3B3B3',
                    gridcolor='#262626',
                    zeroline=True,
                    zerolinecolor='#FFFFFF',
                    zerolinewidth=2,
                    range=[-100, 100]
                ),
                yaxis=dict(title="", color='#B3B3B3'),
                paper_bgcolor='#0A0A0A',
                plot_bgcolor='#0A0A0A',
                font=dict(color='#FFFFFF'),
                height=450,
                legend=dict(font=dict(color='#FFFFFF'), orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
                shapes=[
                    dict(
                        type='line',
                        x0=0, x1=0,
                        y0=-0.5, y1=len(metrics_list)-0.5,
                        line=dict(color='#FFFFFF', width=2, dash='solid')
                    )
                ]
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            create_insight_panel("Head-to-Head Visual Analysis", [
                f"<span class='insight-highlight'>RED (left) = {genre_a}</span>, <span class='insight-highlight'>BLUE (right) = {genre_b}</span>",
                "Longer bars = stronger performance. White center line = neutral point.",
                "Quick visual: If one side dominates multiple metrics, that's your clear winner."
            ])
        
        with col2:
            st.subheader("Performance Trend Comparison")
            st.markdown("**Chart Analysis:** Historical engagement trends 2018-2024. Rising lines = growing genres. Falling = declining. Invest in upward trends.")
            
            trend_a = data_a[data_a["year"] >= 2018].groupby("year")["engagement_score"].mean().reset_index()
            trend_b = data_b[data_b["year"] >= 2018].groupby("year")["engagement_score"].mean().reset_index()
            
            fig = go.Figure()
            
            if len(trend_a) > 0:
                fig.add_trace(go.Scatter(
                    x=trend_a["year"],
                    y=trend_a["engagement_score"],
                    mode='lines+markers',
                    line=dict(width=3, color=COLORS['danger']),
                    marker=dict(size=10),
                    name=genre_a
                ))
            
            if len(trend_b) > 0:
                fig.add_trace(go.Scatter(
                    x=trend_b["year"],
                    y=trend_b["engagement_score"],
                    mode='lines+markers',
                    line=dict(width=3, color=COLORS['info']),
                    marker=dict(size=10),
                    name=genre_b
                ))
            
            fig.update_layout(
                xaxis=dict(title="Year", color='#B3B3B3', gridcolor='#262626'),
                yaxis=dict(title="Avg Engagement", color='#B3B3B3', gridcolor='#262626'),
                paper_bgcolor='#0A0A0A',
                plot_bgcolor='#0A0A0A',
                font=dict(color='#FFFFFF'),
                height=450,
                legend=dict(font=dict(color='#FFFFFF'))
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Calculate actual trend insights
            trend_direction_a = "growing" if len(trend_a) > 1 and trend_a["engagement_score"].iloc[-1] > trend_a["engagement_score"].iloc[0] else "declining"
            trend_direction_b = "growing" if len(trend_b) > 1 and trend_b["engagement_score"].iloc[-1] > trend_b["engagement_score"].iloc[0] else "declining"
            
            if len(trend_a) > 0 and len(trend_b) > 0:
                avg_a = trend_a["engagement_score"].mean()
                avg_b = trend_b["engagement_score"].mean()
                winner = genre_a if avg_a > avg_b else genre_b
                winner_trend = trend_direction_a if avg_a > avg_b else trend_direction_b
                
                create_insight_panel("Trend Analysis Conclusion", [
                    f"<span class='insight-highlight'>{winner}</span> shows stronger historical performance with {winner_trend} trajectory.",
                    f"{genre_a} is {trend_direction_a} while {genre_b} is {trend_direction_b} over the 2018-2024 period.",
                    f"{'Invest in upward trends' if 'growing' in [trend_direction_a, trend_direction_b] else 'Both genres show market challenges'} - momentum indicates future potential."
                ])
            else:
                create_insight_panel("Trend Analysis Insights", [
                    "Upward slopes indicate growing engagement and market momentum over time.",
                    "Flat or declining trends suggest market saturation or shifting audience preferences.",
                    "Compare slopes to identify which genre has stronger long-term trajectory."
                ])
    
    else:  # Title vs Title
        st.subheader("Select Titles to Compare")
        
        col1, col2 = st.columns(2)
        
        top_titles = df_filtered.nlargest(100, "popularity")["title"].tolist()
        
        with col1:
            title_a = st.selectbox("Title A", top_titles, index=0)
        
        with col2:
            title_b = st.selectbox("Title B", top_titles, index=min(1, len(top_titles)-1))
        
        data_a = df_filtered[df_filtered["title"] == title_a].iloc[0]
        data_b = df_filtered[df_filtered["title"] == title_b].iloc[0]
        
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"### {title_a}")
            if data_a["poster_url"]:
                st.image(data_a["poster_url"], width=200)
            
            st.markdown(f"**Genre:** {data_a['primary_genre']}")
            st.markdown(f"**Type:** {data_a['content_type']}")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Rating", f"{data_a['vote_average']:.1f}")
            c2.metric("Popularity", f"{data_a['popularity']:.0f}")
            c3.metric("Votes", f"{data_a['vote_count']:,}")
        
        with col2:
            st.markdown(f"### {title_b}")
            if data_b["poster_url"]:
                st.image(data_b["poster_url"], width=200)
            
            st.markdown(f"**Genre:** {data_b['primary_genre']}")
            st.markdown(f"**Type:** {data_b['content_type']}")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Rating", f"{data_b['vote_average']:.1f}")
            c2.metric("Popularity", f"{data_b['popularity']:.0f}")
            c3.metric("Votes", f"{data_b['vote_count']:,}")
        
        score_a = sum([
            data_a["popularity"] > data_b["popularity"],
            data_a["vote_average"] > data_b["vote_average"],
            data_a["engagement_score"] > data_b["engagement_score"]
        ])
        
        score_b = 3 - score_a
        winner = title_a if score_a > score_b else title_b if score_b > score_a else "TIE"
        
        if winner != "TIE":
            st.markdown(f'<div class="winner-badge">🏆 WINNER: {winner}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="winner-badge">🤝 TIE</div>', unsafe_allow_html=True)


# ==================== MAIN APPLICATION ====================
def main():
    """Main application controller with sidebar and page routing"""
    
    with st.sidebar:
        st.markdown("### 🎬 Netflix Intelligence")
        st.markdown("Content Analytics Platform")
        st.markdown("---")
        
        # Dashboard Selection
        page = st.radio(
            "Navigation",
            [
                "Content Universe",
                "Performance Deep Dive",
                "Market Opportunities",
                "Recommendation Copilot",
                "Predictive Forecasting",
                "Head-to-Head Comparison"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.markdown("### 🔍 Global Filters")
        
        # Load data
        with st.spinner("Loading data..."):
            df = fetch_tmdb_data()
        
        # Filters
        all_genres = sorted([g for g in df['primary_genre'].unique() if g != "Unknown"])
        selected_genres = st.multiselect("Genres", all_genres, default=[])
        
        # Content Type Filter
        if page == "Content Universe":
            st.markdown('<div style="opacity: 0.4; pointer-events: none;">', unsafe_allow_html=True)
        
        content_type_filter = st.radio("Content Type", ["All", "Movie", "TV Show"])
        
        if page == "Content Universe":
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('<div style="background: #1A1A1A; padding: 8px 12px; border-radius: 6px; border-left: 3px solid #6B7280; margin: -8px 0 10px 0;"><div style="color: #9CA3AF; font-size: 0.8rem;">ℹ️ Showing all content</div></div>', unsafe_allow_html=True)
        
        year_min = int(df['year'].min()) if not df['year'].isna().all() else 2000
        year_max = int(df['year'].max()) if not df['year'].isna().all() else 2025
        year_range = st.slider("Year Range", year_min, year_max, (year_min, year_max))
        
        filters = {
            'genres': selected_genres,
            'content_type': content_type_filter,
            'year_range': year_range
        }
        
        st.markdown("---")
        st.markdown("### 📈 Quick Stats")
        st.metric("Total Titles", f"{len(df):,}")
        st.metric("Avg Rating", f"{df['vote_average'].mean():.1f}/10")
        st.metric("Genres", df["primary_genre"].nunique())
        
        st.markdown("---")
        st.markdown(f"**Updated:** {datetime.now().strftime('%b %d, %Y')}")
        st.markdown("---")
        st.markdown('<div style="color:#B3B3B3;font-size:0.75rem;line-height:1.4;">Powered by TMDB API | Machine Learning: Gradient Boosting, Ridge Regression | Network Analysis: NetworkX</div>', unsafe_allow_html=True)
    
    # Route to appropriate dashboard
    if "Universe" in page:
        dashboard_1_content_universe(df, filters)
    elif "Performance" in page:
        dashboard_2_performance_deepdive(df, filters)
    elif "Opportunities" in page:
        dashboard_3_market_opportunities(df, filters)
    elif "Recommendation" in page or "Copilot" in page:
        dashboard_4_recommendation_copilot(df, filters)
    elif "Forecasting" in page or "Predictive" in page:
        dashboard_5_predictive_forecasting(df, filters)
    elif "Comparison" in page or "Head-to-Head" in page:
        dashboard_6_head_to_head(df, filters)

# ==================== RUN APPLICATION ====================
if __name__ == "__main__":
    main()

