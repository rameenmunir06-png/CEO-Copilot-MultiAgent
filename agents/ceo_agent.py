import json
import os
import ssl
from google import genai
from dotenv import load_dotenv
import truststore
# .env file se API Key load karna
load_dotenv()
truststore.inject_into_ssl()

def run_ceo_agent(finance_report_json, inventory_report_json, customer_report_json):
    """
    CEO Agent (AI Powered): Sub-agents ki JSON reports ko evaluate karta hai
    aur Google Gemini API use karke intelligent advice generate karta hai.
    """
    # SSL Certificate verification ko bypass karna taake connection crash na ho
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    finance_data = json.loads(finance_report_json)
    inventory_data = json.loads(inventory_report_json)
    customer_data = json.loads(customer_report_json)
    
    finance_anomaly = finance_data.get("anomaly_detected", False)
    inventory_critical = inventory_data.get("reorder_required", False)
    customer_risk = customer_data.get("customer_satisfaction_risk", False)
    
    flags_count = sum([finance_anomaly, inventory_critical, customer_risk])
    risk_level = "HIGH RISK" if flags_count >= 2 else ("MEDIUM RISK" if flags_count == 1 else "LOW / STABLE")
        
    prompt = f"""
    You are the expert Executive AI CEO Advisor. Analyze these 3 sub-agent JSON business payloads:
    
    1. Finance Data: {finance_report_json}
    2. Inventory Data: {inventory_report_json}
    3. Customer Sentiment Data: {customer_report_json}
    
    Calculated Base Risk Level: {risk_level}
    
    Provide a professional corporate executive summary and actionable strategic recommendations. 
    Keep the response highly structured, clear, and professional.
    """

    try:
        api_key = os.getenv("GEMINI_API_KEY")
        # Client initialize karte waqt explicit allow karte hain
        client = genai.Client(api_key=api_key)
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        ai_recommendations = response.text

    except Exception as e:
        ai_recommendations = f"⚠️ [Gemini API Error]: {e}"

    executive_report = {
        "calculated_risk_level": risk_level,
        "total_operational_flags_raised": flags_count,
        "ceo_ai_strategic_analysis": ai_recommendations,
        "system_status": "Production LLM Layer Successfully Integrated"
    }
    
    return json.dumps(executive_report, indent=2)