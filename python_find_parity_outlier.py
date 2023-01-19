'''
You are given an array (which will have a length of at least 3, but could be
very large) containing integers. The array is either entirely comprised of
odd integers or entirely comprised of even integers except for a single
integer N. Write a method that takes the array as an argument and returns N.
For example:
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11
[160, 3, 1719, 19, 11, 13, -21]
Should return: 160
'''
def find_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if i % 2 > 0:
            odds.append(i) # if the number has the remainder more than 0, it will consider as odd number
        if i % 2 == 0:
            evens.append(i) # if the number has the remainder equal to 0, it will conseder as even number
    print("Evens: ", evens) #print out all the even number 
    print("Odds: ", odds)   #print out all the odd number
    if len(evens) > len(odds): 
        return odds[0] 
    else:
        return evens[0]

print(find_outlier([2, 6, 8, 10, 3]))
