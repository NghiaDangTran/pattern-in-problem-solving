# requency Counter - validAnagram
# Given two strings, write a function to determine if the second string is an anagram of the first. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Examples:

# validAnagram('', '') // true
# validAnagram('aaz', 'zza') // false
# validAnagram('anagram', 'nagaram') // true
# validAnagram("rat","car") // false) // false
# validAnagram('awesome', 'awesom') // false
# validAnagram('amanaplanacanalpanama', 'acanalmanplanpamana') // false
# validAnagram('qwerty', 'qeywrt') // true
# validAnagram('texttwisttime', 'timetwisttext') // true
# Note: You may assume the string contains only lowercase alphabets.

# Time Complexity - O(n)


# read the requiremnt
# look at some example read "" "" true understandble
# look next 'aaz', 'zza' a only apear once
# 'awesome', 'awesom' false
# 'awesome', 'awesomm'

def validAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    data = {}
    for i in s1:

        if i in data:
            data[i] += 1
        else:
            data[i] = 1

    for j in s2:
        if j in data:
            data[j] -= 1
            if data[j] < 0:
                return False
            

        else:
            return False
 
    return True


print(validAnagram('qwertya', 'qeywrte')
      )
