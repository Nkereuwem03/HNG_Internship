from flask import Flask, request
from datetime import date, datetime
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Welcome<h1>"


@app.route('/api')
def api():
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")
    json_object = {'slack_name': slack_name,
                   'current_day': datetime.now().strftime('%A'),
                   'utc_time': datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                   'track': track,
                   'github_file_url': 'https://github.com/Nkereuwem03/HNG_Internship/blob/main/main.py',
                   'github_repo_url': 'https://github.com/Nkereuwem03/HNG_Internship',
                   'status_code': 200}
    return json_object


if __name__ == "__main__":
    app.run(debug=True)
