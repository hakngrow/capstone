import pandas as pd

import datetime

import Config as cfg

import utils.AlphaVantageUtils as av
import utils.PostgresUtils as pg
import utils.PriceUpdater as pu

_PARAM_FUNC = 'func'

_VAL_GET_PRICES = 'get_prices'
_VAL_UPDATE_PRICES = 'update_prices'

_VAL_GET_ALL_SYMBOLS = 'get_all_symbols'
_VAL_GET_SYMBOL = 'get_symbol'

_PARAM_TICKER = 'ticker'
_PARAM_INTERVAL = 'interval'
_PARAM_SIZE = 'size'


def get_all_symbols():

    symbols = pg.get_symbols()

    if symbols is None:
        return 'No symbols found!'
    else:
        df = pd.DataFrame(symbols, columns=[pg._COL_NAME, pg._COL_TICKER])

        print(df.info())

        return df.to_html()


def get_symbol(ticker):

    if ticker is None:
        return 'Missing parameter: ticker'

    name = pg.get_symbol_name(ticker)

    if name is None:
        return f'Symbol with ticker {ticker} NOT found!'
    else:
        return name[0]


def get_prices(ticker, interval, size):

    if ticker is None:
        return 'Missing parameter: ticker'

    if interval is None:
        return 'Missing parameter: interval'

    if size is None:
        return 'Missing parameter: size'

    prices = av.get_prices(cfg.AV_APIKEY, ticker, interval, size)

    return prices.to_html()


def update_prices(ticker, interval, size):

    created, duplicates = pu.update_price(ticker, interval, size)

    return f'{ticker} ({interval}) : {str(created)} created, {str(duplicates)} duplicates'


def process_request(request):

    request_json = request.get_json()

    if request.args and _PARAM_FUNC in request.args:

        func = request.args.get(_PARAM_FUNC)

        print(f'Function detected: {str(func)}')

        ticker = request.args.get(_PARAM_TICKER)
        interval = request.args.get(_PARAM_INTERVAL)
        size = request.args.get(_PARAM_SIZE)

        print(f'Parameters detected: ticker={str(ticker)}, interval={str(interval)}, size={str(size)}')

        if func == _VAL_GET_ALL_SYMBOLS:
            return get_all_symbols()

        elif func == _VAL_GET_SYMBOL:
            return get_symbol(ticker)

        elif func == _VAL_GET_PRICES:
            return get_prices(ticker, interval, size)

        elif func == _VAL_UPDATE_PRICES:
            return update_prices(ticker, interval, size)
        else:
            return f'Unknown function: {str(func)}'

    else:

        return f'capsTone version 1.0 built {str(datetime.datetime.now().timestamp())}'
