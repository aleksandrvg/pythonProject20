from flask import Flask, render_template, request
app = Flask("flaskapp")

@app.route("/")
def HelloFlask():
    return "Главная"

@app.route("/form")
def About():
    return render_template('form.html')

@app.route("/submit", methods=['POST'])
def Submit():
    login = request.form["login"]
    password = request.form["password"]
    return render_template("submit.html", login=login, password=password)

if __name__ == "__main__":
    app.run(debug=True)
