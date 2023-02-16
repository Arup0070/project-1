from flask import Flask, Response,app
from housing.logger import logging
from housing.exception import HousingException
import sys
app= Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("We are trying to raise coustom exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
    logging.info("we are testing logging module")
    return "It is working Just Fine."

if __name__=="__main__":
    app.run(debug=True)