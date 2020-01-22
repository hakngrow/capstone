import utils.Config as cfg

import utils.AlphaVantageUtils as av
import utils.PostgresUtils as pg


def update_price(ticker, interval, size):

    df_prices = av.get_prices(cfg.AV_APIKEY, ticker, interval, size)

    for i in range(0, len(df_prices)):

        if not pg.is_price_duplicate(ticker, interval, df_prices[pg._COL_DATETIME][i]):
            pg.create_prices([df_prices.iloc[i, :].values])
        else:
            print('Duplicate ' + ticker + ' price on ' + str(df_prices[pg._COL_DATETIME][i]))


update_price(av._TIC_MICROSOFT, av._INT_DAILY, av._SIZE_FULL)
