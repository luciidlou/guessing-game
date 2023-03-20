FROM python:3.10.8

WORKDIR /guessing-game

COPY requirements.txt /guessing-game

# `RUN` executes when an image is created
RUN pip install -r requirements.txt

COPY . /guessing-game

ENV USER="guest"
ENV LOW=1
ENV HIGH=20
ENV MAX_GUESSES=3

# `CMD` executes when a container based on the image is started
CMD ["python3", "guessing_game/main.py"]