import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Tạo dữ liệu giả cho dự báo doanh số
def generate_dummy_trend_data(num_records):
    np.random.seed(1)
    data = {
        "TrendID": range(1, num_records + 1),
        "ProductGroupID": np.random.randint(1, 10, num_records),
        "TrendDescription": [f"Trend {i}" for i in range(1, num_records + 1)],
        "StartDate": pd.date_range(start="1/1/2023", periods=num_records, freq='M').strftime("%m/%d/%Y"),
        "EndDate": pd.date_range(start="1/1/2024", periods=num_records, freq='M').strftime("%m/%d/%Y"),
        "Region": np.random.choice(["North", "South", "East", "West"], num_records),
        "SalesForecast": np.random.randint(50000, 150000, num_records),
        "CompetitorAnalysis": np.random.choice(["Competitive", "Non-competitive"], num_records),
        "MarketGrowthRate": np.random.uniform(0.01, 0.1, num_records),
        "CustomerSentiment": np.random.choice(["Positive", "Neutral", "Negative"], num_records),
        "TrendScore": np.random.randint(1, 10, num_records)
    }
    return pd.DataFrame(data)

# Tạo thêm 1000 dòng dữ liệu
df_trends_extended = generate_dummy_trend_data(1000)

# Lưu DataFrame vào file CSV
trend_output_path = "MarketTrend.csv"
df_trends_extended.to_csv(trend_output_path, index=False)

print(f"Dữ liệu đã được lưu vào {trend_output_path}")
