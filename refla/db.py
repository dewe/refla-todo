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


def get_by_id(id):
    items = [item for item in data if item['id'] == id]
    return items[0] if len(items) > 0 else None


def insert(item):
    item['id'] = data[-1]['id'] + 1
    data.append(item)
    return item