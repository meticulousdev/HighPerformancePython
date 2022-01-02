import random
import string

import bcrypt
import requests

import time


def do_task(i, difficulty):
    passwd = ("".join(random.sample(string.ascii_lowercase, 10)).encode("utf8"))
    salt = bcrypt.gensalt(difficulty)
    result = bcrypt.hashpw(passwd, salt)
    return result.decode("utf8")


def save_result_serial(result):
    url = f"http://127.0.0.1:8080/add"
    response = requests.post(url, data=result)
    return response.json()


def calculate_task_serial(num_iter, task_difficult):
    for i in range(num_iter):
        result = do_task(i, task_difficult)
        save_result_serial(result)


if __name__ == '__main__':
    start = time.time()
    calculate_task_serial(600, 8)
    print(f"elapsed time: {time.time() - start}")
