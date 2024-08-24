# Regular Expressions in Python
# Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python.
#  They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

# Metacharacters in regular expressions
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE 
#     to match.
# ()  Enclose a group of REs
# Find list of more meta characters here - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions

# Searching for a pattern in re using re.findall() Method
# You can also use the re.findall function to find all occurrences of the pattern in a string:

# import re
# pattern = r"expression"
# text = "The cat is in the hat."
# matches = re.findall(pattern, text)
# print(matches)
# # Output: ['cat', 'hat']
# Replacing a pattern
# The following example shows how to replace a pattern in a string:

import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."
matches = re.findall(pattern, text)
print(matches)
# Output: ['cat', 'hat']
new_text = re.sub(pattern, "dog", text)
print(new_text)
# Output: "The dog is in the dog."
# Importing re Package
# In Python, regular expressions are supported by the re module. 
# The basic syntax for working with regular expressions in Python is as follows:
# Define a regular expression pattern
pattern = r"expression"
# Match the pattern against a string
text = "Hello, world!"
match = re.search(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")

# import re
# Searching for a pattern in re using re.search() Method
# re.search() method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching part of the string. This method stops after the first match, so this is best suited for testing a regular expression more than extracting data. We can use re.search method like this to search for a pattern in regular expression:
# import re
# pattern=r"[A-Z]+yclone"
# text='''
# This article is about the meteorological phenomenon. For other uses, see Cyclone (disambiguation).
# An extratropical cyclone near Iceland
# Part of a series on
# Weather
# Temperate and polar seasons
# Tropical seasons
# Storms and Dyclone
# Precipitation
# Topics
# Glossaries
# icon Weather portal
# vte
# In meteorology, a cyclone  is a large air mass that rotates around a strong center of low atmospheric pressure, counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Cyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4] The largest low-pressure systems are polar vortices and extratropical cyclones of the largest scale (the synoptic scale). Warm-core cyclones such as tropical cyclones and subtropical cyclones also lie within the synoptic scale.[5] Mesocyclones, tornadoes, and dust devils lie within the smaller mesoscale.
# '''
# matches=re.search(pattern, text)
# # for match in matches:
# print(matches)

# import re
# pattern=r"[A-Z]+yclone"
# text='''
# This article is about the meteorological phenomenon. For other uses, see Cyclone (disambiguation).
# An extratropical cyclone near Iceland
# Part of a series on
# Weather
# Temperate and polar seasons
# Tropical seasons
# Storms and Dyclone
# Precipitation
# Topics
# Glossaries
# icon Weather portal
# vte
# In meteorology, a cyclone  is a large air mass that rotates around a strong center of low atmospheric pressure, counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Cyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4] The largest low-pressure systems are polar vortices and extratropical cyclones of the largest scale (the synoptic scale). Warm-core cyclones such as tropical cyclones and subtropical cyclones also lie within the synoptic scale.[5] Mesocyclones, tornadoes, and dust devils lie within the smaller mesoscale.
# '''
# matches=re.finditer(pattern, text)
# for match in matches:
#   print(text[match.span()[0]: match.span()[1]])
#   print(match)

import re
pattern=r"[a-z]+at"
text="The cat sat on mat"
matches=re.sub(pattern, "dog", text) # it replaces all those words where at is found at the last of the word
print(matches)

import re
text = "The email address is example@example.com."
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    email = match.group()
    print(email)
# Output: example@example.com
# Conclusion
# Regular expressions are a powerful tool for working with strings and text data in Python.
#  Whether you're matching patterns, replacing text, or extracting information, regular expressions make it easy
#  to perform complex string operations with just a few lines of code. With a little bit of practice, 
# you'll be able to use regular expressions to solve all sorts of string-related problems in Python.