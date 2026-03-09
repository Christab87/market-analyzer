import os
import sys

# Ensure current directory is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.analyzer import MarketAnalyzer
from src.visualizer import plot_trends

def main():
    # 1. Diagnostic: Check if data exists
    data_path = 'data/raw_data.csv'
    if not os.path.exists(data_path):
        print(f"DEBUG: File not found at {os.path.abspath(data_path)}")
        return

    try:
        print("DEBUG: Initializing Analyzer...")
        analyzer = MarketAnalyzer(data_path)
        
        print("DEBUG: Calculating Moving Average...")
        data = analyzer.calculate_moving_average(window=7)
        
        # Check if the SMA column was actually created
        print(f"DEBUG: Data shape: {data.shape}")
        print(f"DEBUG: Columns found: {data.columns.tolist()}")

        # 2. Check output directory
        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print("DEBUG: Created 'output' directory.")
        
        output_file = os.path.join(output_dir, 'trend_plot.png')
        
        print(f"DEBUG: Attempting to save plot to {output_file}...")
        plot_trends(data, output_file)
        
        print("DEBUG: Application finished.")
        
    except Exception as e:
        print(f"ERROR: Application crashed with error: {e}")

if __name__ == "__main__":
    main()