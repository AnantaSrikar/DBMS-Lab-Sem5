select cid from Campus where law=1;
select name, rollno, age, math, sci, sports from Student where name="dave";
select name, rollno from Student where math>80 or sci > 80;
select distinct social from Student;
select count(name) from Student where eng < 70;
select * from Student order by math+sci desc;
select loc from Campus where engg=0;

select * from Student where math> 70 and  sci> 70 and  eng > 70 and  social> 70 and sports > 70;

select name, (math+sci+eng+social+sports)/5 as avg from Student order by avg desc limit 1;
select name from Student where substr(name, 2, 1)='a';
select name, math from Student order by math;