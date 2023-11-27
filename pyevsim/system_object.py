# system_object.py
import datetime

class SysObject(object):
    __GLOBAL_OBJECT_ID = 0

    def __init__(self):
        self.__created_time = datetime.datetime.now()
        self.__object_id = SysObject.__GLOBAL_OBJECT_ID
        SysObject.__GLOBAL_OBJECT_ID += 1

    def get_obj_id(self):
        return self.__object_id