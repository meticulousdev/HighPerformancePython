import asyncio
import aiohttp


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
