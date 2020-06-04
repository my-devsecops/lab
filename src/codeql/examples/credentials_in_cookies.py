from flask import Flask, make_response, request

app = Flask("Leak password")


def render_template(data):
    return None


@app.route('/')
def index():
    password = request.args.get("password")
    resp = make_response(render_template(...))
    resp.set_cookie("password", password)
    return resp
