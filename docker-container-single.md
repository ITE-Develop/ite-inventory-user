docker run -p 5050:80 \
        -e 'PGADMIN_DEFAULT_EMAIL=2820.mai.reaksa@rupp.edu.kh' \
        -e 'PGADMIN_DEFAULT_PASSWORD=222444' \
        -e 'PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION=True' \
        -e 'PGADMIN_CONFIG_CONSOLE_LOG_LEVEL=10' \
        --network=mynet \
        --restart=always \
        --name pgadmin4 \
        -d dpage/pgadmin4


docker run --name postgres \
        -p 5432:5433 \
        -e POSTGRES_PASSWORD=dbApi@2024! \
        -e POSTGRES_USER=admin \
        -e POSTGRES_DB=api_db \
        --network=mynet \
        --restart=always \
        -d postgres


docker run --name mysql \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=Rupp2357.! \
    --network mynet \
    --restart=always \
    -d mysql:latest



docker network create mynet


