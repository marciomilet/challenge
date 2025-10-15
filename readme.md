# Campaigns API

## Requirements

 [Python](https://www.python.org)
 [Django](https://duckduckgo.com)
 [Redis](https://redis.io)
 [Docker](https://www.docker.com) (if you are on windows)
  
## Instalation

Firstly clone this repository into any folder you like,
open a terminal on the root folder of the project ( the one that contains requirements.txt)
and
` run pip install requirements.txt `
this should install all depedencies required for the project

## Running the API

after installation on a terminal on api\mysite run
`py manage.py runserver`
to start the server

## Windows

if you are on windows the recommended way to run redis is on a docker container, make sure docker engine is running
and on the root folder run 
`docker run -d -p 6379:6379 redis`
to run the docker container configured on docker-compose.yml
now on a new terminal run
`celery -A mysite worker -l info -P solo`
to start the celery worker and keep track its infos
