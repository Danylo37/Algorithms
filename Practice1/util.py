from datetime import datetime


def calculate_age(birthdate):
    """Calculates age by birthdate

    :param birthdate: (str) string with birthdate in format "DD.MM.YYYY"
    :return: (int) age of the employee
    """
    birthdate = datetime.strptime(birthdate, '%d.%m.%Y')
    current_date = datetime.now()

    age = current_date.year - birthdate.year - (
                (current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    return age
