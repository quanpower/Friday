from app.conf2d import blueprint
from flask import render_template, jsonify
from flask_login import login_required


@blueprint.route('/<template>')
# @login_required
def route_template(template):
    return render_template(template + '.html')

@blueprint.route('/device_status')
def device_status():
    data = {
    'current_value':{    
        'current_value_1': '0.1',
        'current_value_2': '0.2',
        'current_value_3': '0.3',
        'current_value_4': '0.4',
        'current_value_5': '0.5',
        'current_value_6': '0.6',
    },
    'work_status':{
        'work_status_1':'1',
        'work_status_2':'0',
        'work_status_3':'1',
        'work_status_4':'-1',
        'work_status_5':'1',
        'work_status_6':'0',
    },
    'input_pressure':'0.6',
    'material_temprature':'24',
    'line_speed':'1',
    'current_running_time':{
        'h':'1',
        'min':'23',
        's':'45',
    },
    'accumulated_running_time':{
        'h':'50',
        'min':'12',
        's':'25',
    },

    }
    print("js get!")
    return jsonify(data)
