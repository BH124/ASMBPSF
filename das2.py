import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df_trends = pd.read_csv('MarketTrend.csv')

# Chuyển đổi cột StartDate thành định dạng datetime
df_trends['StartDate'] = pd.to_datetime(df_trends['StartDate'])

# Tạo biểu đồ khu vực
plt.figure(figsize=(12, 6))

# Tạo biểu đồ khu vực cho từng vùng
for region in df_trends['Region'].unique():
    subset = df_trends[df_trends['Region'] == region]
    plt.fill_between(subset['StartDate'], subset['SalesForecast'], label=region, alpha=0.5)

plt.xlabel('Start Date')
plt.ylabel('Sales Forecast')
plt.title('Sales Forecast by Region')
plt.legend()
plt.grid(True)
plt.show()