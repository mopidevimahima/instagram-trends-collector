import streamlit as st
import pandas as pd

st.title("📱 Instagram Trends Dashboard")
st.markdown("**Automated scraper** – 144+ trends from Later.com")

@st.cache_data
def load_data():
    try:
        return pd.read_csv("trends.csv")
    except:
        st.error("👈 Run `python trends.py` first!")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    col1, col2 = st.columns(2)
    col1.metric("Total Trends", len(df))
    col2.metric("Unique Sounds", df['trend_name'].nunique())
    
    st.subheader("Latest Trends")
    st.dataframe(df[['trend_name', 'found_at']].tail(10))
    
    search = st.text_input("🔍 Search trends")
    if search:
        filtered = df[df['trend_name'].str.contains(search, case=False, na=False)]
        st.dataframe(filtered[['trend_name', 'found_at']])
else:
    st.info("💡 Run scraper first: `python trends.py`")
