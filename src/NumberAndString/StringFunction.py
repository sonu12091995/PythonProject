
#Ways of String variable
l= "Welcome"
a= 'welcome'

p  = str("welcome")
k  = str('welcome')

# creating empty string
n = ""
n = ''
n = str()

#Imtable string
s = "sonu"
print(id(s)) #2395990788256
print(id(s))
s = s+"sharmaa"
print(s) #2395990788256



# + and * operator use in string
str1 = "sonu"
print(str1+"programming") #sonuprogramming
print(str1*5)# sonu print 10 time






# Slicing concept

# Original string
text = "Hello, World!"

# Slice from index 0 to 4 (excluding 5)
slice1 = text[0:5]
print("Slice 0 to 4:", slice1)  # Output: Hello

# Slice from index 7 to end
slice2 = text[7:]
print("Slice 7 to end:", slice2)  # Output: World!

# Slice with step of 2
slice3 = text[0:12:2]
print("Slice with step 2:", slice3)  # Output: Hlo ol

# Slice using negative indices
slice4 = text[-6:-1]
print("Slice with negative indices:", slice4)  # Output: World




#ord() and chr()
print(ord('A')) #65  Ascii value
print(chr(66)) # B

