from flask import Flask
import subprocess
import json

app = Flask(__name__)

@app.route('/status')
def get_terrad_status():
    result = subprocess.run(['terrad', 'status'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    parsed_output = json.loads(output)
    return parsed_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
