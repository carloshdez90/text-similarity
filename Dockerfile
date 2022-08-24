FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "-b", "0.0.0.0:80", "--workers", "4", "--keep-alive", "7200", "-t", "7200"]