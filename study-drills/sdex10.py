# Study Drills 10

# 1. Memorize all the escape sequences by putting them on flash cards.
# 2. Use ''' (triple-single-quote) instead. 
# Can you see why you might use that instead of """?
# 3. Combine escape sequences and format strings to create a more complex format.

print("ex10.py".center(100, "-"))

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# Using """ or ''' will give the same result. 
# "I'll do a list:" starts on line 6 after ''' on line 5. 
# Thus, there's a space character between them at the end of line 5. 
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

# Print the string the variable tabby_cat refers to.
# i.e. Print a tab and then "I'm tabbed in."
print(tabby_cat)
# Print the string the variable persian_cat refers to.
# i.e. Print "I'm split", a new line and "on a line."
print(persian_cat)
# Print the string the variable backslash_cat refers to. 
# i.e. Print "I'm ", a backslash \, " a ", a backslash \ and " cat."
print(backslash_cat)
# Print the string the variable fat_cat refers to.
# i.e. Print a new line, the text inside triple-quotes and a new line. 
# When pressing enter after ''' or """, \n is input. 
# Python will print out a new line before "I'll do a list:". 
# Likewise, when pressing enter after "Grass", there will be \n. 
print(fat_cat)

# NOTES:
# Escape a double/single quote inside single/double quotes to include it in the string. 
# Here’s an example:
print("I am 6'2\" tall.") # escape double-quote inside string
print('I am 6\'2" tall.') # escape single-quote inside string

print("Escape Sequences".center(100, "-"))

# List of all the escape sequences Python supports:
#   \\          Backslash (\)
#   \'          Single-quote (')
#   \"          Double-quote (")
#   \a          ASCII bell (BEL)
#   \b          ASCII backspace (BS)
#   \f          ASCII formfeed (FF)
#   \n          ASCII linefeed (LF)
#   \N{name}    Character named name in the Unicode database (Unicode only)
#   \r          ASCII carriage return (CR)
#   \t          ASCII horizontal tab (TAB)
#   \uxxxx      Character with 16-bit hex value xxxx (Unicode only)
#   \Uxxxxxxxx  Character with 32-bit hex value xxxxxxxx (Unicode only)
#   \v          ASCII vertical tab (VT)
#   \ooo        Character with octal value oo
#   \xhh        Character with hex value hh
print("Backslash:", "{0:s}".format("\\"))
print("Backslash:", "{0!r} (raw format)".format("\\"))
print("Single-quote:", '{0:s}'.format("\'"))
print("Single-quote:", '{0!r} (raw format)'.format("\'"))
print("Double-quote:", "{0:s}".format("\""))
print("Double-quote:", "{0!r} (raw format)".format("\""))
# \a makes ringing the bell alert sounds.
print("ASCII bell (BEL):", "{0:s}".format("\a"))
print("ASCII bell (BEL):", "{0!r} (raw format)".format("\a"))
# \b removes previous character. 
print("ASCII backspace (BS):", "{0:s}".format("\b"))
print("ASCII backspace (BS):", "{0!r} (raw format)".format("\b"))
# \f causes printers to automatically advance one full page or the start of the next page.
print("ASCII formfeed (FF):", "{0:s}".format("\f"))
print("ASCII formfeed (FF):", "{0!r} (raw format)".format("\f"))
print("ASCII linefeed (LF):", "{0:s}".format("\n"))
print("ASCII linefeed (LF):", "{0!r} (raw format)".format("\n"))
print("\\N{INVERTED EXCLAMATION MARK}:", "{0:s}".format("\N{INVERTED EXCLAMATION MARK}"))
print("\\N{INVERTED EXCLAMATION MARK}:", "{0!r} (raw format)".format("\N{INVERTED EXCLAMATION MARK}"))
print("ASCII carriage return (CR):", "{0:s}".format("\r"))
print("ASCII carriage return (CR):", "{0!r} (raw format)".format("\r"))
print("ASCII horizontal tab (TAB):", "{0:s}".format("\t"))
print("ASCII horizontal tab (TAB):", "{0!r} (raw format)".format("\t"))

print("Backspace".center(100, "-"))
# When putting \\b in between characters, \\b will delete the previous character.
print("Example:")
print("a\bb")
print("a{0:s}b".format("\b"))

print("Character named name in the Unicode database".center(100, "-"))
print("Link:", "http://www.unicode.org/Public/UCD/latest/ucd/NamesList.txt")

print("Carriage return".center(100, "-"))
print("Example:")
print("1919\r20")

print("Horizontal tab".center(100, "-"))
print("Example:")
print("start of tab\tend of tab")

print("Piece of fun code".center(100, "-"))
while True: 
    for i in ["/", "-", "\\", "|"]:
        print("{0:s}\r".format(i), end="")