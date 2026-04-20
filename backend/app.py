from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to connect

# Initialize Database
def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            description TEXT,
            amount REAL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Add Expense
@app.route('/add', methods=['POST'])
def add_expense():
    data = request.json

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (date, category, description, amount)
        VALUES (?, ?, ?, ?)
    """, (data['date'], data['category'], data['description'], data['amount']))

    conn.commit()
    conn.close()

    return jsonify({"message": "Expense added successfully"})

# Get All Expenses
@app.route('/get', methods=['GET'])
def get_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()

    expenses = []
    for row in rows:
        expenses.append({
            "id": row[0],
            "date": row[1],
            "category": row[2],
            "description": row[3],
            "amount": row[4]
        })

    return jsonify(expenses)

if __name__ == "__main__":
    app.run(debug=True)