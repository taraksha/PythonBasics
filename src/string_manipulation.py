#NOTE: These are just Python procedures. You can run this as such

def formatting():
    product_name = "Milk"
    quantity = 4
    price = 200
    print(f" You Have ordered {quantity} {product_name} for {quantity*price}")

formatting()


spl_charac = "He said \"I don't know\""
print(spl_charac)
single_quotes='He said "I don\'t know"'
print(single_quotes)

print("First line.\nSecond line.")
print('C:\some\name')
print(r'C:\some\name') #Use raw string for path as it avoids congusion


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# a \ above excludes that line

print(3 * 'yum' + 'ium')

word = "Python"
print(word[0]) #Indexing 0
print(word[-1]) #Last index

print(word[1:3]) #SLICE(substring) index 1,2

print(word[:3]) #until index 2
print(word[1:]) #from index 1
print(word[-3:]) # characters from the second-last (included) to the end
print(len(word))

replace = "Tutorial to replace string"
new_string = replace.replace("replace","new string")
print(new_string)

original = "How to \"split    \" using characters in String"
after_split= original.split("\"")[1].split("\"")[0].strip()
#split string into array of size 2. Use the required part using index
#Strip: strips the leading and trailing 0s
print(after_split)

#string.find("value") - finds the first occurrence of the value
print(after_split.find("z")) #-1 if not found

#JOIN: used to join a list using the seperator given
name = "asha selvaraj"
print(name)
initial = "".join(word[0].upper() for word in name.split())
print(initial)

corrected_name =  " ".join(word[0].upper()+word[1:] for word in name.split())
print(corrected_name)

print("To capitalize first word alone:",name.capitalize())
print("Swap case:",name.swapcase())
print("Title:",name.title())

