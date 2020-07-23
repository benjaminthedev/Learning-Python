# Declare a var and print it

#f = 0

# print(f)


# Re-declare the var

f = "abcdefg"
print(f)


# An error has occured as vars of differnt types cannot be combined.

print("This is a string " + str(123))


# Global vs local vars in functions

def newFunction():
    # this makes it global:
    global f
    f = "newOne"
    print(f)


newFunction()
print(f)


# Deletes
#del f
# Now Throws error!
# print(f)
