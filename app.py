from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello_world():
    if request.method == "GET":
       return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not username or not password:
            error = "KullanÄ±cÄ± adÄ± yada ÅŸifre boÅŸ olamaz.."
            return render_template("login.html", error=error)
        if username == "mendebur" and password == "taklaci_guvercin_34":
            return send_from_directory("uploads/", "world2.zip")
        else:
            error = "KullanÄ±cÄ± adÄ± yada ÅŸifre yanlÄ±ÅŸ.."
            return render_template("login.html", error=error)
