import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = json.dumps(func(*args, **kwargs))
        return result
    return wrapped


@to_json
def get_data():
    d = {}
    d['Name'] = 'Luke'
    d['Country'] = 'Canada'
    return d


if __name__ == '__main__':
    print(get_data())
    # print(type(get_data()))
    print(get_data.__name__)
