import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def calculate_roas_metrics(gross_margin, ad_spend, roas_target):
    # Beregn Break-even ROAS
    break_even_roas = 1 / (gross_margin / 100)
    
    # Beregn Total Revenue
    total_revenue = ad_spend * roas_target
    
    # Beregn Monthly Profit
    profit_margin = gross_margin / 100
    monthly_profit = (total_revenue * profit_margin) - ad_spend
    
    return break_even_roas, total_revenue, monthly_profit

def plot_profit_projection(ad_spend, roas_target, gross_margin):
    roas_values = [i * 0.5 for i in range(1, 11)]  # ROAS fra 0.5 til 5.0
    profits = [(ad_spend * roas * (gross_margin / 100)) - ad_spend for roas in roas_values]
    
    plt.figure(figsize=(8, 4))
    plt.plot(roas_values, profits, marker='o', linestyle='-', label='Forventet Profit')
    plt.axhline(0, color='red', linestyle='--', label='Break-even')
    plt.xlabel("ROAS")
    plt.ylabel("Profit ($)")
    plt.title("Profit Projection vs. ROAS")
    plt.legend()
    st.pyplot(plt)

# Streamlit UI
st.title("📊 ROAS Kalkulator")
st.write("Beregn din Return on Ad Spend (ROAS) og profitmål for dine kampagner.")

# Input felter
gross_margin = st.slider("Bruttomargin (%)", min_value=5, max_value=95, value=35, step=1)
ad_spend = st.number_input("Annonceringsbudget ($)", min_value=100, value=10000, step=100)
roas_target = st.slider("Mål-ROAS", min_value=1.0, max_value=5.0, value=2.0, step=0.1)

# Beregn metrics
break_even_roas, total_revenue, monthly_profit = calculate_roas_metrics(gross_margin, ad_spend, roas_target)

# Resultater
st.subheader("📊 Resultater")
st.metric(label="Break-even ROAS", value=round(break_even_roas, 2))
st.metric(label="Total Revenue ($)", value=f"{total_revenue:,.2f}")
st.metric(label="Monthly Profit ($)", value=f"{monthly_profit:,.2f}", delta=round(monthly_profit, 2))

# Visualisering af profit
st.subheader("📈 Profit Projection")
plot_profit_projection(ad_spend, roas_target, gross_margin)
