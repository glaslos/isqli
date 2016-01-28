import urllib
import json

import pylibinjection

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    q = request.args.get('q', '')
    output = request.args.get('o', '')
    res = None
    print urllib.unquote(q)
    if q != "":
        res = pylibinjection.detect_sqli(q)
        print repr(q)
    if output == "json":
        return json.dumps(res)
    return render_template('index.html', query=q, res=res)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8008)
