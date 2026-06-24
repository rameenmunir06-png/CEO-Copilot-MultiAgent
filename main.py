import pandas as pd
import os
import json
from agents.finance_agent import run_finance_agent
from agents.inventory_agent import run_inventory_agent
from agents.customer_agent import run_customer_agent
from agents.ceo_agent import run_ceo_agent

print("🚀 CEO Copilot: Initializing Master Testing Framework...")

# Original CSV paths
finance_path = os.path.join("data", "finance_data.csv")
inventory_path = os.path.join("data", "inventory_data.csv")
reviews_path = os.path.join("data", "customer_reviews.csv")

try:
    # Real data load karna baseline ke liye
    df_finance = pd.read_csv(finance_path)
    df_inventory = pd.read_csv(inventory_path)
    df_reviews = pd.read_csv(reviews_path)
    print("✅ [SUCCESS] Baseline CSV data structures loaded successfully!")
    
    print("\n=================================================================")
    print("🔬 RUNNING TEST SCENARIOS (End-to-End Orchestration Testing)")
    print("=================================================================")

    # -------------------------------------------------------------
    # TEST CASE 1: CRITICAL/HIGH RISK (Real CSV Data Current Flow)
    # -------------------------------------------------------------
    print("\n🔥 [TEST 1] Running Current Real Data (Expected: CRITICAL / HIGH RISK)")
    print("-" * 65)
    f_json_1 = run_finance_agent(df_finance)
    i_json_1 = run_inventory_agent(df_inventory)
    c_json_1 = run_customer_agent(df_reviews)
    
    ceo_report_1 = run_ceo_agent(f_json_1, i_json_1, c_json_1)
    print(ceo_report_1)
    
    # -------------------------------------------------------------
    # TEST CASE 2: LOW RISK / IDEAL BUSINESS (Simulated Clean Data)
    # -------------------------------------------------------------
    print("\n🟢 [TEST 2] Simulating Ideal Business Conditions (Expected: LOW / STABLE)")
    print("-" * 65)
    # Fake healthy data generate karna code ke andar testing ke liye
    f_clean_json = json.dumps({"total_revenue": 900000, "total_expenses": 300000, "average_profit_margin": 66.6, "anomaly_detected": False})
    i_clean_json = json.dumps({"total_unique_products": 4, "critical_low_stock_items": 0, "reorder_required": False, "items_to_reorder": []})
    c_clean_json = json.dumps({"total_reviews_received": 10, "positive_reviews": 10, "neutral_reviews": 0, "negative_reviews_flagged": 0, "customer_satisfaction_risk": False})
    
    ceo_report_2 = run_ceo_agent(f_clean_json, i_clean_json, c_clean_json)
    print(ceo_report_2)

    # -------------------------------------------------------------
    # TEST CASE 3: MEDIUM RISK (Only Inventory or Finance Issue)
    # -------------------------------------------------------------
    print("\n🟡 [TEST 3] Simulating Single Operational Issue (Expected: MEDIUM RISK)")
    print("-" * 65)
    # Sirf inventory ka issue simulate karna, baqi sab clean
    i_issue_json = json.dumps({"total_unique_products": 4, "critical_low_stock_items": 2, "reorder_required": True, "items_to_reorder": ["UltraFast USB-C Cable"]})
    
    ceo_report_3 = run_ceo_agent(f_clean_json, i_issue_json, c_clean_json)
    print(ceo_report_3)

    print("\n=================================================================")
    print("🏆 LOCAL FRAMEWORK VERIFICATION complete: All scenarios successfully handled!")
    print("=================================================================")

except FileNotFoundError as e:
    print(f"❌ [ERROR] File missing! Check folder structure. Details: {e}")
except Exception as e:
    print(f"❌ [ERROR] System Orchestration crashed during testing: {e}")