FROM python

WORKDIR /app

COPY requirements.txt /app

# `RUN` executes when an image is created
RUN pip install -r requirements.txt

COPY . /app

# `CMD` executes when a container based on the image in started
CMD ["python3", "guessing_game/main.py"]