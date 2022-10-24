# This configuration use official Docker image for Python
# see: https://docs.docker.com/language/python/build-images/
FROM python:3.9.15-slim-buster

WORKDIR /app

# install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the app
COPY . .

# run the API server
# see: https://fastapi.tiangolo.com/deployment/server-workers/
CMD gunicorn api:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT