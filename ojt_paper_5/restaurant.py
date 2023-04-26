class Restaurant:
    def __init__(self) -> None:
        self.menu_items={} 
        self.booked_table=[]
        self.customer_ordered={}

    def add_items_to_menu(self,item_name,price):
        self.menu_items[item_name]=price
        

    def book_table(self,table_number):
        if table_number not in self.booked_table:
            self.booked_table.append(table_number)
        else:
            print("this table number {} is already booked".format(table_number))
    
    def customer_order(self,item,quantity):
        self.customer_ordered[item]=quantity


    def print_menu(self):
        print("item price")
        for i,j in self.menu_items.items():
            print("{}  {}".format(i,j))    

    def print_table_reversation(self):
        for i in self.booked_table:
            print("table {} is  booked".format(i))

    def print_customer_order(self):
        print("your order details")
        total=0
        for i,j in self.customer_ordered.items():
            total+=(self.menu_items[i])*j
            print("{} {}".format(i,j))
        print("your total bill is {}".format(total))
              

Restaurant_obj=Restaurant()
Restaurant_obj.add_items_to_menu("idly",40)
Restaurant_obj.add_items_to_menu("Dosa",50)
Restaurant_obj.add_items_to_menu("puri",40)
Restaurant_obj.print_menu()
Restaurant_obj.book_table(2)
Restaurant_obj.book_table(1)
Restaurant_obj.customer_order("idly",2)
Restaurant_obj.customer_order("Dosa",1)
Restaurant_obj.print_table_reversation()
Restaurant_obj.print_customer_order()


import re
a="saiteJa@2"
def strong_password(a): 
    if len(a)>=8:          
        if re.search(r"[!@#$%^&*]",a) and re.search(r'[A-Z]',a) and re.search(r'[a-z]',a) and \
                    re.search(r'\d',a):
                        return True

    return False

print(strong_password(a))

# import threading
# import time
# def cube(num):
#     print(num*num*num)

# def square(num):
#     print(num*num)

# start_time=time.time()
# T1=threading.Thread(target=cube,args=([50]))
# T2=threading.Thread(target=square,args=([50]))
# T1.start()
# T2.start()
# T1.join()
# T2.join()
# end=time.time()

# print(end-start_time)

# import multiprocessing 
# import time  

  
# def cube(num):
#     print(num*num*num)

# def square(num):
#     print(num*2)

# def sqrt(num):
#     print(num*num)

    
# if __name__=="__main__":
#     start=time.time()
#     T1=multiprocessing.Process(target=cube,args=([50]))
#     T2=multiprocessing.Process(target=square,args=([50]))
#     T3=multiprocessing.Process(target=sqrt,args=([50000]))
#     T1.start()
#     T2.start()
#     T3.start()
#     T1.join()
#     T2.join()
#     T3.join()
#     end=time.time()
#     print(end-start)
    
