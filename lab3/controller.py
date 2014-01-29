from model import get_person_by_name
from view import render_message


def view_person(name):
    person = get_person_by_name(name)
    response = render_message(person)
    return response
