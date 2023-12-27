docker-compose up -d postgres_db
docker-compose exec postgres_db psql -U postgres -c "CREATE DATABASE $1;"