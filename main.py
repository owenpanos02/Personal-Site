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
    return(render_template('projects.html'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000,
            use_reloader=True, threaded=True)