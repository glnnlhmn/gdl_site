from flask import Blueprint, render_template, send_from_directory

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')


# @main.route('/css/<path:path>')
# def send_css(path):
#     return send_from_directory('docs/css', path)
#
#
# @main.route('/js/<path:path>')
# def send_js(path):
#     return send_from_directory('docs/js', path)