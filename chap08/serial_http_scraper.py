import random
import string

import requests

def generate_urls(base_url: str, num_urls: int):
    for i in range(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))


def run_experiment(base_url: str, num_iter=1000) -> int:
    response_size = 0
    for url in generate_urls(base_url, num_iter):
        response = requests.get(url)
        response_size += len(response.text)

    return response_size


if __name__ == "__main__":
    import time

    delay = 100
    num_iter = 1000
    # base_url = f"http://127.0.0.1:8080/add?name=serial&delay={delay}&"
    # base_url = f"http://www.google.com/add?name=serial&delay={delay}&"
    # Result: 1560000, Time: 100.01842927932739
    base_url = f"https://www.google.com/add?name=serial&delay={delay}&"
    # Result: 1560000, Time: 202.2268431186676

    start = time.time()
    result = run_experiment(base_url, num_iter)
    end = time.time()

    print(f"Result: {result}, Time: {end - start}")