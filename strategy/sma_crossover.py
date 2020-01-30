from pyalgotrade.strategy import BacktestingStrategy

from pyalgotrade.technical import ma
from pyalgotrade.technical import cross

class SMACrossOver(BacktestingStrategy):

    def __init__(self, feed, instrument, sma_period):

        super(SMACrossOver, self).__init__(feed)

        self.__instrument = instrument
        self.__position = None

        self.setUseAdjustedValues(False)

        self.__prices = feed[instrument].getPriceDataSeries()

        print(self.__prices)

        self.__sma = ma.SMA(self.__prices, sma_period)

    def getSMA(self):
        return self.__sma

    def onEnterCanceled(self, position):
        self.__position = None

    def onExitOk(self, position):
        self.__position = None

    def onExitCanceled(self, position):

        # If the exit was canceled, re-submit it.
        self.__position.exitMarket()

    def onBars(self, bars):

        # If a position was not opened, check if should enter a long position.
        if self.__position is None:

            if cross.cross_above(self.__prices, self.__sma) > 0:

                shares = int(self.getBroker().getCash() * 0.9 / bars[self.__instrument].getPrice())

                # Enter a buy market order. The order is good till canceled.
                self.__position = self.enterLong(self.__instrument, shares, True)

        # Check if we have to exit the position.
        elif not self.__position.exitActive() and cross.cross_below(self.__prices, self.__sma) > 0:
            self.__position.exitMarket()