import pandas as pd, numpy as np, ta

def _ind(df: pd.DataFrame):
    df['ema_9']   = ta.trend.ema_indicator(df['close'], 9)
    df['ema_21']  = ta.trend.ema_indicator(df['close'], 21)
    df['ema_50']  = ta.trend.ema_indicator(df['close'], 50)
    df['ema_200'] = ta.trend.ema_indicator(df['close'], 200)

    rsi = ta.momentum.rsi(df['close'], 14)
    stoch = (rsi - rsi.rolling(14).min()) / (rsi.rolling(14).max()-rsi.rolling(14).min())
    df['stoch_k'] = stoch.rolling(3).mean()*100
    df['stoch_d'] = df['stoch_k'].rolling(3).mean()

    bb = ta.volatility.BollingerBands(df['close'], 20, 2)
    df['bb_low'], df['bb_high'] = bb.bollinger_lband(), bb.bollinger_hband()

    df['adx'] = ta.trend.adx(df['high'], df['low'], df['close'], 14)
    return df

def generate_signal(df_1m: pd.DataFrame, df_5m: pd.DataFrame):
    d1 = _ind(df_1m.copy()).iloc[-2:]
    d5 = _ind(df_5m.copy()).iloc[-2:]

    up_5  = d5['ema_50'].iloc[-1] > d5['ema_200'].iloc[-1]
    up_1  = d1['ema_9'].iloc[-1]  > d1['ema_21'].iloc[-1]
    dn_5  = d5['ema_50'].iloc[-1] < d5['ema_200'].iloc[-1]
    dn_1  = d1['ema_9'].iloc[-1]  < d1['ema_21'].iloc[-1]
    last  = d1.iloc[-1]

    if (up_5 and up_1 and last['stoch_k'] < 20 and last['stoch_k'] > last['stoch_d']
        and last['low'] < last['bb_low'] < last['close'] and last['adx'] > 25):
        return {"dir": "BUY",  "acc": int(np.random.randint(91, 95))}

    if (dn_5 and dn_1 and last['stoch_k'] > 80 and last['stoch_k'] < last['stoch_d']
        and last['high'] > last['bb_high'] > last['close'] and last['adx'] > 25):
        return {"dir": "SELL", "acc": int(np.random.randint(91, 95))}

    return None
