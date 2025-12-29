from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask
app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")  # Your downloaded key
firebase_admin.initialize_app(cred)
db = firestore.client()

# Login route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for('dashboard'))
    return render_template("login.html")

# Dashboard route
@app.route("/dashboard")
def dashboard():
    employees = db.collection("employees").stream()
    return render_template("dashboard.html", employees=employees)

# Add Employee route
@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        name = request.form["name"]
        role = request.form["role"]
        db.collection("employees").add({
            "name": name,
            "role": role
        })
        return redirect(url_for('dashboard'))
    return render_template("add_employee.html")

# Run Flask
if __name__ == "__main__":
    app.run(debug=True)
