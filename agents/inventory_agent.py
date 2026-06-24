import pandas as pd
import json

def run_inventory_agent(df_inventory):
    """
    Inventory Agent: Stock data ko analyze karta hai aur low stock items ki report deta hai.
    """
    # 1. Total unique products aur total stock nikalna
    total_products = int(df_inventory['product_id'].nunique())
    
    # 2. Critical Low Stock items dhoondna (Jahan stock_status == 'Critical Low Stock')
    low_stock_df = df_inventory[df_inventory['stock_status'] == 'Critical Low Stock']
    critical_count = int(len(low_stock_df))
    
    # 3. Restock recommendations aur alert logic
    reorder_required = False
    items_to_reorder = []
    
    if critical_count > 0:
        reorder_required = True
        # Jo items low hain unke naam list mein daalna
        items_to_reorder = low_stock_df['product_name'].tolist()
        alert_msg = f"Critical alert! {critical_count} product(s) need immediate restocking."
    else:
        alert_msg = "All product stock levels are stable."

    # 4. Standard Structured JSON Output Format
    inventory_report = {
        "total_unique_products": total_products,
        "critical_low_stock_items": critical_count,
        "reorder_required": reorder_required,
        "items_to_reorder": items_to_reorder,
        "inventory_status_alert": alert_msg
    }
    
    return json.dumps(inventory_report, indent=2)