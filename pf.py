# num_list= [0,1,2,3,4,5]
# double_list=[]
# even_num=[]
# for x in num_list:
#     double_list.append(x*2)

# print(double_list)

# for x in num_list:
#     if(x%2==0):
#         even_num.append(x)

# print(even_num)

# def even(x):
#     return x%2==0
# even_func=list(filter(even,num_list))
# print(even_func)


#fungsi lambda
# greeting = lambda name: print(f"WOIIIIIII, {name}")
# sapa = greeting
# greeting("dastin")

#list compeheresion
# numb =[0,1,2,3,4,5]
# double = [x*2 for x in numb]
# print(double)

#reducing
# from functools import reduce
# numb = [1,2,3,4,5]

# def get_sum(acc,x):
#     print(f'acc is {acc}, x is {x}')
#     return acc + x
# sum = reduce(get_sum,numb)
# print(sum)

#combining
karyawan = [{
    'name': "A",
    'gaji': 2000,
    'div': 'dev'
},{
    'name': "b",
    'gaji': 3000,
    'div': 'bos'
}]

#filter
def apani(karyawan):
    return karyawan['div']=='bos'
dev = list(filter(apani, karyawan))

def gajian(karyawan):
    return karyawan['gaji']
list_gaji=list(map(gajian,dev))
print(list_gaji)