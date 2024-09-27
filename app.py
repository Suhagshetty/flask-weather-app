from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual API key
API_KEY = "e3314a1fa9253c6916ea99386f4a23fc"


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"error": "City not found."}
    return render_template("index.html", weather_data=weather_data)


if __name__ == "__main__":
    app.run(debug=True)
