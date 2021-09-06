-- q11
SELECT name, (math+sci+eng+social+sports)/5 AS avg FROM Student ORDER BY avg DESC LIMIT 1;

-- q12
SELECT name FROM Student WHERE substr(name, 2, 1)='a';

-- q13
SELECT name, math FROM Student ORDER BY math;