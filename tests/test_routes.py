from flask import template_rendered, render_template, Blueprint
from contextlib import contextmanager
import pytest

test_blueprint = Blueprint('test', __name__, template_folder='templates')

@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

def test_index_route(client, app):
    with captured_templates(app) as templates:
        response = client.get('/')
        assert response.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'pages/index.html'
        # You can also check for specific context variables if needed
        # assert 'some_variable' in context