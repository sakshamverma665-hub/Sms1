from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ORIGINAL_API = "https://api.selfunit.in/SMS/api.php"

@app.route("/get", methods=["GET"])
def proxy():
    params = request.args.to_dict()

    try:
        resp = requests.get(ORIGINAL_API, params=params, timeout=15)
        resp.raise_for_status()
    except requests.RequestException as e:
        return jsonify({"error": str(e), "owner": "@Saksham24_11"}), 502

    try:
        data = resp.json()
    except ValueError:
        data = {"response": resp.text}

    # Remove unwanted field
    if "by" in data and data["by"] == "@jatinbro69":
        del data["by"]

    # Add owner
    data["owner"] = "@Saksham24_11"
    return jsonify(data)
