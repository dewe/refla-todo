from copy import copy

data = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'done': False
    }
]

def get_all():
    return data


def get_by_id(item_id):
    items = [item for item in data if item['id'] == item_id]
    return items[0] if len(items) > 0 else None


def insert(item):
    item = copy(item)
    item['id'] = data[-1]['id'] + 1
    data.append(item)
    return item


def update(item_id, item):
    item = copy(item)
    item['id'] = item_id
    globals()['data'] = map(lambda x: x if x['id'] != item_id else item, data)
    return item