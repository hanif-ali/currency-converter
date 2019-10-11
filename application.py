import requests
from flask import Flask, render_template, request
app = Flask(__name__)

cl_api_key = "c31d3624ef4dfb9dfcb2dd41fe81c694"

currencies = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 
'BBD','BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 
'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 
'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 
'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 
'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 
'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 
'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 
'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 
'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 
'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 
'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 
'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 
'ZWL']


def find_rate(source_rate, target_rate):
    return target_rate/source_rate


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", currencies=currencies)


@app.route("/convert", methods=["POST"])
def convert():
    target = request.form.get("target")
    amount = request.form.get("amount")
    source = request.form.get("source")

    results = {"success": False}

    if target and amount and source:
        api_url = "http://data.fixer.io/api/latest"

        params_source = {"access_key": cl_api_key, "symbols":source, "base": "EUR"}
        params_target = {"access_key": cl_api_key, "symbols":target, "base": "EUR"}

        data_source = requests.get(api_url, params_source).json() 
        data_target = requests.get(api_url, params_target).json() 

        if data_source["success"] and data_target["success"]:
            source_rate = data_source["rates"][source]
            target_rate = data_target["rates"][target]
            

            rate = find_rate(source_rate, target_rate)

            target_amount = rate*float(amount)

            results["success"] = True
            results["amount"] = amount
            results["target_amount"] = target_amount
            results["target"] = target
            results["rate"] = rate
            results["source"] = source

    return results            