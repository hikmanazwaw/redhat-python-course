# Python is case sensitive. Therefore, the following two variables are different
the_Person = "Him"
the_person = "Her"

# Python statements do not end with a semicolon, but you can use one to separate two statements on the same line
length = 10; width = 5
area = length * width
print(area)

# You can continue a long statement by placing the \ character at the end of the line.
message = "This is a long string just to \
illustrate continuation across multiple lines"

result = 500 * 2 + \
400 * 3

# The following snippet of code uses the print() function with multiple arguments.
data = "This is just a string of text"
print("This is the first argument",
      "This is the second argument",
      data)

# sep: untuk display between argument
# end: untuk last parameter
print("Hello", 123, "Goodbye", 5 + 9, sep=":", end="###")
Hello:123:Goodbye:14### 

# syntax input()
response = input("Please enter some text:")
Please enter some text:Hello
response = input("Please enter some text:\n")
Please enter some text:
Goodbye
print("The last response is", response, sep=":")
The last response is:Goodbye


response = input("Please enter a number: ")
Please enter a number: 456
print("The response of", response, "is of type", type(response))
The response of 456 is of type <class 'str'>