from flask import Flask, render_template, request

app = Flask(__name__)

METHOD_GET = 0
METHOD_POST = 0


@app.route('/')
def index_route():
    return render_template("index.html")


@app.route('/request-counter', methods=["GET", "POST"])
def request_counter_route():
    if request.method == "GET":
        print("GET")
        global METHOD_GET
        METHOD_GET += 1
    if request.method == "POST":
        print("POST")
        global METHOD_POST
        METHOD_POST += 1
    return render_template("request-counter.html", method_get=METHOD_GET, method_post=METHOD_POST)


@app.route('/statistics')
def statistics_route():
    return render_template("statistics.html")


if __name__ == '__main__':
    app.run()
