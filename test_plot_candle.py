import pandas as pd
import mplfinance as mpf

df = pd.read_csv('BTC-USD.csv')
df.Date =  pd.to_datetime(df.Date)

df = df.set_index('Date')
# df.loc['2021-05-06']

# mpf.plot(df)

# mpf.plot(df,type='line',volume=True)
# mpf.plot(df['2021-04'],type='line',volume=True)
# mpf.plot(df['2021-04'],volume=True)
# mpf.plot(df['2021-04'],type='candle',volume=True)


# mpf.plot(df['2021-01':'2021-04'],type='candle',mav=(20),volume=True,tight_layout = True)
mpf.plot(df['2021-01':'2021-04'],type='candle',mav=(20),volume=True,tight_layout = True,savefig='image.png')