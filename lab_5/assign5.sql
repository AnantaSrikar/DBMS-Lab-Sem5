-- All the new tables are created using create-db.py since it's easier to add data that way

-- Student table update

-- a. Dropping columns that are not required
ALTER TABLE Student DROP math;
ALTER TABLE Student DROP sci;
ALTER TABLE Student DROP eng;
ALTER TABLE Student DROP social;
ALTER TABLE Student DROP sports;

-- b. Add fk to rollno to sem1 rollno
ALTER TABLE Student DROP PRIMARY KEY; -- Since I used rollno as a primary key initially
ALTER TABLE Student ADD CONSTRAINT fk_rollno FOREIGN KEY (rollno) REFERENCES marks_sem1(rollno);

-- c. add cid
ALTER TABLE Student ADD cid INT;
-- Copy values as shown in table: Done in update-db.py

-- d. Add fk to cid to campus cid
ALTER TABLE Student ADD CONSTRAINT fk_cid FOREIGN KEY (cid) REFERENCES Campus(cid);

-- Campus table update

-- a. Make cid primary key
-- NOTE: CID is already a primary key, as I have made the table in that way back in lab_1.