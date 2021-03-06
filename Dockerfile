FROM python:3
MAINTAINER Violet M. <vi@violet.wtf>

WORKDIR /gofree

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./run.py"]
