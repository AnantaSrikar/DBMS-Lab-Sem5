-- q1
SELECT cid FROM Campus WHERE law = 1;

-- q2
SELECT name, rollno, age, math, sci, sports FROM Student WHERE name="dave";

-- q3
SELECT name, rollno FROM Student WHERE math > 80 OR sci > 80;

-- q4
SELECT DISTINCT social FROM Student;

-- q5
SELECT count(name) FROM Student WHERE eng < 70;

-- q6
SELECT * FROM Student ORDER BY math+sci DESC LIMIT 1;

-- q7
SELECT loc FROM Campus WHERE engg=0;

-- q8
SELECT sum(case when engg=1 then cap else 0 end) AS stem, sum(case when engg=0 then cap else 0 end) AS no_stem FROM Campus;

-- q9
SELECT * FROM Student WHERE math > 70 AND  sci > 70 AND  eng > 70 AND  social > 70 AND sports > 70;

-- q10
SELECT count(*) FROM Student WHERE rollno >= 1 AND rollno <= 20;
SELECT count(*) FROM Student WHERE rollno >= 21 AND rollno <= 40;
SELECT count(*) FROM Student WHERE rollno >= 41 AND rollno <= 60;