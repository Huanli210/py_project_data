import random
import pandas as pd
from datetime import datetime, timedelta
# 隨機生成資料的函數
def generate_data(num_rows):
    data = []
    
    # 生成隨機日期，範圍從 2022-01-01 到 2023-6-30
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 6, 30)
    
    # 儲存每個帳號的貨幣對應關係
    account_currency_map = {}
    
    for _ in range(num_rows):
        # 隨機生成日期
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        date = start_date + timedelta(days=random_days)
        date_str = date.strftime('%Y/%m/%d')

        # 隨機生成帳號（假設帳號是 10 位字母數字）
        account = ''.join(random.choices('0123456789ABCDEF', k=10))
        
        # 確保帳號有一個固定的貨幣
        if account not in account_currency_map:
            account_currency_map[account] = random.choice(['CNY', 'HKD', 'JPY', 'KRW', 'TWD'])
        
        currency = account_currency_map[account]

        # 隨機生成轉蛋次數，現在最多 4000 次
        gacha_count = random.randint(1, 4000)

        # 隨機生成中獎次數，確保不超過轉蛋次數
        win_count = random.randint(0, gacha_count)

        # 計算中獎機率
        win_rate = f'{(win_count / gacha_count) * 100:.2f}%'

        # 隨機生成花費金額，範圍從 0 到 2,000,000
        cost = random.randint(0, 2000000)

        # 累積寶物總價
        total_value = random.randint(1000, 10000)
        
        # 把一行資料添加到列表中
        data.append([date_str, account, currency, gacha_count, win_count, win_rate, cost, total_value])
    return data

# 生成 20000 條隨機資料
data = generate_data(20000)

# 將資料轉換為 DataFrame
df = pd.DataFrame(data, columns=['日期', '帳號', '貨幣', '轉蛋次數', '中獎次數', '中獎機率', '花費金額', '累積寶物總價'])

# 儲存為 Excel 文件
df.to_excel('game_data.xlsx', index=False)

print("隨機資料已生成並儲存為 game_data.xlsx")
