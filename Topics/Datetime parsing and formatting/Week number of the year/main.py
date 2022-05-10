from datetime import datetime


def get_week_number(datetime_obj):
    return datetime_obj.strftime('Week number: %U.')
