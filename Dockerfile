FROM python:3.10.8

WORKDIR /app

COPY requirements.txt /app

# `RUN` executes when an image is created
RUN pip install -r requirements.txt

COPY . /app

ARG DEFAULT_LOW=1
ARG DEFAULT_HIGH=20
ARG DEFAULT_MAX_GUESSES=3

ENV LOW ${DEFAULT_LOW}
ENV HIGH ${DEFAULT_HIGH}
ENV MAX_GUESSES ${DEFAULT_MAX_GUESSES}

# `CMD` executes when a container based on the image is started
CMD ["python3", "guessing_game/main.py"]