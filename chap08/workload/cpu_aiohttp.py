import asyncio
import aiohttp

import time

from cpu_bcrypt import do_task


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


if __name__ == '__main__':
    start = time.time()
    calculate_task_batch(600, 8)
    print(f"elapsed time: {time.time() - start}")
