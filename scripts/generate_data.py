import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_financial_data(days=100, start_price=150.0):
    # Set seed for reproducibility (so your tests are consistent)
    np.random.seed(42)
    
    # Generate dates
    dates = [datetime.now() - timedelta(days=i) for i in range(days)][::-1]
    
    # Random walk: Daily returns with a slight upward "drift"
    # 0.001 is a small daily growth, 0.02 is volatility (standard deviation)
    returns = np.random.normal(loc=0.001, scale=0.02, size=days)
    
    # Calculate price series
    price_series = start_price * (1 + returns).cumprod()
    
    # Create DataFrame
    df = pd.DataFrame({'Date': dates, 'Close': price_series})
    return df

if __name__ == "__main__":
    df = generate_financial_data(days=100)
    df.to_csv('data/raw_data.csv', index=False)
    print("Successfully generated 100 days of synthetic data to data/raw_data.csv")