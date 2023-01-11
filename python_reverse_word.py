
"""
Write a `reverseWords` function that accepts a string a parameter, and reverses each word in the string. Every space should stay, so you cannot use `words` from `Prelude`.
Example:
```
reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
```
"""

# Solution
def reverse_words(str):
  strList = []
  for word in str.split(' '):
      x = strList.append(word[::-1])
      y = ' '.join(strList)
  print(y)
#   return ' '.join(strList)
  
reverse_words("This is an example")

""" 
output
 "shiT si na elpmaxe"
 """
