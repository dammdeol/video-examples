docker run -d \
--name OracleDB \
--publish 1521:1521 \
--restart always \
--volume oracle_db:/ORCL \
store/oracle/database-enterprise:12.2.0.1-slim