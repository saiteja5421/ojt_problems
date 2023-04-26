



def add(a,b):
    return a+b


def sub(a,b):

    return a-b

def main():
    print(__name__)

if __name__=="__main__":
    main()
    

try:
    a,b=[1,2,3]
except ValueError as err:
    print("ValueError: {}".format(err))



