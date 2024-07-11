from flask import Flask
import time
import requests  # Importing requests to handle HTTP requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! My name is Octavian."

def register_service():
    service_info = {
        "serviceDefinition": "OctavianService",
        "provider": {
            "systemName": "OctavianProvider",
            "address": "localhost",
            "port": 5000,
            "authenticationInfo": None
        },
        "serviceUri": "/",
        "endOfValidity": None,
        "secure": False,
        "metadata": {},
        "interfaces": ["HTTP-INSECURE-JSON"]
    }
    try:
        resp = requests.post("http://localhost:8443/serviceregistry/register", json=service_info)
        resp.raise_for_status()
    except requests.RequestException as err:
        print(f"Service registration failed: {err}")

if __name__ == "__main__":
    # Wait to make sure core services are up
    time.sleep(10)
    register_service()
    app.run(host='0.0.0.0', port=5000)
