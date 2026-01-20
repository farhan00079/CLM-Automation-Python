import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from backend.serpapi_reviews import fetch_google_reviews

st.set_page_config(page_title="Restaurant Review Analytics", layout="wide")

st.title("📊 Google Restaurant Review Analytics Dashboard")

data_id = st.text_input(
    "Enter Google Maps data_id",
    placeholder="0x89c259af336b3341:0xa4969e07ce3108de"
)

if data_id:
    with st.spinner("Fetching reviews from Google Maps..."):
        reviews = fetch_google_reviews(data_id)

    if not reviews:
        st.error("❌ No reviews found for this place")
    else:
        # ---- Ratings extraction ----
        ratings = [r.get("rating") for r in reviews if r.get("rating")]

        df = pd.DataFrame(ratings, columns=["rating"])
        rating_count = df["rating"].value_counts().sort_index()

        # ---- Analytics ----
        st.subheader("⭐ Rating Distribution")

        fig, ax = plt.subplots()
        rating_count.plot(kind="bar", ax=ax)
        ax.set_xlabel("Star Rating")
        ax.set_ylabel("Number of Users")
        ax.set_title("Google Review Rating Analytics")

        st.pyplot(fig)

        # ---- Summary ----
        st.subheader("📌 Summary")
        st.write(f"Total Reviews: {len(ratings)}")
        st.write(f"Average Rating: {round(sum(ratings)/len(ratings), 2)} ⭐")

        # ---- Sample Reviews ----
        st.subheader("📝 Sample Reviews")
        for r in reviews[:5]:
            st.markdown(
                f"""
                ⭐ **{r.get("rating")}**  
                {r.get("snippet")}
                ---
                """
            )
