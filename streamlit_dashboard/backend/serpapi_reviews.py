from serpapi import GoogleSearch
import streamlit as st

def fetch_google_reviews(data_id):
    params = {
        "engine": "google_maps_reviews",
        "data_id": data_id,
        "hl": "en",
        "api_key": st.secrets["SERPAPI_KEY"]
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    return results.get("reviews", [])
