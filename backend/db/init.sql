CREATE TABLE IF NOT EXISTS inference_requests (
    id SERIAL PRIMARY KEY,
    x FLOAT NOT NULL,
    y FLOAT NOT NULL,
    result FLOAT NOT NULL
);
