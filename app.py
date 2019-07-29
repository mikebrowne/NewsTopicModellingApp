from flask import Flask, render_template, request, jsonify, Response
#from data_collection import scrape
from BackEnd.DataCollection.business_wire_scraper import test_function

app = Flask(__name__)

# Add a single endpoint that we can use for testing
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Add scrape button
@app.route('/response', methods=["POST"])
def response():
    data = test_function()

    if data is not None:
        return render_template('index.html', data_=data)
    else:
        return render_template('index.html', null=True)


if __name__ == '__main__':
    app.run()