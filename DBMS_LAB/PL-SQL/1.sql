declare
flag number:=0;
i number;
n number;

begin
n:=&num;
for i in 2..n/2 loop
if mod(n,i)=0 then
flag:=1;
exit;
end if;
end loop;

dbms_output.put_line(flag);
if flag=0 then
dbms_output.put_line(n||'is'||'Prime');
else
dbms_output.put_line(n|| 'is  not Prime');
end if;
end;
/
