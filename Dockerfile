FROM python:3.6

WORKDIR /app

COPY ./romanos/* ./romanos/
COPY ./tests/* ./tests/

COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["pytest",  "-x"]
