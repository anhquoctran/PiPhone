import time
import datetime


def convert_to_unix_timestamp(valuedatetime):
    unixtime = time.mktime(valuedatetime.timetuple())
    return unixtime


def convert_timestamp_to_time(valuetimestamp):
    d = datetime.datetime.fromtimestamp(valuetimestamp)
    return d
