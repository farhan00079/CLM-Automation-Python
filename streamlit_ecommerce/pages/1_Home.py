import streamlit as st

# ---------- LOGIN CHECK ----------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

st.set_page_config(page_title="MyKart | Home", layout="wide")

# ================= NAVBAR (STREAMLIT SAFE) =================
nav1, nav2, nav3 = st.columns([2, 4, 2])

with nav1:
    st.markdown("## 🛒 **MyKart**")

with nav2:
    st.text_input(
        "Search",
        placeholder="Search for products, brands and more",
        label_visibility="collapsed"
    )

with nav3:
    st.markdown("🛒 Cart &nbsp;&nbsp; 👤 Account")

st.divider()

# ================= MENU BAR =================
menu1, menu2, menu3 = st.columns(3)
menu1.markdown("**About**")
menu2.markdown("**Shopping**")
menu3.markdown("**Contact Us**")

st.divider()

# ================= HERO BANNER =================
st.markdown("## 🔥 Big Billion Sale")
st.info("Up to **70% OFF** on Mobiles, Fashion & Electronics")

# ================= CATEGORIES =================
st.subheader("Top Categories")
c1, c2, c3, c4 = st.columns(4)
c1.button("📱 Mobiles")
c2.button("💻 Laptops")
c3.button("👕 Fashion")
c4.button("🎧 Electronics")

st.divider()

# ================= PRODUCTS =================
st.subheader("Featured Products")

p1, p2, p3 = st.columns(3)

with p1:
    st.image("https://via.placeholder.com/200")
    st.markdown("**Smartphone**")
    st.write("₹14,999")
    st.button("Add to Cart", key="cart1")

with p2:
    st.image("https://via.placeholder.com/200")
    st.markdown("**Wireless Headphones**")
    st.write("₹2,999")
    st.button("Add to Cart", key="cart2")

with p3:
    st.image("https://via.placeholder.com/200")
    st.markdown("**Smart Watch**")
    st.write("₹4,999")
    st.button("Add to Cart", key="cart3")

st.divider()

# ================= LOGOUT =================
if st.button("Logout"):
    st.session_state.logged_in = False
    st.switch_page("app.py")
