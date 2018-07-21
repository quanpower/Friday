from .user import Login, Logout, GetUser, Register, Users
from .daq import Projects, Products, Devices, DeviceDaqRealtime, DeviceDaqAlarm, DeviceDaqHistory, DeviceDaqRecord

from .auto_init import AutoInit
from .fake import FakeNotices

__all__ = [
    'Register',
    'Login',
    'Logout',
    'GetUser',
    'Users',
    'Projects',
    'Products',
    'Devices',
    'DeviceDaqRealtime',
    'DeviceDaqAlarm',
    'DeviceDaqHistory',
    'DeviceDaqRecord',
    'AutoInit',
    'FakeNotices',
]