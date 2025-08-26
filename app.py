#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    # Delay long enough for Flask to start
    Timer(2, lambda: webbrowser.open("http://localhost:9000")).start()
    app.run(host="0.0.0.0", port=9000, debug=True, use_reloader=False)
