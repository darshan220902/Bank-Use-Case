from flask import Flask, render_template, request

app = Flask(__name__)

class Bank:
    def __init__(self, c_name, c_pin, c_balance):
        self.c_name = c_name
        self.c_pin = c_pin
        self.c_balance = c_balance

    def withdraw(self, amount, entered_pin):
        if entered_pin == self.c_pin:
            withdraw_amount = min(amount, self.c_balance)
            self.c_balance -= withdraw_amount
            return f"Withdrawn {withdraw_amount}. New balance: {self.c_balance}"
        else:
            return "Invalid PIN"

    def check_balance(self, entered_pin):
        if entered_pin == self.c_pin:
            return f"Current balance: {self.c_balance}"
        else:
            return "Invalid PIN"

    def deposit_balance(self, amount):
        self.c_balance += amount
        return f"Deposited {amount}. New balance: {self.c_balance}"


customer_bank = Bank("darshan", 123, 7000)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = int(request.form['amount'])
    pin = int(request.form['pin'])
    result = customer_bank.withdraw(amount, pin)
    return render_template('result.html', result=result)

@app.route('/check_balance', methods=['POST'])
def check_balance():
    pin = int(request.form['pin'])
    result = customer_bank.check_balance(pin)
    return render_template('result.html', result=result)

@app.route('/deposit', methods=['POST'])
def deposit():
    amount = int(request.form['amount'])
    result = customer_bank.deposit_balance(amount)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
