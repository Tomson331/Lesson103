type("Hello, world")
"class" 'str'

phrase = "Hello, world"
type = phrase
"class" 'str'

# String Literals
string1 = 'Hello, world'
string2 = "1234"
string3 = "We are winners"
string4 = 'Keep smiling'

text = "He asked, "Whose is this book?""
file "<stdin>" , line 1
text = "She answer, "It,s mine""

len("abc")
letters = "abc"
num_letters = len(letters)
num_letters

long_string = "This is multiline string is" \
              "displayed on one line"
print(long_string)
print("""An example of "
      "a string that spans across multiple lines"
      "that also preserves whitespace""")

# 4.1 What is the String?
# Solutions to review exercises

# Exercise 1
print('The are "two apostrophes" in this sting.')

# Exercise 2
print("The string has got one apostrophe.")

# Exercise 3
print(
    """This string was written on multiple lines,
      and it displays across multiple lines."""
)

# Exercise 4
print("This one-line string was written out \
      using multiple lines.")

# String Concatenation
string1 = "abra"
string2 = "cadabra"
magic_string = string1 + string2
magic_string

first_name = "Artur"
last_name = "Dent"
full_name = first_name + " " + last_name
full_name

# String Indexing
flavor = "apple pie"
flavor[1]
flavor[0]
flavor[9]
flavor[-1]
flavor[-10]

final_index = len(user_input) - 1
last_character = user_input[final_index]
last_character = user_input [-1]

# Slicing
first_three_letters = flavor[0] + flavor[1] + flavor[2]
first_three_letters
flavor = "apple pie"
flavor [0:3]
flavor[:5]
flavor[5:]
flavor[:]
flavor[:14]
flavor[13:15]
flavor[-9:-6]
flavor[-9:0]
flavor[-9:]

# Strings are Immutable
word = "goal"
word[0] = "f"
word = "goal"
word= "f" +  word[1:]

# 4.2 Concatenation, Indexing, Slicing
# Solutions to review exercises

# Exercise 1
# Display the number of letters in the string
my_string = "qwerdcfgdsvbfkf"
print(len)my_string

# Exercise 2
# Concatenate two strings together
string_up = "super"
string_down = "man"
print(string_up + string_down)

# Exercise 3
# Display two strings together, with a space in between
string_small = "I am"
string_big = "years old"
print(string_small + "37" + string_big)

# Exercise 4
# Use subscripting to display part of a string
print("bazinga" [2:6])

# 4.3 Manipulate Strings With Methods
# Converting String Case
# .lower()
"John Locke" .lower()
name = "John Locke"
name.lower()

# .upper()
loud_voice = "John Locke"
loud_voice.upper()
len(loud_voice)

# Removing Whitespace  a String
1. .rstrip()
2. .lstrip()
3. .strip()

name ="John Locke   "
name
name.rstrip()
name = "    John Locke"
name.lstrip()









