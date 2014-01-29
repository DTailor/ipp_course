TEMPLATE = " %s %s is %s old, and is a %s by fate."


def render_message(person):
    name = person['name']
    surname = person['surname']
    age = person['age']
    ocupation = person['ocupation']

    return TEMPLATE % (name,
                       surname,
                       age,
                       ocupation
                       )
