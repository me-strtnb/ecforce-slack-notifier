from flask import Flask, request
import requests

app = Flask(__name__)

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

@app.route("/ecforce-webhook", methods=["POST"])
def ecforce_webhook():
    data = request.json

    order_id = data.get("order_id", "不明")
    name = data.get("customer_name", "不明")
    amount = data.get("total_price", "不明")

    text = f":tada: 新しい注文！\n・顧客名: {name}\n・注文ID: {order_id}\n・金額: {amount}円"

    requests.post(SLACK_WEBHOOK_URL, json={"text": text})
    return "", 200

if __name__ == "__main__":
    app.run(port=8080)