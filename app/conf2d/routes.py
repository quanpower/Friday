from app.conf2d import blueprint
from flask import render_template, jsonify
from flask_login import login_required
from app import db
from app.models import Project, Product, Device, Daq, Alarm
from sqlalchemy import and_
import json
import random
import datetime, time


@blueprint.route('/<template>')
# @login_required
def route_template(template):
    return render_template(template + '.html')


@blueprint.route('/running_status/<device_id>')
def running_status(device_id):
    return render_template('running_status.html', device_id=device_id)


@blueprint.route('/alarm_records/<user_id>')
def alarm_records(user_id):
    return render_template('alarm_records.html', user_id=user_id)


@blueprint.route('/device_status')
def device_status():

    device_daq_realtime = Daq.query.filter_by(device_id=4).order_by(
        Daq.gmt_daq.desc()).first()

    print('--------device_daq_realtime--------\n' * 3)
    print(device_daq_realtime)

    daq_values = device_daq_realtime.daq_value
    # daq_values = json.loads(device_daq_realtime.daq_value)
    gmt_daq = device_daq_realtime.gmt_daq
    gmt_daq_str = datetime.datetime.strftime(gmt_daq, "%H-%M-%S")
    

    print(daq_values)

    return jsonify(daq_values)



