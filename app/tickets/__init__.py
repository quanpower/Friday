from flask import Blueprint

blueprint = Blueprint(
    'tickets_blueprint',
    __name__,
    url_prefix='/tickets',
    template_folder='templates',
    static_folder='static'
)
