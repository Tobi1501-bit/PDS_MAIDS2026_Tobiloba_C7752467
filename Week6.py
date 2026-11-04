# Open and close a file
file1 = open(r"MyFile1.txt","w+")

file1 = open(r"MyFile1.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.write("Hello \n")
file1.writelines(L)    #Multiple string
file1.close()

file1 = open("MyFile1.txt","r+")

print("Output of Read function is ")
print(file1.read())
print()

# byte from the beginning.
file1.seek(0)

print( "Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)
# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
file1.seek(0)
print("Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()



#Appending to a file
file1 = open("Myfile1.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.writelines(L)
file1.close()


# Append-adds at last
file1 = open("Myfile1.txt","a")        #append mode
file1.write("Today \n")
file1.close()


file1 = open("Myfile1.txt","r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()

# Write-Overwrites
file1 = open("Myfile1.txt","w")           #write mode
file1.write("Tomorrow \n")
file1.close()


file1 = open("Myfile1.txt","r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()


import pandas as pd

df = pd.read_csv("data(2).csv")            #Read a CSV File
df.to_csv('data.csv')                      #Write to CSV File
print(df)

df.to_excel('data2.xlsx')                  #Write to Excel file
df = pd.read_excel('data2.xlsx')           #Read Excel file
print(df)

df.to_json('data(2).json')                 #Write to JSON
df.to_json('data(2g)-index.json', orient='index')
