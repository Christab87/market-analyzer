import pandas as pd

class MarketAnalyzer:
    def __init__(self, file_path: str):
        self.df = pd.read_csv(file_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])

    def calculate_moving_average(self, window: int = 7):
        """Calculates simple moving average for closing price."""
        if 'Close' not in self.df.columns:
            raise ValueError("CSV must contain a 'Close' column")
        
        col_name = f'SMA_{window}'
        self.df[col_name] = self.df['Close'].rolling(window=window).mean()
        return self.df

    def get_summary(self):
        """Returns basic stats."""
        return self.df.describe()