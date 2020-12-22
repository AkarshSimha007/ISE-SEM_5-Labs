declare
cursor v_emp is
select * from employee;

emp v_emp%rowtype;

begin
open v_emp;
loop
fetch v_emp into emp;
exit when v_emp%notfound;
dbms_output.put_line(emp.ssn||' '||emp.deptno);
end loop;
close v_emp;
end;
/
