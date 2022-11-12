import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    year = date.strftime("%Y")
    month = date.strftime("%B")
    day = date.strftime("%d")
    day_word = date.strftime("%A")
    return f"{day_word} {day} {month} {year}"


def convert_f_to_c(temp_in_farenheit):
    """Converts a temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    return round(((float(temp_in_farenheit) - 32) * 5 / 9), 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    num_weather_data = []
    for item in weather_data:
        num_weather_data.append(float(item))

    return sum(num_weather_data) / len(weather_data)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file, encoding="utf8") as weather_file:
        weather_data = csv.reader(weather_file)
        next(weather_data)

        weather_data_list = []

        for line in weather_data:
            if line != []:
                new_line = []
                new_line.append(line.pop(0))
                for item in line:
                    new_line.append(int(item))
                weather_data_list.append(new_line)
        return(weather_data_list)


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and its position in the list.
    """
    num_weather_data = []

    if weather_data != []:
        for item in weather_data:
            num_weather_data.append(float(item))

        min_value = min(num_weather_data)
        reversed_num_weather_data = num_weather_data[::-1]
        min_value_index = len(num_weather_data) - 1 - reversed_num_weather_data.index(min_value)

        return min_value, min_value_index
    return ()


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and its position in the list.
    """
    num_weather_data = []

    if weather_data != []:
        for item in weather_data:
            num_weather_data.append(float(item))

        max_value = max(num_weather_data)
        reversed_num_weather_data = num_weather_data[::-1]
        max_value_index = len(num_weather_data) - 1 - reversed_num_weather_data.index(max_value)

        return max_value, max_value_index
    return ()


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
