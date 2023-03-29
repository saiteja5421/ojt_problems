try:
    with open("file1.txt","a") as file:
        b =file.write("Hello World")
except :
    print("File not found")
    

# f =open("file1.txt","w")
# f.write("Hello world")
# f.close() 