from flask import Blueprint

blueprint = Blueprint(
    'conf2d_blueprint',
    __name__,
    url_prefix='/conf2d',
    template_folder='templates',
    static_folder='static'
)
