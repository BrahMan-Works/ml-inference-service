import logging
import asyncio

from app.db_async import bulk_insert

write_queue: asyncio.Queue = asyncio.Queue(maxsize=10000)

async def db_writer():
    while True:
        batch = []

        item = await write_queue.get()
        batch.append(item)

        while len(batch) < 100:
            try:
                item = write_queue.get_nowait()
                batch.append(item)
            except asyncio.QueueEmpty:
                break

        try:
            await bulk_insert(batch)
        except Exception as e:
            logging.info(f"Writer error: {e}")

