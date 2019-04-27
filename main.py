from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "n the beginning tof the year 1800 Volta tmade the first electric battery. He made it of tcopper and zink disks whi'dry battery'."

result = re.findall(r't\w*'string)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
