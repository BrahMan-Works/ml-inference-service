import logging
import asyncio
import numpy as np
import torch

from app.ml_model import model, device

gpu_queue = asyncio.Queue()

BATCH_SIZE = 64
MAX_WAIT_MS = 10

async def gpu_batch_worker():
    while True:
        batch = []
        futures = []

        item = await gpu_queue.get()
        batch.append(item[0])
        futures.append(item[1])

        start = asyncio.get_event_loop().time()

        while len(batch) < BATCH_SIZE:
            if (asyncio.get_event_loop().time() - start) * 1000 > MAX_WAIT_MS:
                break

            try:
                item = gpu_queue.get_nowait()
                batch.append(item[0])
                futures.append(item[1])
            except asyncio.QueueEmpty:
                await asyncio.sleep(0.001)

        features = np.vstack(batch)

        logging.info(f"GPU batch size: {len(batch)}")

        with torch.no_grad():
            tensor = torch.tensor(features, dtype=torch.float32).to(device)
            with torch.autocast("cuda"):
                outputs = model(tensor)

        for i, future in enumerate(futures):
            future.set_result(outputs[i][0])

async def submit_inference(features):
    loop = asyncio.get_event_loop()
    future = loop.create_future()

    await gpu_queue.put((features, future))

    result = await future
    return result

