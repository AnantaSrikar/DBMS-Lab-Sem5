-- q1
SELECT name, dob, DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(dob, '%Y') - (DATE_FORMAT(NOW(), '00-%m-%d') < DATE_FORMAT(dob, '00-%m-%d')) AS age FROM Student HAVING age > 17 ORDER BY age DESC;

-- q2
SELECT COUNT(CASE WHEN gender='M' THEN 1 end) AS male_cnt, COUNT(CASE WHEN gender='F' THEN 1 end) AS female_cnt FROM Student WHERE DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(dob, '%Y') - (DATE_FORMAT(NOW(), '00-%m-%d') < DATE_FORMAT(dob, '00-%m-%d')) > 19;

-- q3
SELECT COUNT(*) as good_studs FROM Student where math > (SELECT (avg(math)+avg(sci)+avg(eng)+avg(social)+avg(sports))/5 FROM Student);

-- q4
SELECT unique (SELECT COUNT(*) FROM Campus where SUBSTR(pincode, 1, 1)='5' or SUBSTR(pincode, 1, 1)='6') as south, (SELECT count(*) FROM Campus where SUBSTR(pincode, 1, 1)='3' or SUBSTR(pincode, 1, 1)='4') AS west FROM Campus;

-- q5
SELECT name FROM Student ORDER BY (math+sci+eng+social+sports) DESC LIMIT 1,1;

-- q6
SELECT name, rollno, (math+sci+eng+social+sports)/5 AS avg_marks, (SELECT CASE WHEN avg_marks > (AVG(math)+AVG(sci)+AVG(eng)+AVG(social)+AVG(sports))/5 THEN 'High' else 'Low' end FROM Student) AS score_status FROM Student;