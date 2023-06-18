from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    print('test')
    return(render_template('index.html'))


@app.route("/contact")
def contact():
    return(render_template('contact.html'))


@app.route("/projects")
def projects():
    return(render_template('projects_test.html'))


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9087, debug=True)


