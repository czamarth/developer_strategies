import os

from flask import Flask, jsonify

from strategy import Strategy

dirpath = os.path.dirname(__file__)
devpath = os.path.join(dirpath, 'developer_strategies.txt')

app = Flask(__name__)
app.debug = False
strategy = Strategy(devpath)


@app.route('/')
def root():
    return jsonify(strategy=strategy.get_strategy())


if __name__ == '__main__':
    app.run()
