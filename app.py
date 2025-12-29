from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

# Simulate application start time to calculate uptime
start_time = time.time()

@app.route('/')
def home():
    """
    Main endpoint visible via browser.
    Returns the current status and uptime of the service.
    """
    uptime = time.time() - start_time
    return jsonify({
        "status": "Running",
        "message": "Hello from Docker and Kubernetes!",
        "uptime_seconds": round(uptime, 2),
        "version": "1.0.0"
    })

@app.route('/health')
def health():
    """
    Health check endpoint used by Kubernetes Liveness Probes.
    Returns HTTP 200 (OK) to signal that the container is healthy.
    If this fails, K8s will restart the pod.
    """
    return jsonify({"health": "ok"}), 200

if __name__ == "__main__":
    # Run the app on all interfaces (0.0.0.0) on port 5000
    app.run(host='0.0.0.0', port=5000)