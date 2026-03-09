import pytest
import pandas as pd
from src.analyzer import MarketAnalyzer

def test_moving_average():
    # Setup dummy data
    data = {'Date': ['2023-01-01', '2023-01-02'], 'Close': [100, 110]}
    pd.DataFrame(data).to_csv('temp.csv', index=False)
    
    analyzer = MarketAnalyzer('temp.csv')
    df = analyzer.calculate_moving_average(window=2)
    
    assert 'SMA_2' in df.columns
    # The SMA of 100 and 110 is 105
    assert df['SMA_2'].iloc[1] == 105.0