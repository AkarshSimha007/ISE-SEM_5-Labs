declare
cursor my_cursor is
select * from employee;
p my_cursor%rowtype;
begin
open my_cursor;
dbms_output.put_line('Printing names of Employees and DeptNo');

loop
fetch my_cursor into p;
exit when my_cursor%notfound;
update employee
 set deptno=deptno+10;
  dbms_output.put_line(p.deptno||'  '||p.name);
end loop;
end;
/
