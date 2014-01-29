DATA = [
    {
        'name': 'Dan',
        'surname': 'Tailor',
        'age': '22',
        'ocupation': 'Web Developer'
    },
    {
        'name': 'Bob',
        'surname': 'Dylan',
        'age': '72',
        'ocupation': 'Singer'
    }
]


def get_person_by_name(name):
    for person in DATA:
        if person['name'] == name:
            return person
    return False
