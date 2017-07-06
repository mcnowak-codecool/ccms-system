from models.mentor_model import Mentor
from models.user_model import User
from views.mentor_view import *
from views.assignment_view import *
from models.assignment_model import Assignment
from datetime import datetime


def add_new_assignment(codecool):
    print_add_assignment_title()
    content = get_assignment_content()
    year = get_assignment_year()
    month = get_assignment_month()
    day = get_assignment_day()
    try:
        date = datetime(int(year), int(month), int(day))
        assignment = Assignment(content, date, Assignment.last_id + 1)
        codecool.assignments_list.append(assignment)
    except TypeError:
        print('Wrong values!')

    print_assignment_details(assignment)


def start_controller(codecool, mentor):
    choice = ''
    while choice != '0':
        print_mentor_menu()
        choice = get_choice()

        if choice == '1':
            print_students_list(codecool)
        elif choice == '2':
            add_new_assignment(codecool)
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass


def submit_assignment():
    pass
