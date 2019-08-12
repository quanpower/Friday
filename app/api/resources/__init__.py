from .user import Login, Logout, GetUser, Register, Users, UserInfo
from .daq import Projects, Products, ProductProfile, Devices, DeviceProfile, DeviceDaqRealtime,\
 DeviceDaqAlarm, DeviceDaqHistory, DeviceDaqRecord, ProductDistribute, RegionDistribute, \
 DevicesOfProduct, DeviceDetail,DeviceHistoryRecord,DeviceAlarmRecord,DeviceRunningStatus, \
 AlarmRecord, DeviceOnLine

from .auto_init import AutoInit
from .add_mannual import AddUser, AddProject, AddProduct, AddDevice
from .fake import FakeNotices, Counter, MaintenanceRecord
from .version import ChangeLog, TodoList

__all__ = [
    'Register',
    'Login',
    'Logout',
    'GetUser',
    'Users',
    'UserInfo',
    'Projects',
    'Products',
    'ProductProfile',
    'Devices',
    'DeviceProfile',
    'DeviceDaqRealtime',
    'DeviceDaqAlarm',
    'DeviceDaqHistory',
    'DeviceDaqRecord',
    'AddUser',
    'AddProject',
    'AddProduct',
    'AddDevice',
    'AutoInit',
    'FakeNotices',
    'ChangeLog',
    'TodoList',
    'Counter',
    'MaintenanceRecord',
    'ProductDistribute',
    'RegionDistribute',
    'DevicesOfProduct',
    'DeviceDetail',
    'DeviceHistoryRecord',
    'DeviceAlarmRecord',
    'DeviceRunningStatus',
    'AlarmRecord',
    'DeviceOnLine',
]