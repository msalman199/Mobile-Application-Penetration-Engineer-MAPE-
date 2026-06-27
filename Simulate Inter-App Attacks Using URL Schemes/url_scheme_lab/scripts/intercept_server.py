#!/usr/bin/env python3
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
intercepted_data = []

@app.route('/callback', methods=['GET', 'POST'])
def callback_handler():
    """
    Handle callbacks from exploited applications.
    Captures and stores all incoming data.
    """
    # TODO: Extract timestamp
    # TODO: Capture request method, URL, and parameters
    # TODO: Store in intercepted_data list
    # TODO: Log to console
    # TODO: Return success response
    pass

@app.route('/data')
def view_data():
    """
    View all intercepted data.
    """
    # TODO: Return intercepted_data as JSON
    pass

@app.route('/clear')
def clear_data():
    """
    Clear all intercepted data.
    """
    # TODO: Clear intercepted_data list
    # TODO: Return confirmation
    pass

def main():
    print("Starting interception server on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    main()
