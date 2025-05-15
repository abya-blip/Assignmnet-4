file  = open("output.txt" , "w")
a = str(input("Enter text to write to the file: "))
file.write(a)
print("Data successfully written to ouput.txt\n\n")
f.close()

file = open("output.txt" , "a")
a = str(input("Enter text to append to the file: "))
file.append(a)
print("Data successfully appended to out[ut.txt")
f.close()


file = open("output.txt" , "r")
a = file.read()
print("Final contents of the file: \n",a)

f.close()
