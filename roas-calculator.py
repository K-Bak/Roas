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
    roas_values = [i for i in range(1, 21)]  # ROAS fra 1 til 20
    profits = [(ad_spend * roas * (gross_margin / 100)) - ad_spend for roas in roas_values]
    
    plt.figure(figsize=(8, 4))
    plt.plot(roas_values, profits, marker='o', linestyle='-', label='Forventet Profit')
    plt.axhline(0, color='red', linestyle='--', label='Break-even')
    plt.xlabel("ROAS")
    plt.ylabel("Profit (kr.)")
    plt.title("Profitfremskrivning vs. ROAS")
    plt.legend()
    st.pyplot(plt)

# Streamlit UI
st.image("generaxion-logo-fixed.png", width=200)  # Tilføj logo øverst på siden
st.title("📊 ROAS Kalkulator")
st.write("Beregn din Return on Ad Spend (ROAS) og profitmål for dine kampagner.")

# Input felter
gross_margin = st.slider("Bruttomargin (%)", min_value=5, max_value=95, value=35, step=1)
ad_spend = st.number_input("Annonceringsbudget (kr.)", min_value=100, value=10000, step=100)
roas_target = st.slider("Mål-ROAS", min_value=1.0, max_value=20.0, value=2.0, step=0.1)

# Beregn metrics
break_even_roas, total_revenue, monthly_profit = calculate_roas_metrics(gross_margin, ad_spend, roas_target)

# Resultater
st.subheader("📊 Resultater")
st.metric(label="Break-even ROAS", value=round(break_even_roas, 2))
st.metric(label="Total Omsætning (kr.)", value=f"{total_revenue:,.2f} kr.")
st.metric(label="Månedlig Profit (kr.)", value=f"{monthly_profit:,.2f} kr.", delta=round(monthly_profit, 2))

# Visualisering af profit
st.subheader("📈 Profitfremskrivning")
plot_profit_projection(ad_spend, roas_target, gross_margin)

# Ny graf: Profit ved forskellige ROAS niveauer
st.subheader("📉 Profit ved forskellige ROAS-mål")
roas_values = [i for i in range(1, 21)]
profits = [(ad_spend * roas * (gross_margin / 100)) - ad_spend for roas in roas_values]

plt.figure(figsize=(8, 4))
plt.plot(roas_values, profits, marker="o", linestyle="-", label="Profit vs. ROAS")
plt.axhline(0, color="red", linestyle="--", label="Break-even")
plt.xlabel("ROAS")
plt.ylabel("Profit (kr.)")
plt.title("Profit ved forskellige ROAS-mål")
plt.legend()
st.pyplot(plt)
