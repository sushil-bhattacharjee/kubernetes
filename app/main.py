from flask import Flask
import socket

ip = socket.gethostbyname(socket.gethostname())

def get_routers():
    # Replace the SQL query with a static list of routers
    routers = [
        {"hostname": "Router1", "ip": "192.168.1.1"},
        {"hostname": "Router2", "ip": "192.168.1.2"},
        {"hostname": "Router3", "ip": "192.168.1.3"},
        {"hostname": "Router4", "ip": "192.168.1.4"},
    ]
    return routers

app = Flask(__name__)

@app.route('/')
def home():
    out = (
        f"Welcome to Cisco Devnet.<br>"
        f"IP address of the server is {ip}.<br><br>"
        f"Welcome to the JamesBond world!<br><br>"
        f"Here is a list of the routers in the inventory:<br>"
    )
    out += "This is start of routers in the inventory:<br><br>"
    for r in get_routers():
        out += f"-> Hostname: {r['hostname']}, IP: {r['ip']}<br>"
    out += "This is the end of the routers inventory"
    return out

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
