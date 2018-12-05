from app.tickets import blueprint
from flask import render_template
from flask_security import login_required


@blueprint.route('/<template>')
# @login_required
def route_template(template):
    return render_template(template + '.html')
