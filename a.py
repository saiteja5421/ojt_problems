# # def decor1(func):
# # 	def inner():
# # 		x=func()
# # 		# print(x * x)
# # 		return x * x 
# # 	return inner

# def decor(func):
# 	def inner():
# 		x = func()
# 		# print(2 + x)
# 		return 2 + x
# 	return inner 

# # @decor1
# # @decor
# def num():
# 	a=10
# 	# print(a)
# 	return a  

#print(num())

# # a=decor1(decor(num))
# # print(a())

# a=decor1(decor(num))
# print(a())


# m=list(input())
# n=input()
# out=[]
# for i,j in (enumerate(m)):
#     if j==n:
#         k=m.copy()
#         k.pop(i)
#         # print("".join(k))
#         out.append("".join(k))
        
# print(max(out))


# a=402
# b=407
# print(id(a) is id(b))



import pickle
  
def storeData():
    # initializing data to be stored in db
    Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',
    'age' : 21, 'pay' : 40000}
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
    'age' : 50, 'pay' : 50000}
    # database
    db = {}
    db['Omkar'] = Omkar
    db['Jagdish'] = Jagdish
    print("sai")      
    # Its important to use binary mode
    dbfile = open('examplePickle.txt', 'ab')
    # source, destination
    pickle.dump(db, dbfile)                     
    dbfile.close()
  
def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle.txt', 'rb')     
    db = pickle.load(dbfile)
    print(db)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()

# storeData()
loadData()

a ="%"
print(a.isalpha())








