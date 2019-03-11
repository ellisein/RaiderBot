from datetime import datetime

import matplotlib
matplotlib.use("Agg")

import seaborn
seaborn.set_style("darkgrid")


GRAPH_COLOR = "indianred"
GRAPH_FILENAME = "token.png"

class TokenGraph:
    def __init__(self):
        self._fig = matplotlib.pyplot.figure(figsize=(8,4))
        self._ax = self._fig.add_subplot(1, 1, 1)
        #self._ax.set_ylim([200000, 300000])
        self.clear()

    def add(self, time, price):
        self._data_x.append(time)
        self._data_y.append(price)

    def clear(self):
        self._data_x = list()
        self._data_y = list()

    def save(self):
        _data_x_converted = matplotlib.dates.date2num(self._data_x)
        self._ax.clear()
        self._ax.plot_date(_data_x_converted, self._data_y,
                           linestyle="solid", marker=None, color=GRAPH_COLOR)
        matplotlib.pyplot.xticks(rotation=70)
        self._fig.savefig(GRAPH_FILENAME, bbox_inches="tight")


DATA_FILENAME = "token.db"

class TokenData:
    def __init__(self):
        pass

    def write(self, timestamp, price):
        with open(DATA_FILENAME, "a+") as f:
            f.write("{} {}\n".format(timestamp, price))

    def read(self, num=None):
        with open(DATA_FILENAME, "r") as f:
            data = f.readlines()
        if len(data) == 0:
            return None
        if num:
            data = data[-num:]
        converted = list()
        for d in data:
            s = d.split(" ")
            converted.append({"time": datetime.fromtimestamp(int(s[0])),
                              "price": int(s[1])})
        return converted
