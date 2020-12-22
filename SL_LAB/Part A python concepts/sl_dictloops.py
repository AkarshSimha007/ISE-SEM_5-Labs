def sum_math_v_vi_average(list_of_dicts):
 avg=[]
 for d in list_of_dicts:
  n1=d.pop('v')
  n2=d.pop('vi')
  d['v'+'vi']=(n1+n2)/2
  avg.append(d['v'+'vi'])
 return avg

student_details=[{'id':1,'subject':'math','v':70,'vi':82},
{'id':2,'subject':'math','v':80,'vi':94},
{'id':3,'subject':'math','v':90,'vi':86}]

print(sum_math_v_vi_average(student_details))
