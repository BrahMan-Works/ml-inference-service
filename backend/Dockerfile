FROM nvidia/cuda:12.3.1-runtime-ubuntu22.04

WORKDIR /app

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install --no-cache-dir \
    torch torchvision torchaudio \
    --extra-index-url https://download.pytorch.org/whl/cu121

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN cd app/cpp && python setup.py build_ext --inplace || true

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
