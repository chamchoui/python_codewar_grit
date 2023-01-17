"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""
def generate_hashtag(s):
    s = '#'+s.title() #add hashtag in the front of the string
    s = s.split()     #split the string by the whitespace
    s = ''.join(s)    #join the string w/o any whitespace
    if len(s) in range(2,140): # this loop check the condition within range until 140 char, beyond 140 char the loop return False
        return s
    else:
        return False
    

print(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')    
print(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')
