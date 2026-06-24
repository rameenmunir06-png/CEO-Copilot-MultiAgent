import pandas as pd
import json

def run_finance_agent(df_finance):
    """
    Finance Agent: Financial data ko analyze karta hai aur JSON output deta hai.
    """
    # 1. Calculations
    total_revenue = int(df_finance['sales_revenue'].sum())
    total_expenses = int(df_finance['operational_costs'].sum() + df_finance['marketing_spend'].sum())
    avg_margin = float(df_finance['profit_margin_percent'].mean())
    
    # 2. Anomaly Detection Logic (Anomalies dhoondna)
    # Agar kisi din margin 20% se kam ho, to anomaly detected = True
    low_margin_days = df_finance[df_finance['profit_margin_percent'] < 20.0]
    
    anomaly_detected = False
    anomaly_reason = "No major financial anomalies detected."
    
    if not low_margin_days.empty:
        anomaly_detected = True
        date_of_drop = low_margin_days['date'].iloc[0]
        reason_text = f"Sudden profit drop on {date_of_drop} due to low margin alignment."
        anomaly_reason = reason_text

    # 3. Exactly ChatGPT ka bataya hua JSON Output Format Schema
    finance_report = {
        "total_revenue": total_revenue,
        "total_expenses": total_expenses,
        "average_profit_margin": round(avg_margin, 2),
        "anomaly_detected": anomaly_detected,
        "anomaly_reason": anomaly_reason
    }
    
    # Python dictionary ko proper JSON string mein convert karna
    return json.dumps(finance_report, indent=2)