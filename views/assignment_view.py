def print_assignment_details(assignment):
    """
    Function prints assignment details

    Args:
        assignment (Assignment): object represents single assignment added by mentor

    Returns:
        None
    """

    ornament = 30 * '='
    print(ornament)
    print('Assignment id:', assignment.assignment_id)
    print('Deadline:', assignment.deadline)
    print('Assignment:', assignment.content)
    print(ornament)


def print_title():
    ornament = 30 * '='
    print(ornament)
    print("You are adding new assignment.")


def get_content():
    return input("Input assignment content: ")


def get_year():
    return input("Input deadline year: ")


def get_month():
    return input("Input deadline month: ")


def get_day():
    return input("Input deadline day: ")
