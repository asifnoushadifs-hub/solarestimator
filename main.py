# solar_estimator_final.py

import streamlit as st
import pandas as pd

# -----------------------------------------------------------
# Page Setup
# -----------------------------------------------------------
st.set_page_config(page_title="Solar Estimator", page_icon="🌞", layout="centered")

st.title("🌞 Solar Plant Estimator")
st.caption("Estimate your solar potential, cost, and financing options in seconds!")

st.divider()

# -----------------------------------------------------------
# Consumer Data
# -----------------------------------------------------------
consumer_data = {
    "1001": {"avg_bill": 1400, "location": "Kollam"},
    "1002": {"avg_bill": 2100, "location": "Trivandrum"},
}

developers_by_location = {
    "Kollam": ["Tata Solar", "Energy", "Solis"],
    "Trivandrum": ["Adani Solar", "KSENERGY"],
}

banks_by_location = {
    "Kollam": [
        {"Bank": "State Bank of India", "Interest Rate": "8.2%", "Tenure": "7 years"},
        {"Bank": "HDFC Bank", "Interest Rate": "8.5%", "Tenure": "10 years"},
        {"Bank": "Federal Bank", "Interest Rate": "8.7%", "Tenure": "8 years"},
    ],
    "Trivandrum": [
        {"Bank": "Canara Bank", "Interest Rate": "8.4%", "Tenure": "9 years"},
        {"Bank": "Axis Bank", "Interest Rate": "8.6%", "Tenure": "10 years"},
        {"Bank": "Kerala Gramin Bank", "Interest Rate": "8.1%", "Tenure": "8 years"},
    ],
}

# -----------------------------------------------------------
# Input Section
# -----------------------------------------------------------
st.subheader("🏠 Consumer Information")

consumer_id = st.text_input("Enter Consumer ID", placeholder="e.g., 1001 or 1002")

location = None
avg_bill = None

if consumer_id in consumer_data:
    avg_bill = consumer_data[consumer_id]["avg_bill"]
    location = consumer_data[consumer_id]["location"]

    st.success(f"Average Monthly Bill: ₹{avg_bill}")
    st.info(f"📍 Location: {location}")

elif consumer_id:
    st.error("❌ Consumer ID not found in database.")

# -----------------------------------------------------------
# Area Input
# -----------------------------------------------------------
st.divider()
st.subheader("☀️ Solar Exposure Area")

area = st.number_input("Enter Unshaded Area (in sq. ft.)", min_value=0.0, step=10.0, format="%.2f")

# -----------------------------------------------------------
# Prediction Logic
# -----------------------------------------------------------
st.divider()
if st.button("🔮 Predict Solar Potential"):
    if avg_bill and area > 0:
        # Core Calculations
        plant_kw = round(area / 100, 2)
        monthly_savings = round(avg_bill * 0.8, 2)
        subsidy = round(plant_kw * 30000, 2)
        cost = round(plant_kw * 65000, 2)
        net_cost = round(cost - subsidy, 2)

        st.success("✅ Solar Estimation Summary")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Solar Plant Capacity", f"{plant_kw} KW")
            st.metric("Estimated Monthly Savings", f"₹{monthly_savings}")
        with col2:
            st.metric("Subsidy (Govt.)", f"₹{subsidy}")
            st.metric("Installation Cost", f"₹{cost}")

        st.info(f"💰 **Net Cost after Subsidy:** ₹{net_cost}")

        st.divider()

        # -----------------------------------------------------------
        # Developers Section
        # -----------------------------------------------------------
        if location:
            st.subheader(f"🔧 Solar Developers in {location}")
            devs = pd.DataFrame({
                "Developer": developers_by_location[location],
                "Contact": ["1800-123-1111", "1800-123-2222", "1800-123-3333"][:len(developers_by_location[location])],
                "Rating": ["⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐⭐"][:len(developers_by_location[location])]
            })
            st.dataframe(devs, use_container_width=True)

        # -----------------------------------------------------------
        # Banks Section
        # -----------------------------------------------------------
        if location:
            st.divider()
            st.subheader(f"🏦 Banks Offering Solar Loans in {location}")
            banks = pd.DataFrame(banks_by_location[location])
            st.dataframe(banks, use_container_width=True)

        # -----------------------------------------------------------
        # Support Info
        # -----------------------------------------------------------
        st.divider()
        st.info("📞 For support, dial **1800-123-45678** to reach your State Solar Advisor.")

    else:
        st.error("⚠️ Please enter a valid Consumer ID and Unshaded Area before predicting.")

# -----------------------------------------------------------
# Footer
# -----------------------------------------------------------
st.divider()
st.caption("🌱 Powered by the State Solar Mission Initiative.")
