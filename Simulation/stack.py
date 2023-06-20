import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta

def create_df():
    # CSVファイルのパス
    csv_file = 'data.csv'

    # CSVファイルを読み込む
    df = pd.read_csv(csv_file)

    # 日付をdatetime型に変換する
    df['date_start'] = pd.to_datetime(df['date_start'])
    df['date_end'] = pd.to_datetime(df['date_end'])
    df['date_dup'] = pd.to_datetime(df['date_dup'])

    # 1/1から2/10までの期間を行、aからcを列にしたデータフレームを作成する
    date_range = pd.date_range(start='2023/1/1', end='2023/2/10')
    categories = ['a', 'b', 'c']
    df_total = pd.DataFrame(0, index=date_range, columns=categories)

    # amountを計算する
    for index, row in df.iterrows():
        start_date = row['date_start']
        end_date = row['date_end']
        dup_date = row['date_dup']
        amount = row['amount']
        category = row['category']
        
        # date_startからdate_endまでの期間はamountを加算
        df_total.loc[start_date:dup_date - timedelta(days=1), category] += amount
        
        # date_dupの期間はamountを2倍にして加算
        df_total.loc[dup_date:end_date, category] += amount * 2

    return df_total
# 日付ごとのamountの総計を計算

# 積み上げ面グラフを作成
# df_total.plot(kind='area', stacked=True)
# plt.xlabel('Date')
# plt.ylabel('Total Amount')
# plt.title('Stacked Area Graph')
# plt.legend()
# plt.xticks(rotation=45)
# plt.show()
