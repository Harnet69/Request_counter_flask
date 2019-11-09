from flask import Flask, render_template, request

app = Flask(__name__)

requests = {"METHOD_GET":0, "METHOD_POST":0, "METHOD_PUT":0, "METHOD_DELETE":0}


@app.route('/')
def index_route():
    return render_template("index.html")


@app.route('/request-counter', methods=["GET", "POST"])
def request_counter_route():
    if request.method == "GET":
        requests['METHOD_GET'] += 1
    if request.method == "POST":
        requests['METHOD_POST'] += 1
    if request.method == "PUT":
        requests['METHOD_PUT'] += 1
    if request.method == "DELETE":
        requests['METHOD_DELETE'] += 1
    return render_template("request-counter.html", requests=requests)


@app.route('/statistics')
def statistics_route():
    return render_template("statistics.html", requests=requests)


if __name__ == '__main__':
    app.run()
