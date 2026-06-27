"""
app.py
--------
FLASK APPLICATION entry point - yeh file chalane se web server start
hota hai.

Yahan hum:
    1. Flask app initialize karenge
    2. Har tier ke routes register karenge (Blueprints use karke -
       jaise clv_routes, churn_routes, segment_routes)
    3. app.run() se server start karenge

Structure (jab banayenge):
    from flask import Flask
    from customer_intelligence_suite.pipeline.prediction_pipeline import ...

    app = Flask(__name__)

    @app.route("/predict/clv", methods=["POST"])
    def predict_clv():
        ...

    @app.route("/predict/churn", methods=["POST"])
    def predict_churn():
        ...

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)
"""
