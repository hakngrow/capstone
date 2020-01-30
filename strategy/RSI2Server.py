import itertools

from pyalgotrade.optimizer import server
from pyalgotrade.barfeed import yahoofeed

import utils.AlphaVantageUtils as av

def parameters_generator():

    instrument = [av._TIC_APPLE]
    entrySMA = range(40, 45)
    exitSMA = range(20, 25)
    rsiPeriod = range(10, 15)
    overBoughtThreshold = range(70, 71)
    overSoldThreshold = range(30, 31)

    return itertools.product(instrument, entrySMA, exitSMA, rsiPeriod, overBoughtThreshold, overSoldThreshold)


if __name__ == '__main__':

    # Load the bar feed from the CSV files.
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV(av._TIC_APPLE, "AAPL.csv")

    # Run the server.
    server.serve(feed, parameters_generator(), "localhost", 5000)