FROM tiangolo/uvicorn-gunicorn:python3.10

LABEL maintainer="Fat Plants MU <fatplantsmu@gmail.com>"

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Set environment variables
ENV place=docker

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--ssl-certfile","auth_docker/fullchain.pem","--ssl-keyfile","auth_docker/privkey.pem"]