-- q11
select name, (math+sci+eng+social+sports)/5 as avg from Student order by avg desc limit 1;

-- q12
select name from Student where substr(name, 2, 1)='a';

-- q13
select name, math from Student order by math;