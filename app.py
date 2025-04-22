import streamlit as st
from utils.predictor import predict_customer_segment

st.set_page_config(page_title="Customer Segmentation Chatbot", page_icon="🤖", layout="centered")

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title & Description
st.markdown("<h1 class='title'>Customer Chatbot Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Curious which type of customer you're dealing with? Answer a few quick questions and let the bot classify them.</p>", unsafe_allow_html=True)
st.markdown("---")

# Simulated chat input
with st.form("chat_form"):
    st.markdown("### Let's get to know your customer:")
    income = st.number_input("What's their Income?", min_value=0, value=40000, step=1000)
    wines = st.number_input("How much have they spent on non-essential items?", min_value=0, value=150)
    meats = st.number_input("How much on essential food items?", min_value=0, value=100)
    web = st.slider("How many times have they shopped online?", 0, 20, 5)
    catalog = st.slider("Catalog purchases?", 0, 20, 2)
    store = st.slider("Store purchases?", 0, 20, 3)
    response = st.radio("Did they respond to past campaigns?", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")

    submitted = st.form_submit_button("Predict Segment")

if submitted:
    features = {
        "Income": income,
        "MntWines": wines,
        "MntMeatProducts": meats,
        "NumWebPurchases": web,
        "NumCatalogPurchases": catalog,
        "NumStorePurchases": store,
        "Response": response
    }

    try:
        prediction = predict_customer_segment(features)

        if prediction == "High-Value Loyalist":
            card_color = "#ecfccb"
            border_color = "#65a30d"
            insight = "This customer has high spending and campaign engagement. Best to retain with loyalty perks and exclusive offers."
        else:
            card_color = "#dbeafe"
            border_color = "#2563eb"
            insight = "This customer is conscious about spending. Use targeted campaigns and value-driven communication."

        st.markdown(f"""
        <div style='
            background-color: {card_color};
            border-left: 6px solid {border_color};
            padding: 1.5rem;
            margin-top: 2rem;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        '>
            <h3 style='color: #111827; margin-bottom: 0.5rem;'>Predicted Segment: <span style='color:{border_color}'>{prediction}</span></h3>
            <p style='font-size: 1.05rem; color: #374151;'>{insight}</p>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Something went wrong: {e}")


