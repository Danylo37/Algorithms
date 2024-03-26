import calendar
import random


def generate_birthday(a, b):
    """Generates birthdate from 'a' year to 'b' year

    :param a: year from
    :param b: year to

    :return: (str) string with birthdate in format 'DD.MM.YYYY'
    """
    month = random.randint(1, 12)
    year = random.randint(a, b)

    day_range = calendar.monthrange(year, month)[1]
    day = random.randint(1, day_range)

    birthdate = "{:02d}.{:02d}.{}".format(day, month, year)

    return birthdate
