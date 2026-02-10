from app.db import get_connection

def insert_inference(x: float, y: float, result: float) -> int:
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO inference_requests (x, y, result)
            VALUES (%s, %s, %s)
            RETURNING id;
            """,
            (x, y, result)
        )

        inserted_id = cur.fetchone()[0]
        conn.commit()

        return inserted_id
    
    except Exception:
        if conn:
            conn.rollback()
        raise

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def get_inference_by_id(inference_id: int):
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT id, x, y, result
            FROM inference_requests
            WHERE id = %s;
            """,
            (inference_id,)
        )

        row = cur.fetchone()
        return row

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

