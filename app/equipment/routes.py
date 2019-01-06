from app.equipment import blueprint
from flask import render_template, jsonify
from flask_security import login_required
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


@blueprint.route('/product_list/<int:user_id>')
def product_list(user_id):

    products = Product.query.filter_by(user_id=user_id).order_by(
        Product.gmt_create.desc()).all()

    print('--------products--------\n' * 3)
    print(products)
    products_list = []
    for product in products:
        print(product.devices)
        products_list.append(product)

    print(products_list)
    # return jsonify(products_list)
    return render_template('product_list.html', products=products_list)




@blueprint.route('/device_list/<int:user_id>')
def device_list(user_id):

    return render_template('device_list.html', user_id=user_id)


@blueprint.route('/device_of_product/<int:product_id>')
def device_of_product(product_id):

    return render_template('device_of_product.html', product_id=product_id)


@blueprint.route('/device_detail/<device_id>')
def device_detail(device_id):
    return render_template('device_detail.html', device_id=device_id)


    # device_daq_realtime = Daq.query.filter_by(device_id=4).order_by(
    #     Daq.gmt_daq.desc()).first()

    # # device_daq_realtime = db.session.query(Daq.gmt_daq, Daq.daq_value).filter(
    # #     Daq.device_id == deviceID).order_by(
    # #     Daq.gmt_daq.desc()).first()


    # print('--------device_daq_realtime--------\n' * 3)
    # print(device_daq_realtime)

    # daq_values = device_daq_realtime.daq_value
    # # daq_values = json.loads(device_daq_realtime.daq_value)
    # gmt_daq = device_daq_realtime.gmt_daq
    # gmt_daq_str = datetime.datetime.strftime(gmt_daq, "%H-%M-%S")
    

    # print(daq_values)


    # # data = {
    # # 'current_value':{    
    # #     'current_value_1': '0.1',
    # #     'current_value_2': '0.2',
    # #     'current_value_3': '0.3',
    # #     'current_value_4': '0.4',
    # #     'current_value_5': '0.5',
    # #     'current_value_6': '0.6',
    # # },
    # # 'work_status':{
    # #     'work_status_1':'1',
    # #     'work_status_2':'0',
    # #     'work_status_3':'1',
    # #     'work_status_4':'-1',
    # #     'work_status_5':'1',
    # #     'work_status_6':'0',
    # # },
    # # 'input_pressure':'0.6',
    # # 'material_temprature':'24',
    # # 'line_speed':'1',
    # # 'current_running_time':{
    # #     'h':'1',
    # #     'min':'23',
    # #     's':'45',
    # # },
    # # 'accumulated_running_time':{
    # #     'h':'50',
    # #     'min':'12',
    # #     's':'25',
    # # },
    # # 'current_time':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

    # # }

    # return jsonify(daq_values)


