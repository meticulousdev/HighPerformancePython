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
    base_url = f"http://127.0.0.1/add?name=serial&delay={delay}&"

    start = time.time()
    result = run_experiment(base_url, num_iter)
    end = time.time()

    print(f"Result: {result}, Time: {end - start}")
    # Result: 196000, Time: 1.4080660343170166
