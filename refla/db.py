data = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

def get_all():
    return data


def get_by_id(id):
    items = [item for item in data if item['id'] == id]
    return items[0] if len(items) > 0 else None
