import pandas as pd
import json

def run_customer_agent(df_reviews):
    """
    Customer Agent: Reviews data ko analyze karta hai aur sentiment analysis report deta hai.
    """
    # 1. Total reviews calculate karna
    total_reviews = int(len(df_reviews))
    
    # 2. Sentiment count nikalna
    # Assuming column ka naam 'sentiment_tag' hai aur negative reviews 'Negative' hain
    neg_reviews_df = df_reviews[df_reviews['sentiment_tag'] == 'Negative']
    negative_count = int(len(neg_reviews_df))
    
    positive_count = int(len(df_reviews[df_reviews['sentiment_tag'] == 'Positive']))
    neutral_count = total_reviews - (negative_count + positive_count)
    
    # 3. Customer satisfaction alert logic
    satisfaction_risk = False
    customer_alert_msg = "Customer sentiment is healthy and positive."
    
    # Agar 30% se zyada reviews negative hon to risk true ho jaye
    if total_reviews > 0 and (negative_count / total_reviews) > 0.30:
        satisfaction_risk = True
        customer_alert_msg = "High volume of negative feedback detected! Customer retention risk."

    # 4. Standard Structured JSON Output Format
    customer_report = {
        "total_reviews_received": total_reviews,
        "positive_reviews": positive_count,
        "neutral_reviews": neutral_count,
        "negative_reviews_flagged": negative_count,
        "customer_satisfaction_risk": satisfaction_risk,
        "sentiment_status_alert": customer_alert_msg
    }
    
    return json.dumps(customer_report, indent=2)