from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, PayPal!"

@app.route('/payment/execute', methods=['GET'])
def payment_execute():
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')

    # Here you would execute the payment using PayPal SDK
    # Example:
    # payment = paypalrestsdk.Payment.find(payment_id)
    # if payment.execute({"payer_id": payer_id}):
    #     return jsonify({"status": "Payment executed successfully"})
    # else:
    #     return jsonify({"status": "Payment execution failed"})

    return "Payment Executed"

@app.route('/payment/cancel', methods=['GET'])
def payment_cancel():
    return "Payment Canceled"

if __name__ == '__main__':
    app.run(debug=True)
