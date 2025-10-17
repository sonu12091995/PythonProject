
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



# max,min,length
print(max("abc"))#c
print(min("abc"))#a
print(len("abc"))#3


# in or not in
fruite = "bnanna"
print("uite" in fruite) # (true) in means uite is the part of fruite
print("sone" not in fruite) #(true) not in means sonu is not part of fruite


# String compersion

# Example 8: String comparison

print("tim" == "tie")         # False → 'tim' is not equal to 'tie'
print("free" != "freedom")    # True  → the two strings are different
print("arrow" > "aron")       # True  → compared alphabetically ('a'=='a', 'r'=='r', 'r'>'o')
print("right" >= "left")      # True  → 'r' comes after 'l' in dictionary order
print("teeth" < "tee")        # False → 'teeth' is longer but starts with 'tee', so it's greater
print("yellow" <= "fellow")   # False → 'y' comes after 'f'
print("abc" > "")             # True  → any non-empty string is greater than an empty string



# Example9 : Testing strings True/False

s = "welcome to python"

print(s.isalnum())                # False
print("Welcome".isalpha())        # True

print("2012".isdigit())           # True

print("first Number".isidentifier())  # False

print(s.islower())                # True
print("WELCOME".isupper())        # True

print(" ".isspace())              # True
