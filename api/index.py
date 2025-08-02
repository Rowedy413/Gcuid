from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__, template_folder="../templates")

GRAPH_API_URL = "https://graph.facebook.com/v18.0"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        access_token = request.form.get('token')

        if not access_token:
            return render_template("index.html", error="Token is required")

        url = f"{GRAPH_API_URL}/me/conversations?fields=id,name&access_token={access_token}"

        try:
            response = requests.get(url)
            data = response.json()

            if "data" in data:
                return render_template("index.html", groups=data["data"])
            else:
                return render_template("index.html", error="Invalid token or no Messenger groups found")
        except:
            return render_template("index.html", error="Something went wrong")

    return render_template("index.html")
