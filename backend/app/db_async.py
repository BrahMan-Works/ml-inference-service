import os
import logging
import asyncio
import asyncpg

pool = None

async def bulk_insert(batch):
    query = """
            INSERT INTO inference_requests (x, y, result)
            VALUES ($1, $2, $3)
            """

    async with pool.acquire() as conn:
        async with conn.transaction():
            await conn.executemany(query, batch)

async def init_async_pool():
    global pool
    try:
        pool = await asyncpg.create_pool(
            database = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            min_size = 5,
            max_size = 50
        )
        logging.info("Async DB pool created.")
        return
    except Exception as e:
        logging.info(f"Async DB not ready.")

    raise Exception("Failed to initialize async DB pool.")

async def insert_inference_async(x, y, result):
    async with pool.acquire() as connection:
        return await connection.fetchval(
            """
            INSERT INTO inference_requests (x, y, result)
            VALUES ($1, $2, $3)
            RETURNING id;
            """,
            x, y, result
        )

