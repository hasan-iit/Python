from operator import add
lt1 = [5, 10, 15, 20, 25, 30]
lt2 = [2, 4, 6, 8, 10, 12]
add_lst =[]
for i in range(len(lt1)):
    add_lst.append(lt1[i]+lt2[i])
print(add_lst)
lt3 = [2, 4, 6, 8, 10, 'shahed']
rsl_list =list(map(add,lt1,lt2))
print(rsl_list)

