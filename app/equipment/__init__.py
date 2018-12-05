from flask import Blueprint

blueprint = Blueprint(
    'equipment_blueprint',
    __name__,
    url_prefix='/equipment',
    template_folder='templates',
    static_folder='static'
)
