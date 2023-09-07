from flask import Flask, request
from datetime import date, datetime
import requests

app = Flask(__name__)
utc_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


@app.route('/api')
def index():
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")
    json_object = {'slack_name': slack_name,
                   'current_day': datetime.now().strftime('%A'),
                   'utc_time': utc_time,
                   'track': track,
                   'github_file_url': 'github_file_url',
                   'github_repo_url': 'github_repo_url',
                   'status_code': 200}
    return json_object


if __name__ == "__main__":
    app.run(debug=True)
