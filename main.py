import pprint as pp

import Config as cfg

import utils.AlphaVantageUtils as av


_LBL_TICKER = 'ticker'
_LBL_INTERVAL = 'interval'
_LBL_SIZE = 'size'


def get_prices(ticker, interval, size):

    prices = av.get_prices(cfg.AV_APIKEY, ticker, interval, size)

    return pp.pformat(prices.to_dict(), indent=4)


def process_request(request):

    request_json = request.get_json()

    if request.args and _LBL_TICKER in request.args:

        ticker = request.args.get(_LBL_TICKER)
        interval = request.args.get(_LBL_INTERVAL)
        size = request.args.get(_LBL_SIZE)

        return get_prices(ticker, interval, size)

    elif request_json and _LBL_TICKER in request_json:

        return 'In JSON section'
    else:
        return f'Hello World!'
