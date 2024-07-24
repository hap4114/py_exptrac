from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

# Define your database model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100))
    amount = db.Column(db.Float)

# Create database tables within the application context
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_expense():
    category = request.form['category']
    amount = float(request.form['amount'])

    new_expense = Expense(category=category, amount=amount)
    db.session.add(new_expense)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/list')
def list_expenses():
    expenses = Expense.query.all()
    return render_template('expenses.html', expenses=expenses)

@app.route('/data')
def get_data():
    expenses = Expense.query.with_entities(Expense.category, db.func.sum(Expense.amount)).group_by(Expense.category).all()

    labels = [category for category, _ in expenses]
    values = [float(amount) for _, amount in expenses]

    return jsonify({'labels': labels, 'values': values})

if __name__ == '__main__':
    app.run(debug=True)
