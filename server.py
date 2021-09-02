from flask import Flask, request
import socket
import json
import requests

app = Flask(__name__)

CONSUMERS = {}
PROVIDERS = {}
SERVICES = {}
PROVIDER_SETTINGS = {}  # TODO

PROVIDER_URL = ""

######################################

@app.route('/')
def hello_world():
    return 'Service broker'

@app.route('/api/ip')
def get_ip():
    h_name = socket.gethostname()
    IP_addres = socket.gethostbyname(h_name)
    return json.dumps({
        "host_name": h_name,
        "ip": IP_addres
    })

######################################

# @app.route('/api/consumer/register', methods=['POST', 'PUT'])
# def add_device():
#     data = request.get_json() 
#     CONSUMERS[data['url']] = data 
#     return "ok"

# @app.route('/api/consumer/unregister', methods=['POST', 'PUT'])
# def remove_device():
#     data = request.get_json() 
#     CONSUMERS.pop(data['url'])
#     return "ok"

# @app.route('/api/consumer/list', methods=['GET'])
# def list_device():
#     return json.dumps(CONSUMERS)

######################################

# @app.route('/api/provider/register', methods=['POST', 'PUT'])
# def add_device():
#     data = request.get_json() 
#     PROVIDERS[data['url']] = data 
#     return "ok"

# @app.route('/api/provider/unregister', methods=['POST', 'PUT'])
# def remove_device():
#     data = request.get_json() 
#     PROVIDERS.pop(data['url'])
#     return "ok"

# @app.route('/api/provider/list', methods=['GET'])
# def list_device():
#     return json.dumps(PROVIDERS)

######################################

@app.route('/api/provider/register', methods=['POST', 'PUT'])
def add_device():
    data = request.get_json() 
    global PROVIDER_URL
    PROVIDER_URL = data['url']
    return "ok"

@app.route('/api/provider/list', methods=['GET'])
def list_device():
    return json.dumps(PROVIDER_URL)

######################################

@app.route('/api/service/request', methods=['POST', 'PUT'])
def add_depl():
    data = request.get_json() 
    print(data)
    try:
        r = requests.put("{}/api/service/add".format(PROVIDER_URL), json=data)
        print(r.content)
    except:
        print("exception")

    # SERVICES[data['id']] = data 
    return "ok"

@app.route('/api/service/remove', methods=['POST', 'PUT'])
def remove_depl():
    data = request.get_json() 
    try:
        print(data)
        r = requests.put("{}/api/service/remove".format(PROVIDER_URL), json=data)
        print(r.content)
    except:
        print("exception")

    # SERVICES.pop(data['id'])
    return "ok"

@app.route('/api/service/url', methods=['POST', 'PUT'])
def url_depl():
    data = request.get_json() 
    try:
        print(data)
        r = requests.put("{}/api/service/url".format(PROVIDER_URL), json=data)
        print(r.content)
    except:
        print("exception")

    # SERVICES.pop(data['id'])
    return r

@app.route('/api/service/list', methods=['GET'])
def list_depl():
    return json.dumps(SERVICES)

# ######################################

# @app.route('/api/provider/settings', methods=['POST', 'PUT'])
# def add_broker():
#     data = request.get_json()
#     PROVIDER_SETTINGS[data['id']] = data
#     return "ok"

# @app.route('/api/provider/list/settings', methods=['GET'])
# def list_brokers():
#     return json.dumps(BROKERS)

# ######################################


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)