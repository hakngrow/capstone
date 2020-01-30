from pyalgotrade.optimizer import worker

from strategy import rsi2

if __name__ == '__main__':
    worker.run(rsi2.RSI2, "localhost", 5000, workerName="RSI2Worker")