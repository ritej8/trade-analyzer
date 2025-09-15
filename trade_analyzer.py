# trade_analyzer.py
  # Simple SwapMate trade analyzer using Pandas

import pandas as pd
import json

def analyze_trades(csv_file="trades.csv"):
      try:
          df = pd.read_csv(csv_file)
          print("Data preview:")
          print(df.head())
          
          # Group by category
          category_counts = df.groupby('category').size()
          print("Trades by category:", category_counts)
          
          # Simple recommendation: Top categories for a user
          user_id = 1
          user_trades = df[df['user_id'] == user_id]['category'].value_counts()
          print("User 1's top categories:", user_trades)
          
          # Save to JSON
          summary = {"category_counts": category_counts.to_dict(), "user_1_top": user_trades.to_dict()}
          with open("trade_summary.json", "w") as f:
              json.dump(summary, f, indent=4)
          print("Saved summary to trade_summary.json")
          
          return summary
      except FileNotFoundError:
          return {"error": "CSV file not found"}

if __name__ == "__main__":
      analyze_trades()