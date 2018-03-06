#!/usr/bin/python





## read n character 0<= n <= infinity

f = open("input.in", "r") 
n = 10
print "Read",n, "chars."
print(f.read(n))
f.close()


# print the whole file content
f = open("input.in", "r") 

print "Read the whole file."
print(f.read())
f.close()


# Read line from file 
f = open("input.in", "r") 

print "Read line" 
print(f.readline())
f.close()


# Read N line from file 

f = open("input.in", "r") 
n=3
print "Read",n, "bytes from lines"
print(f.readline(10))
f.close()
print "DONE "

#file f can be considered as an array of lines
f = open("input.in", "r") 

for line in f:
	print line
f.close()
	
	
# Closing file is very important for performance
f = open("input.in", "r") 

f.close()





	
