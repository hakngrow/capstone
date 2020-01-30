from pyalgotrade.barfeed import yahoofeed

from pyalgotrade import plotter

from pyalgotrade.stratanalyzer.returns import Returns
from pyalgotrade.stratanalyzer.sharpe import SharpeRatio
from pyalgotrade.stratanalyzer.drawdown import DrawDown
from pyalgotrade.stratanalyzer.trades import Trades

from strategy import sma_crossover

_PARAM_TICKER = 'PG'
_PARAM_FILENAME = 'PG-1y.csv'
_PARAM_SMA_PERIODS = 20

# Load the bar feed from the CSV file
feed = yahoofeed.Feed()
feed.addBarsFromCSV(_PARAM_TICKER, _PARAM_FILENAME)

# Evaluate the strategy with the feed's bars.
strategy = sma_crossover.SMACrossOver(feed, _PARAM_TICKER, _PARAM_SMA_PERIODS)

# Attach returns analyzer to the strategy
analyzer_returns = Returns()
strategy.attachAnalyzer(analyzer_returns)

# Attach Sharpe Ratio analyzer to the strategy
analyzer_sharpe = SharpeRatio()
strategy.attachAnalyzer(analyzer_sharpe)

# Attach Draw Down analyzer to the strategy
analyzer_drawDown = DrawDown()
strategy.attachAnalyzer(analyzer_drawDown)

# Attach Trades analyzer to the strategy
analyzer_trades = Trades()
strategy.attachAnalyzer(analyzer_trades)

# Attach the plotter to the strategy.
pltr = plotter.StrategyPlotter(strategy)

# Include the SMA in the instrument subplot to get it displayed along with the closing prices.
pltr.getInstrumentSubplot(_PARAM_TICKER).addDataSeries(f'SMA {_PARAM_SMA_PERIODS}', strategy.getSMA())

# Plot the simple returns on each bar.
pltr.getOrCreateSubplot('returns').addDataSeries('Simple Returns', analyzer_returns.getReturns())

# Run the strategy.
strategy.run()
strategy.info('Final portfolio value: $%.2f' % strategy.getResult())

print('Final portfolio value: $%.2f' % strategy.getResult())

print('Cumulative returns: %.2f %%' % (analyzer_returns.getCumulativeReturns()[-1] * 100))
print('Sharpe ratio: %.2f' % (analyzer_sharpe.getSharpeRatio(0.05)))
print('Max. drawdown: %.2f %%' % (analyzer_drawDown.getMaxDrawDown() * 100))

print('')
print('Total trades: %d' % (analyzer_trades.getCount()))
if analyzer_trades.getCount() > 0:
    profits = analyzer_trades.getAll()
    print('Avg. profit: $%2.f' % (profits.mean()))
    print('Profits std. dev.: $%2.f' % (profits.std()))
    print('Max. profit: $%2.f' % (profits.max()))
    print('Min. profit: $%2.f' % (profits.min()))
    returns = analyzer_trades.getAllReturns()
    print('Avg. return: %2.f %%' % (returns.mean() * 100))
    print('Returns std. dev.: %2.f %%' % (returns.std() * 100))
    print('Max. return: %2.f %%' % (returns.max() * 100))
    print('Min. return: %2.f %%' % (returns.min() * 100))

print('')
print('Profitable trades: %d' % (analyzer_trades.getProfitableCount()))
if analyzer_trades.getProfitableCount() > 0:
    profits = analyzer_trades.getProfits()
    print('Avg. profit: $%2.f' % (profits.mean()))
    print('Profits std. dev.: $%2.f' % (profits.std()))
    print('Max. profit: $%2.f' % (profits.max()))
    print('Min. profit: $%2.f' % (profits.min()))
    returns = analyzer_trades.getPositiveReturns()
    print('Avg. return: %2.f %%' % (returns.mean() * 100))
    print('Returns std. dev.: %2.f %%' % (returns.std() * 100))
    print('Max. return: %2.f %%' % (returns.max() * 100))
    print('Min. return: %2.f %%' % (returns.min() * 100))

print('')
print('Unprofitable trades: %d' % (analyzer_trades.getUnprofitableCount()))
if analyzer_trades.getUnprofitableCount() > 0:
    losses = analyzer_trades.getLosses()
    print('Avg. loss: $%2.f' % (losses.mean()))
    print('Losses std. dev.: $%2.f' % (losses.std()))
    print('Max. loss: $%2.f' % (losses.min()))
    print('Min. loss: $%2.f' % (losses.max()))
    returns = analyzer_trades.getNegativeReturns()
    print('Avg. return: %2.f %%' % (returns.mean() * 100))
    print('Returns std. dev.: %2.f %%' % (returns.std() * 100))
    print('Max. return: %2.f %%' % (returns.max() * 100))
    print('Min. return: %2.f %%' % (returns.min() * 100))

# Plot the strategy.
pltr.plot()