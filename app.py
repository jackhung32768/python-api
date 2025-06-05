from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calc")
def calc():
    try:
        print("a=",a)
        print("b=",b)
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        result = a + b
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/convert_between_celsius_and_fahrenheit")
def convert_between_celsius_and_fahrenheit():
    try:
        celsius = request.args.get("celsius")
        fahrenheit = request.args.get("fahrenheit")

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
        
if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=5000)
     import os
     port = int(os.environ.get("PORT", 5000))
     app.run(host="0.0.0.0", port=port)