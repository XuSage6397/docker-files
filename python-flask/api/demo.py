from flask import Blueprint

demo = Blueprint('demo', __name__)


@demo.route('/demo')
def get_items():
    return {"items": ["item1", "item2"]}
