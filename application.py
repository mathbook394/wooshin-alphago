from flask import Flask, request, Response
from flask import render_template

application = Flask(__name__,static_folder='assets')

@application.route("/", methods=["GET"])
def main():
    return render_template("main.html")
    

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)