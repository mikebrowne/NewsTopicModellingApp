from flask import Flask, render_template, request, jsonify, Response
#from data_collection import scrape
from BackEnd.main import BackEndInterface
import datetime as dt
import sys

app = Flask(__name__)

back_end_interface = BackEndInterface()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/response', methods=["POST"])
def response():
    company_name = request.form.get("company-name")
    ticker = request.form.get("ticker")
    date = request.form.get("date").split("-")
    date = dt.datetime(int(date[0]), int(date[1]), int(date[2]))

    data = back_end_interface.get(company_name, ticker, date)

    if data is not None:
        return render_template('index.html', data_=data)
    else:
        return render_template('index.html', null = True)


if __name__ == '__main__':
    app.run()