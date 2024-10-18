grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
st_aver = {}
a,b,j,k,s = len(grades[0]),len(grades[1]),len(grades[2]),len(grades[3]),len(grades[4])
sum_a,sum_b,sum_j,sum_k,sum_s = sum(grades[0]),sum(grades[1]),sum(grades[2]),sum(grades[3]),sum(grades[4])
aa = sum_a/a
bb = sum_b/b
jj = sum_j/j
kk = sum_k/k
ss = sum_s/s
grades_st = [["Aaron",aa],["Bilbo",bb],["Johnny",jj],["Khendrik",kk],["Steve",ss]]
aaa = dict(grades_st)
st_aver.update(aaa)
print(st_aver)