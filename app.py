from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calc")
def calc():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        result = a + b
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=5000)
     import os
     port = int(os.environ.get("PORT", 5000))
     app.run(host="0.0.0.0", port=port)