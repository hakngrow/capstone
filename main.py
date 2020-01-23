import pandas as pd

import Config as cfg

import utils.AlphaVantageUtils as av
import utils.PostgresUtils as pg
import utils.PriceUpdater as pu

_LBL_FUNC = 'func'

_VAL_GET_PRICES = 'get_prices'
_VAL_UPDATE_PRICES = 'update_prices'

_VAL_GET_SYMBOLS = 'get_symbols'

_LBL_TICKER = 'ticker'
_LBL_INTERVAL = 'interval'
_LBL_SIZE = 'size'


def get_all_symbols():

    return pd.DataFrame(pg.get_symbols()).to_html()


def get_prices(ticker, interval, size):

    prices = av.get_prices(cfg.AV_APIKEY, ticker, interval, size)

    return prices.to_html()


def update_prices(ticker, interval, size):

    created, duplicates = pu.update_price(ticker, interval, size)

    return ticker + ' ' + interval + ': ' + created + ' created, ' + duplicates + ' duplicates'


def process_request(request):

    request_json = request.get_json()

    if request.args and _LBL_FUNC in request.args:

        func = request.args.get(_LBL_FUNC)

        ticker = request.args.get(_LBL_TICKER)
        interval = request.args.get(_LBL_INTERVAL)
        size = request.args.get(_LBL_SIZE)

        if func == _VAL_GET_SYMBOLS:
            get_all_symbols()

        elif func == _VAL_GET_PRICES:
            return get_prices(ticker, interval, size)

        elif func == _VAL_UPDATE_PRICES:
            return update_prices(ticker, interval, size)

    elif request_json and _LBL_TICKER in request_json:

        return 'In JSON section'
    else:
        return f'Hello World!'
