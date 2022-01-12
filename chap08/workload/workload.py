# 8.3.1 Serial
import random
import string

import bcrypt
import requests

# 8.3.2 Batched Results
import asyncio
import aiohttp

import time


# 8.3.1 Serial
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


# 8.3.2 Batched Results
class AsyncBatcher(object):
    def __init__(self, batch_size):
        self.batch_size = batch_size
        self.batch = []
        self.client_session = None
        self.url = f"http://127.0.0.1:8080/add"
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args, **kwargs):
        self.flush()
    
    def save(self, result):
        self.batch.append(result)
        if len(self.batch) == self.batch_size:
            self.flush()
    
    def flush(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__aflush())

    async def __aflush(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(result, session) for result in self.batch]
            for task in asyncio.as_completed(tasks):
                await task
            self.batch.clear()
    
    async def fetch(self, result, session):
        async with session.post(self.url, data=result) as response:
            return await response.json()


def calculate_task_batch(num_iter, task_difficulty):
    with AsyncBatcher(100) as batcher:
        for i in range(num_iter):
            result = do_task(i, task_difficulty)
            batcher.save(result)


# 8.3.3 Full Async
def save_result_aiohttp(client_session):
    sem = asyncio.Semaphore(100)

    async def saver(result):
        nonlocal sem, client_session
        url = f"http://127.0.0.1:8080/add"
        async with sem:
            async with client_session.post(url, data=result) as response:
                return await response.json()
    
    return saver


async def calculate_task_aiohttp(num_iter, task_difficulty):
    task = []
    async with aiohttp.ClientSession() as client_session:
        saver = save_result_aiohttp(client_session)
        for i in range(num_iter):
            result = do_task(i, task_difficulty)
            task = asyncio.create_task(saver(result))
            task.append(task)
            await asyncio.sleep(0)
        await asyncio.wait(task)



if __name__ == '__main__':
    start = time.time()
    calculate_task_serial(600, 8)
    print(f"Serial took {time.time() - start} seconds")
    
    start = time.time()
    calculate_task_batch(600, 8)
    print(f"Batched Results took {time.time() - start} seconds")

    start = time.time()
    calculate_task_aiohttp(600, 8)
    print(f"Full Async took {time.time() - start} seconds")

    # Serial took 91.36244678497314 seconds
    # Batched Results took 9.949486255645752 seconds
    # workload.py:114: RuntimeWarning: coroutine 'calculate_task_aiohttp' was never awaited
    #   calculate_task_aiohttp(600, 8)
    # RuntimeWarning: Enable tracemalloc to get the object allocation traceback
    # Full Async took 0.002679109573364258 seconds
