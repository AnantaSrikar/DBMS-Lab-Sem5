-- q1
SELECT name FROM Student WHERE team='R' UNION SELECT name FROM Student WHERE gender='F';

-- q2
SELECT team, count(*) AS COUNT FROM Student GROUP BY team;

-- q3
SELECT team, avg(math) FROM Student WHERE gender='M' GROUP BY team;

-- q4
SELECT * FROM Student ORDER BY team;

--q5
SELECT team, avg(sci) FROM Student GROUP BY team ORDER BY avg(sci) LIMIT 2;