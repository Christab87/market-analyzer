import matplotlib.pyplot as plt
import os

def plot_trends(df, output_path: str):
    """
    Creates a professional-grade trend analysis visualization.
    """
    # Use a professional style
    plt.style.use('seaborn-v0_8-darkgrid')
    
    plt.figure(figsize=(12, 6))
    
    # Plotting Price
    plt.plot(df['Date'], df['Close'], 
             label='Market Price', 
             color='#2c3e50', # Dark Blue
             linewidth=2, 
             alpha=0.7)
    
    # Plotting SMA (if it exists)
    sma_col = [col for col in df.columns if 'SMA' in col]
    if sma_col:
        plt.plot(df['Date'], df[sma_col[0]], 
                 label=f'Moving Average ({sma_col[0]})', 
                 color='#e74c3c', # Red
                 linestyle='--', 
                 linewidth=2.5)

    plt.title('Market Sentiment: Price vs. Moving Average Trend', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.legend(loc='best')
    plt.tight_layout()
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save as high-resolution
    plt.savefig(output_path, dpi=300)
    print(f"Visual report successfully exported to: {output_path}")