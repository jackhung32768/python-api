from flask import Flask, request, jsonify

import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/calc")
def calc():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        logging.info(f"a = {a}")
        logging.info(f"b = {b}")
        result = a + b
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/convert_between_celsius_and_fahrenheit")
def convert_between_celsius_and_fahrenheit():
    try:
        celsius = request.args.get("celsius")
        fahrenheit = request.args.get("fahrenheit")
        logging.info(f"celsius = {celsius}")
        logging.info(f"fahrenheit = {fahrenheit}")

        if celsius:
            f = float(celsius) * 9 / 5 + 32
            return jsonify({"fahrenheit": f})
        elif fahrenheit:
            c = (float(fahrenheit) - 32) * 5 / 9
            return jsonify({"celsius": c})
        else:
            return jsonify({"error": "請提供 celsius 或 fahrenheit"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/convert_between_inch_and_cm")
def convert_between_inch_and_cm():
    try:
        inch = request.args.get("inch")
        cm = request.args.get("cm")
        logging.info(f"inch = {inch}")
        logging.info(f"cm = {cm}")

        if inch:
            cm_val = float(inch) * 2.54
            return jsonify({"cm": cm_val})
        elif cm:
            inch_val = float(cm) / 2.54
            return jsonify({"inch": inch_val})
        else:
            return jsonify({"error": "請提供 inch 或 cm"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/convert_between_mile_and_km")
def convert_between_mile_and_km():
    try:
        mile = request.args.get("mile")
        km = request.args.get("km")
        logging.info(f"mile = {mile}")
        logging.info(f"km = {km}")

        if mile:
            km_val = float(mile) * 1.60934
            return jsonify({"km": km_val})
        elif km:
            mile_val = float(km) / 1.60934
            return jsonify({"mile": mile_val})
        else:
            return jsonify({"error": "請提供 mile 或 km"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400
        
        
if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=5000)
     import os
     port = int(os.environ.get("PORT", 5000))
     app.run(host="0.0.0.0", port=port)