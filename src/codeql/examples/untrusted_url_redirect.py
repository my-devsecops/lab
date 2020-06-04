from flask import Flask, request, redirect

app = Flask(__name__)

VALID_REDIRECT = "http://cwe.mitre.org/data/definitions/601.html"


@app.route('/')
#Bad Redirect
def hello_bad():
    target = request.args.get('target', '')
    return redirect(target, code=302)

#Good Redirect
def hello_good():
    target = request.args.get('target', '')
    if target == VALID_REDIRECT:
        return redirect(target, code=302)
    else:
        ...# Error
