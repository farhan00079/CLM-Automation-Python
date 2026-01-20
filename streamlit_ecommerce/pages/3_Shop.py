import streamlit as st

# ---------- SESSION STATE ----------
if "cart" not in st.session_state:
    st.session_state.cart = []

# ---------- HEADER ----------
col1, col2 = st.columns([8, 2])

with col1:
    st.markdown("## 🛍️ My Shopping Store")

with col2:
    st.button(f"🛒 Cart ({len(st.session_state.cart)})")

st.markdown("---")

# ---------- PRODUCTS ----------
products = [
    {"id": 1, "name": "Wireless Headphones", "price": 1499, "image": "https://picsum.photos/300?random=1"},
{"id": 2, "name": "Smart Watch", "price": 2999, "image": "https://picsum.photos/300?random=2"},
{"id": 3, "name": "Bluetooth Speaker", "price": 1999, "image": "https://picsum.photos/300?random=3"},

]

# ---------- PRODUCT GRID ----------
cols = st.columns(3)

for index, product in enumerate(products):
    with cols[index % 3]:
        st.markdown(
            """
            <div style="
                border:1px solid #e6e6e6;
                border-radius:15px;
                padding:15px;
                text-align:center;
                box-shadow:0 4px 12px rgba(0,0,0,0.08);
            ">
            """,
            unsafe_allow_html=True
        )

        st.image(product["image"], use_container_width=True)
        st.markdown(f"### {product['name']}")
        st.markdown(f"#### ₹ {product['price']}")

        if st.button("➕ Add to Cart", key=product["id"]):
            st.session_state.cart.append(product)
            st.success("Added to cart")

        st.markdown("</div>", unsafe_allow_html=True)
