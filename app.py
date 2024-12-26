from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='docs', template_folder='docs')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('docs/css', path)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('docs/js', path)


if __name__ == '__main__':
    app.run(debug=True)