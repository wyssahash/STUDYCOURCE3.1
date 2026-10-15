from flask import Flask, render_template, url_for, request, redirect
import mysql.connector
app = Flask(__name__)
    

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password",
        database="sports_inventory",
        port=3306
    )


@app.route("/equipment")
def equipment():
    conn = get_db_connection()

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT
                e.equipment_id,
                e.name,
                c.name AS category,
                e.quantity,
                e.condition_status,
                e.price
            FROM equipment AS e
            JOIN categories AS c
                ON e.category_id = c.category_id
            ORDER BY e.equipment_id
        """)

        items = cursor.fetchall()
        return render_template("equipment.html", items=items)

    finally:
        cursor.close()
        conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")  


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001, debug=True)