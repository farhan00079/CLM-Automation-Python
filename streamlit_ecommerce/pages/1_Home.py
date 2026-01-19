import streamlit as st

# ---------- LOGIN CHECK ----------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

st.set_page_config(page_title="MyKart | Home", layout="wide")

# ================= NAVBAR =================
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

# ================= MENU BAR (WORKING BUTTONS) =================
menu1, menu2, menu3 = st.columns(3)

with menu1:
    if st.button("About", key="about_btn"):
        st.switch_page("pages/2_About.py")

with menu2:
    if st.button("Shopping", key="shopping_btn"):
        st.switch_page("pages/3_Shop.py")

with menu3:
    if st.button("Contact Us", key="contact_btn"):
        st.switch_page("pages/4_Contact.py")

st.divider()

# ================= HERO BANNER =================
st.markdown("## 🔥 Big Billion Sale")
st.info("Up to **70% OFF** on Mobiles, Fashion & Electronics")

# ================= CATEGORIES =================
st.subheader("Top Categories")
c1, c2, c3, c4 = st.columns(4)

c1.button("📱 Mobiles", key="cat1")
c2.button("💻 Laptops", key="cat2")
c3.button("👕 Fashion", key="cat3")
c4.button("🎧 Electronics", key="cat4")

st.divider()

# ================= PRODUCTS =================
st.subheader("Featured Products")

p1, p2, p3 = st.columns(3)

with p1:
    st.image( "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9")
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
if st.button("Logout", key="logout_btn"):
    st.session_state.logged_in = False
    st.switch_page("app.py")