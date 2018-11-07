from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse, abort
import time
import datetime
import json


COUNTERS = {
    '1': {'counter': 10},
    '2': {'counter': 20},
    '3': {'counter': 30},
}


def abort_if_device_doesnt_exist(device_id):
    if device_id not in COUNTERS:
        abort(404, message="Device {} doesn't exist".format(device_id))

parser = reqparse.RequestParser()
parser.add_argument('switch')


# Todo
# shows a single todo item and lets you delete a todo item
class Counter(Resource):
    def get(self, device_id):
        abort_if_device_doesnt_exist(device_id)
        return COUNTERS[device_id]

    def post(self, device_id):
        args = parser.parse_args()
        if args['switch'] == 'start':
            counter = {'status':'reseted', 'counter': 0}
            COUNTERS[device_id] = counter
            return counter, 201
        return 'invaild'



class FakeList(Resource):

    def get(self):
        pass

    def post(self):
        pass


        # return jsonify({ 'success': True, 'message': 'Ok' })

    def delete(self):
        pass

    def put(self):
        pass


class FakeNotices(Resource):

    def get(self):
        getNotices = [
            {
            'id': '000000001',
            'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png',
            'title': '你收到了 14 份新周报',
            'datetime': '2017-08-09',
            'type': '通知',
            },
            {
            'id': '000000002',
            'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/OKJXDXrmkNshAMvwtvhu.png',
            'title': '你推荐的 曲妮妮 已通过第三轮面试',
            'datetime': '2017-08-08',
            'type': '通知',
            },
            {
            'id': '000000003',
            'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/kISTdvpyTAhtGxpovNWd.png',
            'title': '这种模板可以区分多种通知类型',
            'datetime': '2017-08-07',
            'read': True,
            'type': '通知',
            },
            {
            'id': '000000004',
            'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/GvqBnKhFgObvnSGkDsje.png',
            'title': '左侧图标用于区分不同的类型',
            'datetime': '2017-08-07',
            'type': '通知',
            },
            {
            'id': '000000005',
            'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png',
            'title': '内容不要超过两行字，超出时自动截断',
            'datetime': '2017-08-07',
            'type': '通知',
            },
            {
            'id': '000000006',
            'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/fcHMVNCjPOsbUGdEduuv.jpeg',
            'title': '曲丽丽 评论了你',
            'description': '描述信息描述信息描述信息',
            'datetime': '2017-08-07',
            'type': '消息',
            },
            {
            'id': '000000007',
            'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/fcHMVNCjPOsbUGdEduuv.jpeg',
            'title': '朱偏右 回复了你',
            'description': '这种模板用于提醒谁与你发生了互动，左侧放『谁』的头像',
            'datetime': '2017-08-07',
            'type': '消息',
            },
            {
            'id': '000000008',
            'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/fcHMVNCjPOsbUGdEduuv.jpeg',
            'title': '标题',
            'description': '这种模板用于提醒谁与你发生了互动，左侧放『谁』的头像',
            'datetime': '2017-08-07',
            'type': '消息',
            },
            {
            'id': '000000009',
            'title': '任务名称',
            'description': '任务需要在 2017-01-12 20:00 前启动',
            'extra': '未开始',
            'status': 'todo',
            'type': '待办',
            },
            {
            'id': '000000010',
            'title': '第三方紧急代码变更',
            'description': '冠霖提交于 2017-01-06，需在 2017-01-07 前完成代码变更任务',
            'extra': '马上到期',
            'status': 'urgent',
            'type': '待办',
            },
            {
            'id': '000000011',
            'title': '信息安全考试',
            'description': '指派竹尔于 2017-01-09 前完成更新并发布',
            'extra': '已耗时 8 天',
            'status': 'doing',
            'type': '待办',
            },
            {
            'id': '000000012',
            'title': 'ABCD 版本发布',
            'description': '冠霖提交于 2017-01-06，需在 2017-01-07 前完成代码变更任务',
            'extra': '进行中',
            'status': 'processing',
            'type': '待办',
            },
            ]
        return jsonify(getNotices)

    def post(self):
        pass


        # return jsonify({ 'success': True, 'message': 'Ok' })

    def delete(self):
        pass

    def put(self):
        pass