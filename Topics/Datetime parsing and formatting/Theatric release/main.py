from datetime import datetime


def get_release_date(release_str):
    string_time = release_str.split(':')[1].strip()
    return datetime.strptime(string_time, '%d %B %Y')
