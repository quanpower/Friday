from flask import Blueprint

blueprint = Blueprint(
    'conf3d_blueprint',
    __name__,
    url_prefix='/conf3d',
    template_folder='templates',
    static_folder='static'
)
