import asyncio
import random
import string
from functools import partial

from tornado.httpclient import AsyncHTTPClient


AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient", 
                          max_clients=100)


def generate_urls(base_url: str, num_urls: int):
    for i in range(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))


async def run_experiment(base_url: str, num_iter=1000) -> int:
    http_client = AsyncHTTPClient()
    urls = generate_urls(base_url, num_iter)
    response_sum = 0
    tasks = [http_client.fetch(url) for url in urls]
    for task in asyncio.as_completed(tasks):
        respose = await task
        response_sum += len(respose.body)
    return response_sum


if __name__ == "__main__":
    import time

    delay = 100
    num_iter = 1000
    run_func = partial(run_experiment,
                       f"http://127.0.0.1?name=tornado&delay={delay}&",
                       num_iter)

    start = time.time()
    result = asyncio.run(run_func())
    end = time.time()

    print(f"Result: {result}, Time: {end - start}")
    # first run - Result: 45000, Time: 6.025541067123413
    # second run - Result: 45000, Time: 0.13853025436401367

    # ModuleNotFoundError: No module named 'pycurl'
    # https://gist.github.com/vidakDK/de86d751751b355ed3b26d69ecdbdb99
    # pycurl                    7.44.1                   pypi_0    pypi

    # ValueError: a coroutine was expected, got functools.partial(<function run_experiment at 0x1054403a0>, 'http://127.0.0.1?name=tornado&delay=100&', 1000)
    # result = asyncio.run(run_func) > result = asyncio.run(run_func())
