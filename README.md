## How to use it
- Run `docker compose up -d --build` - To build images and run them
- Next command is to see what containers are running `docker compose ps`. Example output
    ```bash
        ~/projects/blizy$ docker compose ps
    NAME            IMAGE                     COMMAND                  SERVICE    CREATED      STATUS             PORTS
    blizy_db        postgres:17               "docker-entrypoint.s…"   db         5 days ago   Up 2 days          0.0.0.0:5432->5432/tcp
    blizy_db_ui     adminer                   "entrypoint.sh docke…"   db-ui      7 days ago   Up 2 days          0.0.0.0:8080->8080/tcp
    blizy_fronend   blizy-homework-frontend   "docker-entrypoint.s…"   frontend   7 days ago   Up About an hour   0.0.0.0:3000->3000/tcp
    blizy_nginx     nginx:latest              "/docker-entrypoint.…"   nginx      7 days ago   Up 2 days          0.0.0.0:8000->80/tcp
    blizy_php       blizy-homework-php        "docker-php-entrypoi…"   php        5 days ago   Up 2 days          0.0.0.0:9000->9000/tcp
    blizy_python    blizy-homework-python     "python3"                python     3 days ago   Up 2 days          
    
    ```
- To access container you just simply use name. As example `docker exec -it blizy_php sh`

## Credentials
- ### Database :
  - username: root
  - password: password
  - database: blizy 
  - container name: db
- ### Database ui:
  - server: db
  - username: root
  - password: password
  - database: blizy
- ### Frontend:
  - website: localhost: 3000
- ### Backend:
  - Website is accesable over `localhost:8000`
  - Api platform: `localhost:8000/api`

## Setup containers:
- ### PHP
  - Go to container `docker exec -it blizy_php sh`
  - Type `composer install`
  - Then `bin/console doctrine:migrations:migrate`
- ### Frontend(nuxt)
    - Go to container `docker exec -it blizy_fronend sh`
    - Type `npm install`
    - <span style="color:red">ATTENTION  if using linux or MacOs you will need to remove `host: process.env.NUXT_HOST,` from `frontend/nuxt.config.ts` </span>
- ### Python scrapper
  - Go to container `docker exec -it blizy_python sh`
  - Run `pip install -r requirements.txt`
  - Then run `python main.py scrape-fundamentals`
  - Then run `python main.py scrape-products`
  - <span style="color:red">If the `python main.py scrape-products` run it again. (Problem is that models are not loaded after they are inserted - would need to look at it to fix)</span>
  - That's it it should work
- ### GO to `localhost:3000`
- 
## Considerations:
- Need to fix `model` load when products are synced to database. Problem is that after models are inserted and tried to fetch again data is empty.
- Current parser could be improved, because sometimes model is not parsed correctly
- Possibility to go inside "detailed" page and take all the info <- can ban ip if not careful enough
- Would need test
- Better error handling
- Needs Logging