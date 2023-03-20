# Guess the Random Number! :grin:
*An extremely simple number guessing game built with Python*
## About
The goal behind this simple guessing game was to gain some familiarity with Docker and understand how it can be used to run applications in an isolated environment and share these applications and their environments with other developers!

I've come to realize that a big reason Docker is so appealing to the majority of developers is because of how lightweight it is and how much easier it is to share, deploy, and test applications across all types of different machines.
## Installation
### Docker
1. Pull down the [latest docker image](https://hub.docker.com/repository/docker/luciidlou/guessing-game/general) from the Docker Hub
```
docker pull luciidlou/guessing-game:latest
```
2. Run the image in a container 
- With the default values
```
docker run --rm --name guessing-game-app -it luciidlou/guessing-game:latest
```
- With custom values  
`USER: str` (The name of the player. Defaults to `"guest"`)  
`LOW: int` (The lowest number you can guess. Defaults to `1`)  
`HIGH: int` (The highest number you can guess. Defaults to `20`)  
`MAX_GUESSES: int` (total number of times the player can guess before losing. Defaults to `3`)
```
docker run --rm --name guessing-game-app -it -e USER=<"YOUR NAME HERE"> -e LOW=<integer> -e HIGH=<integer> -e MAX_GUESSES=<integer> luciidlou/guessing-game:latest
```
---
### Source Code
1. Clone the source code onto your local machine
```
git clone git@github.com:luciidlou/guessing-game.git
```
2. Install dependencies (from project's root directory `/guessing-game`)
```
pip install -r requirements.txt
```
3. Play the game!
```
python guessing_game/main.py
```
