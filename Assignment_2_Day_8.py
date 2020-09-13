name = input("Enter the file name: ")
try:
    fh = open(name, 'r')
    fh.write("Hey, this is text file")
    fh.close()
except IOError:
    print('You cannot write in file with other operations, please use correct operation')
