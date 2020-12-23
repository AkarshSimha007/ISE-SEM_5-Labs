declare
cursor  c1 is 
select * from employee;

v_emp c1%rowtype;

begin
open c1;
loop
fetch c1 into v_emp;
exit when c1%notfound;

insert into employee1 values(v_emp.ssn,v_emp.name,v_emp.deptno);
end loop;
end;
/
