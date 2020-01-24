import utils.AlphaVantageUtils as av
import utils.PostgresUtils as pg

import model.FeatureEngineer as fe


def update_date_features(ticker, interval):

    dates = pg.get_price_dates(ticker, interval)

    features_array = []

    for i in range(0, len(dates)):

        if pg.get_features(ticker, interval, dates[i[1]]) is None:

            features = fe.get_date_features(dates[i][1])

            features_array.append([dates[i][0], \
                                   features[0], features[1], features[2], \
                                   features[3], features[4], features[5], \
                                   int(features[6][0]), int(features[6][1]), int(features[7][0]), int(features[7][1]), \
                                   int(features[8][0]), int(features[8][1]), int(features[9][0]), int(features[9][0])])

    pg.create_features(features_array)


update_date_features(av._TIC_MICROSOFT, av._INT_DAILY)
