import utils.AlphaVantageUtils as av


def get_prices(request):

    request_json = request.get_json()

    if request.args and 'ticker' in request.args:
        
        ticker = request.args.get('ticker')
        interval = request.args.get('ticker')

        prices = av.get_prices('4F9G7E51ZEMJ6L2B', ticker, interval, av._SIZE_COMPACT )

        return prices

    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'