"""
prediction_pipeline.py
-------------------------
Yeh file FLASK APP use karega - jab user koi data submit kare
(jaise "is customer ka CLV predict karo"), yeh file:
    1. Saved model (.pkl) load karega
    2. Input data ko sahi format/scaling mein convert karega
    3. Prediction return karega

training_pipeline.py "model BANANE" ke liye hai,
prediction_pipeline.py "ban chuke model SE PREDICT karne" ke liye hai -
yeh dono ALAG concerns hain (Training Time vs Inference/Serving Time).

Har tier ke liye yahan ek class/function hogi:
    - predict_clv(input_data)
    - predict_churn(input_data)
    - get_customer_segment(input_data)
"""
