import csv
import random


def load_csv():
    with open("data/Cancer_Data.csv", "r") as csvfile:
        return list(csv.DictReader(csvfile))


def random_select():
    data = load_csv()
    selection = {random.randint(0, len(data)) for _ in range(0, 10)}
