from flask import Flask, render_template, Response, Request, url_for

app = Flask(__name__)

"""
# night_color = "#222222"
# day_color = "#F1F1F1"
# header_night_color = "#333333"
# header_day_color = "#E1E1E1"
# night_text = "white"
# day_text = "black"

page_settings = {
	"bg_night_color": "#222222",
	"bg_day_color": "#F1F1F1",
	"header_night_color": "#333333",
	"header_day_color": "#E1E1E1",
	"text_night_color": "white",
	"text_day_color": "black"
}
"""

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/About")
def about():
	return "<center><h1>About</h1></center>"

@app.route("/Contact")
def contact():
	return "<center><h1>Contact</h1></center>"

@app.route("/Form")
def form():
	return "<center><h1>Form</h1></center>"

"""
@app.route("/results", methods=["GET", "POST"])
def results():
	return render_template("results.html")
"""

if __name__ == "__main__":
	app.run(debug = True)