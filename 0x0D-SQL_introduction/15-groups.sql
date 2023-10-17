-- A script that groups number of records
SELECT score, COUN T(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
