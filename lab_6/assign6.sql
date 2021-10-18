-- q1
SELECT * FROM Student JOIN marks_sem1 ON Student.rollno=marks_sem1.rollno;

-- q2
SELECT name, marks_sem1.sports FROM Student JOIN marks_sem1 ON Student.rollno=marks_sem1.rollno;

-- q3
SELECT Student.name, marks_sem1.math, Student.rollno FROM Student JOIN Campus ON Student.cid=Campus.cid JOIN marks_sem1 ON Student.rollno=marks_sem1.rollno WHERE Campus.law=1;

-- q4
