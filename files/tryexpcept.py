try:
  my_file = open("file1.txt","r")
except FileNotFoundError:
  print("Sorry, the file does not exist")
else:
  contents = my_file.read()
  print(contents)
  my_file.close()
finally:
  print("finally runs")
