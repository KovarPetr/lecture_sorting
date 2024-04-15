import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    iteration = 0
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for key, value in row.items():
                if iteration == 0:
                    data[key] = [int(value)]
                else:
                    data[key].append(int(value))
            iteration = iteration + 1
        return data


def selection_sort(list_to_sort, direction="up"):
    iteration = 0
    position = 0
    if direction == "up":
        for number in list_to_sort:
            min = list_to_sort[iteration]
            for comparable in list_to_sort[iteration:]:
                if min > comparable:
                    min = comparable
                    position_min = position
                position = position + 1
            list_to_sort[iteration], list_to_sort[position_min] = list_to_sort[position_min], list_to_sort[iteration]
            iteration = iteration + 1
            position_min = iteration
            position = iteration
    if direction == "down" :
        for number in list_to_sort:
            max = list_to_sort[iteration]
            for comparable in list_to_sort[iteration:]:
                if max < comparable:
                    max = comparable
                    position_max = position
                position = position + 1
            list_to_sort[iteration], list_to_sort[position_max] = list_to_sort[position_max], list_to_sort[iteration]
            iteration = iteration + 1
            position_max = iteration
            position = iteration
    return list_to_sort


def main():
    data = read_data("numbers.csv")
    print(selection_sort(data["series_1"], "down"))
    pass


if __name__ == '__main__':
    main()
