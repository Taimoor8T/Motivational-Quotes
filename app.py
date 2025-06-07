from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Do not wait to strike till the iron is hot, but make it hot by striking.",
    "The best way to predict the future is to create it.",
    "At the top of the mountain but we are really only halfway up.",
    "The only way to do great work is to love what you do.",
]
@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        new_quote =request.form.get("quote")
        if new_quote:
            quotes.append(new_quote)
        return redirect('/')
        
    random_quote =random.choice(quotes)
    return render_template("index.html", quote=random_quote)
if __name__ == '__main__':
    print("Starting the Flask server...")
    app.run(debug=True)