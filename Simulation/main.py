import pandas as pd
from datetime import timedelta
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def generate_stacked_graph():
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

@app.route('/')
def index():
    df = generate_stacked_graph()
    chart_data = []
    for column in df.columns:
        chart_data.append({
            'label': column,
            'data': df[column].tolist()
        })

    return render_template('home.html', chart_data=chart_data)

@app.route('/api/data')
def api_data():
    df = generate_stacked_graph()
    chart_data = []
    for column in df.columns:
        chart_data.append({
            'label': column,
            'data': df[column].tolist()
        })

    return jsonify(chart_data)

if __name__ == '__main__':
    app.run(debug=True)
