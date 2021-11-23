import csv
from random import randint

def create_content_timestampAndValue(content_line_num: int, first_timestamp: int):
    for i in range(0, content_line_num):
        yield first_timestamp+randint(1000, 100000), i


if __name__ == "__main__":
    file_path = "data.csv"
    content_line_num = 10000
    first_timestamp = 1637390767

    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for timestamp, value in create_content_timestampAndValue(content_line_num, first_timestamp):
            writer.writerow([timestamp, value])

