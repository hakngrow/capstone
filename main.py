import Config as cfg

import utils.AlphaVantageUtils as av


_LBL_TICKER = 'ticker'
_LBL_INTERVAL = 'interval'


def get_prices(ticker, interval):

    prices = av.get_prices(cfg.AV_APIKEY, ticker, interval, av._SIZE_COMPACT)

    return prices.to_json()

def execute_request(request):

    request_json = request.get_json()

    if request.args and _LBL_TICKER in request.args:

        ticker = request.args.get(_LBL_TICKER)
        interval = request.args.get(_LBL_INTERVAL)

        return get_prices(ticker, interval)

    elif request_json and _LBL_TICKER in request_json:

        ticker = request.args.get(_LBL_TICKER)
        interval = request.args.get(_LBL_INTERVAL)

        return 'In JSON section'
    else:
        return f'Hello World!'
