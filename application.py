import requests
from flask import Flask, render_template, request
app = Flask(__name__)

cl_api_key = "c31d3624ef4dfb9dfcb2dd41fe81c694"

@app.route("/", methods=["GET", "POST"])
def index():
    target = request.form.get("target")
    amount = request.form.get("amount")
    source = request.form.get("source")
    results = {}

    if target and amount and source:
        api_url = "http://data.fixer.io/api/latest"
        params = {"access_key": cl_api_key, "symbols":target, "base": source}

        res = requests.get(api_url, params)
        if res.status_code != 200:
            return "Some Error"
        else:
            data = res.json()
            if data["success"]:
                rate = data["rates"][target]
                target_amount = rate*float(amount)
            else: 
                return "Some Error Occured"
        results["amount"] = amount
        results["target_amount"] = target_amount
        results["target"] = target
        results["rate"] = rate
        results["source"] = source


    return render_template("index.html", results = results)