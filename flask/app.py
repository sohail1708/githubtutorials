from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/form", methods=["GET", "POST"])
def form_contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        return f"Thank you {name} for your message: {message}. We will contact you at {email}."
    return render_template("form.html")

@app.route("/success/<int:score>")
def success(score):
    if score >=50:
        result = "Congratulations! You passed the exam. Good job bro!! you should come again"
    else:
        result = "Sorry, you failed the exam. Better luck next time"
    return render_template("/success.html", result=result)

@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
