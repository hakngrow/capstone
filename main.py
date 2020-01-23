import Config as cfg

import utils.AlphaVantageUtils as av


def get_prices(request):

    return type(request)

    '''
    request_json = request.get_json()

    if request.args and 'ticker' in request.args:

        ticker = request.args.get('ticker')
        interval = request.args.get('interval')

        print(ticker, interval)

        #prices = av.get_prices(cfg.AV_APIKEY, ticker, interval, av._SIZE_COMPACT )

        return ticker, interval

    elif request_json and 'ticker' in request_json:

        ticker = request_json['ticker']
        interval = request_json['interval']

        print(ticker, interval)

        #prices = av.get_prices(cfg.AV_APIKEY, ticker, interval, av._SIZE_COMPACT )

        return ticker, interval
    else:
        return f'Hello World!'
    '''